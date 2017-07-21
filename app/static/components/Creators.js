var React = require('react');
var api = require('./api.js');
var Table = require('./Table.js');
var Card = require('./Card.js');
import ReactLoading from 'react-loading';
import { PageHeader, Pagination, Button, 
		 ButtonGroup, ButtonToolbar,
		 Grid, Row, Col, FormGroup, FormControl, Form } from 'react-bootstrap';

var fixMargin = {
	margin: '0'
}

var imgNotFound = "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available/standard_xlarge.jpg";
var photoFilter = [{'name': 'img','op': 'does_not_equal', 'val': imgNotFound}];
var descFilter = [{'name': 'desc','op': '!=', 'val': ''}];
var orderByAsc = "full_name";
var orderByDsc = "-full_name";

class Creators extends React.Component{
	constructor(props) {
	    super();
	    this.state = {
	      creators: null,
	      activePage: 1,
	      numPages: 0,
	      hasPhoto: false,
	      hasDesc: false,
	      sortAsc: true,
    	};

    	this.handleSelect = this.handleSelect.bind(this); //pls work
    	this.updateCreators = this.updateCreators.bind(this); //pls work
    	this.applyFilter = this.applyFilter.bind(this);
    	this.loadTable = this.loadTable.bind(this);
    	this.handleChange = this.handleChange.bind(this);
	   	this.jumpToPage = this.jumpToPage.bind(this);
    	this.cancelFilter = this.cancelFilter.bind(this);
  	}

	componentWillMount() {
	    this.updateCreators(this.state.creators)
	}

	updateCreators(creators) {
		var filter;
		var orderBy;
		this.setState(function() {
			return {
				creators: creators
			}
		});

		if(this.state.hasPhoto) {
			filter = photoFilter;
		}
		else if(this.state.hasDesc) {
			filter = descFilter;
		}

		if(this.state.sortAsc){
			orderBy = orderByAsc;
		}
		else{
			orderBy = orderByDsc;
		}


		api.getCreators(this.state.activePage, filter, orderBy)
	      .then(function (creators) {
	        this.setState(function () {
	          return {
	            creators: creators.data,
	            numPages: Math.ceil(creators.meta.total / 6)
	          }
	        });
	      }.bind(this));
	}

	handleSelect(eventKey){
		this.setState({activePage: eventKey}, function () {
			this.updateCreators(null);
		});
	}

	applyFilter(filterKey){
	    if(filterKey === 1) {
	    	this.setState({
	    		hasPhoto: true,
	    		hasDesc: false
	    	}, function() {
	    		this.updateCreators(null);
	    	});
	    }
	    else if(filterKey === 2){
	    	this.setState({
	    		hasPhoto: false,
	    		hasDesc: true
	    	}, function() {
	    		this.updateCreators(null);
	    	});
	    }
	}

	applySort(sortKey){
		if(sortKey === 1){
			this.setState({
				sortAsc: true
			}, function(){
				this.updateCreators(null);
			});
		}
		else if(sortKey === 2){
	    	this.setState({
	    		sortAsc: false
	    	}, function() {
	    		this.updateCreators(null);
	    	});
	    }
		
	}

	createCards() {
		var cardsArray = [];
		const { creators } = this.state;
		for(var i = 0; i < creators.length; i++) {
				cardsArray.push(<Card modelLink="/creatorInstance" 
								      modelInstance={creators[i]} />);
		}
		return cardsArray;
	}

	handleChange(e){
		this.state.activePage = Number(e.target.value);
	}

	jumpToPage(){
		this.setState({}, function(){
			this.updateCreators(null);
		});
	}

	cancelFilter(){
		this.setState({hasDesc: false, hasPhoto: false}, function(){
			this.updateCreators(null);
		})
	}

	loadTable(){
		if(!this.state.creators){
            return <div style={{display: 'flex', justifyContent: 'center'}}>
	            			<ReactLoading type="bars" height='650px' width='375px'
	            						  delay={5} color='red' />
            	   </div>
        }   
        else{
         	return (
         		<div className="text-center">
	         		<Table cards={this.createCards()}/>
	         		<Row>
	         		<Col xs={0} sm={2} md={2}/>
	         		 <Col xs={12} sm={8} md={8}>
		          		<Pagination
				       	prev
				        next
				        ellipsis
				        boundaryLinks
				        style={{marginBottom: '0px'}}
				        items={this.state.numPages}
				        maxButtons={5}
				        activePage={this.state.activePage}
				        onSelect={this.handleSelect} />
			        
			       
							<h3 className="text-center" style={fixMargin}>JUMP TO PAGE #:</h3>
							<Col sm={5} md={5}/>
							<Col sm={2} md={2}>
								<FormControl type="text"
										 className="center-block"
										 id="activePage"
										 onChange={this.handleChange} />
								<p/>
								<Button bsStyle="red" onClick={() => this.jumpToPage()}>
										JUMP
								</Button>
							<h3/>
							</Col>
							<Col sm={5} md={5}/>
					</Col>
					<Col xs={0} sm={2} md={2}/>
					</Row>
		    	</div>
		    );
		}
	}

	render(){
		return(
			<div>
				<PageHeader className="text-center" style={fixMargin}>CREATORS</PageHeader>
					<Row>
						<Col sm={2} md={2}/>
						<Col sm={4} md={4}>
							<ul className="list-unstyled">
								<li className="text-center">
									<h3 className="text-center">FILTER BY:</h3>

										<Button bsStyle="red" onClick={() => this.applyFilter(1)}>
												Photo Available
										</Button>
									{this.state.hasPhoto ? <div>
										<p>Photo Filter Applied</p>
										<Button bsStyle="red" onClick={() => this.cancelFilter()}>
											Deactivate Filter
										</Button></div> : <p/>}
								</li>
							</ul>
						</Col>
						
						<Col sm={4} md={4}>
							<ul className="list-unstyled">
								<li className="text-center">
									<h3 className="text-center">SORT BY:</h3>
										<Button bsStyle="red" onClick={() => this.applySort(1)}>
												Ascending
										</Button>
										{" "}
										<Button bsStyle="red" onClick={() => this.applySort(2)}>
												Descending
										</Button>
										{this.state.sortAsc ? <p>Sorting by Ascending Name</p> : <p>Sorting by Descending Name</p> }
								</li>
							</ul>
						</Col>
						<Col sm={2} md={4}/>
					</Row>
				<PageHeader style={{marginTop: '0px'}}/> {/*Makes line across screen*/}
				{this.loadTable()}
			</div>
		)
	}

}

module.exports = Creators;