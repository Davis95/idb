# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = mixed-indentation
# pylint: disable = missing-docstring
# pylint: disable = no-member
# pylint: disable = relative-import
# pylint: disable = line-too-long
# pylint: disable = trailing-whitespace
# pylint: disable = multiple-imports
# pylint: disable = bad-continuation
# pylint: disable = trailing-newlines

from unittest import main, TestCase
import json, simplejson
import requests
from models import db, Character, Comic, Event, Series, Creator
from idb import app
#

class UnitTest(TestCase):

    def test_add_series(self):
	
	with app.app_context():

        	newSeries = Series(id=9021090, title="Testing 123", desc="This is a test Series",
                           start=2015, end=2018, img="http://www.whitehouse.gov/logo.jpg", num_creators=1,
                           num_characters=8, num_comics=289, num_events=4)
        	db.session.add(newSeries)
		db.session.commit()
		query = db.session.query(Series).filter_by(id="9021090").first()
		self.assertEqual(query.id, 9021090)
		self.assertEqual(query.title, "Testing 123")
		self.assertEqual(query.desc, "This is a test Series")
		self.assertEqual(query.start, 2015)
		self.assertEqual(query.end, 2018)
		self.assertEqual(query.img, "http://www.whitehouse.gov/logo.jpg")
		self.assertEqual(query.num_creators, 1)
		self.assertEqual(query.num_characters, 8)
		self.assertEqual(query.num_comics, 289)
		self.assertEqual(query.num_events, 4)
		db.session.delete(newSeries)
		db.session.commit()

    def test_add_comic(self):

	with app.app_context():

		newComic = Comic(id=9021090, title="Test Comic", issue_num=4, desc="Test Desc", upc="12345678",
				 pg_ct=88, price=4.99, img="http://www.utexas.edu/diploma.gif", num_creators=6, num_characters=7, num_events=3)
		db.session.add(newComic)
		db.session.commit()
		query = db.session.query(Comic).filter_by(id="9021090").first()
		self.assertEqual(query.id, 9021090)
		self.assertEqual(query.title, "Test Comic")
		self.assertEqual(query.img, "http://www.utexas.edu/diploma.gif")
		self.assertEqual(query.num_creators, 6)
		self.assertEqual(query.num_characters, 7)
		self.assertEqual(query.num_events, 3)
		db.session.delete(newComic)
		db.session.commit()

    def test_add_creator(self):

	with app.app_context():

		newCreator = Creator(id=9021090, full_name="Fake Creator",
				     img="http://www.whitehouse.gov/obama.jpg", num_comics=1, num_series=8, num_events=44)
		db.session.add(newCreator)
		db.session.commit()
		query = db.session.query(Creator).filter_by(id="9021090").first()
		self.assertEqual(query.id, 9021090)
		self.assertEqual(query.full_name, "Fake Creator")
		self.assertEqual(query.img, "http://www.whitehouse.gov/obama.jpg")
		self.assertEqual(query.num_comics, 1)
		self.assertEqual(query.num_series, 8)
		self.assertEqual(query.num_events, 44)
		db.session.delete(newCreator)
		db.session.commit()

    def test_add_character(self):

	with app.app_context():

		newCharacter = Character(id=9021090, name="Manchurian Candidate",
					 desc="This guy is some Character",
					 img="http://www.kremlin.org/trump.png",
								     num_comics=1001, num_series=88, num_events=0)
		db.session.add(newCharacter)
		db.session.commit()
		query = db.session.query(Character).filter_by(id="9021090").first()
		self.assertEqual(query.id, 9021090)
		self.assertEqual(query.name, "Manchurian Candidate")
		self.assertEqual(query.desc, "This guy is some Character")
		self.assertEqual(query.img, "http://www.kremlin.org/trump.png")
		self.assertEqual(query.num_comics, 1001)
		self.assertEqual(query.num_series, 88)
		self.assertEqual(query.num_events, 0)
		db.session.delete(newCharacter)
		db.session.commit()

    def test_add_event(self):
	
	with app.app_context():

		newEvent = Event(id=9021090, title="The Big Short",
					desc="Wall Street trips and falls",
				 img="http://www.boa.com/freemoney.jpg", num_creators=987654,
							     num_characters=1000, num_comics=787, num_series=1)
		db.session.add(newEvent)
		db.session.commit()
		query = db.session.query(Event).filter_by(id="9021090").first()
		self.assertEqual(query.id, 9021090)
		self.assertEqual(query.title, "The Big Short")
		self.assertEqual(query.desc, "Wall Street trips and falls")
		self.assertEqual(query.img, "http://www.boa.com/freemoney.jpg")
		self.assertEqual(query.num_creators, 987654)
		self.assertEqual(query.num_characters, 1000)
		self.assertEqual(query.num_comics, 787)
		self.assertEqual(query.num_series, 1)
		db.session.delete(newEvent)
		db.session.commit()

    def test_add_character_with_null_img(self):
	
	with app.app_context():

		newCharacter = Character(id=9021090, name="Argent",
					 desc="She is a Character",
					 img=None, num_comics=0, num_series=0, num_events=0)
		db.session.add(newCharacter)
		db.session.commit()
		query = db.session.query(Character).filter_by(id="9021090").first()
		self.assertEqual(query.id, 9021090)
		self.assertEqual(query.name, "Argent")
		self.assertEqual(query.desc, "She is a Character")
		self.assertEqual(query.img, None)
		self.assertEqual(query.num_comics, 0)
		self.assertEqual(query.num_series, 0)
		self.assertEqual(query.num_events, 0)
		db.session.delete(newCharacter)
		db.session.commit()

    def test_add_creator_with_null_img(self):

        with app.app_context():
	
		newCreator = Creator(id=9021090, full_name="Alan Hopkins",
				     img=None, num_comics=0, num_series=0, num_events=0)
		db.session.add(newCreator)
		db.session.commit()
		query = db.session.query(Creator).filter_by(id="9021090").first()
		self.assertEqual(query.id, 9021090)
		self.assertEqual(query.full_name, "Alan Hopkins")
		self.assertEqual(query.img, None)
		self.assertEqual(query.num_comics, 0)
		self.assertEqual(query.num_series, 0)
		self.assertEqual(query.num_events, 0)
		db.session.delete(newCreator)
		db.session.commit()


#    def test_character_get_request(self):
#	
#	with app.app_context():
#	
#		headers = {"Content-Type": "application/vnd.api+json", "Accept": "application/vnd.api+json"}
#		api_request = requests.get("http://marveldb.net/api/characters/500", headers=headers)	
#		
#		api_id = (int)((json.loads(api_request.text))['data']["id"])
#		api_img = (json.loads(api_request.text))['data']['attributes']["img"]
#
#		db_request = db.session.query(Character).get(500)
#		db_id = db_request.id
#		db_img = db_request.img
#		self.assertEqual(api_id, db_id)
#		self.assertEqual(api_img, db_img)

    def test_series_get_request(self):
	
	with app.app_context():

		headers = {"Content-Type": "application/vnd.api+json", "Accept": "application/vnd.api+json"}
		api_request = requests.get("http://marveldb.net/api/series/7524", headers=headers)
		api_id = (int)((json.loads(api_request.text))['data']["id"])
		api_img = (json.loads(api_request.text))['data']['attributes']["img"]

		db_request = db.session.query(Series).get(7524)
		db_id = db_request.id
		db_img = db_request.img
		self.assertEqual(api_id, db_id)
		self.assertEqual(api_img, db_img)

    def test_creator_get_request(self):
	
	with app.app_context():

		headers = {"Content-Type": "application/vnd.api+json", "Accept": "application/vnd.api+json"}
		api_request = requests.get("http://marveldb.net/api/creators/621", headers=headers)
		api_id = (int)((json.loads(api_request.text))['data']["id"])
		api_img = (json.loads(api_request.text))['data']['attributes']["img"]

		db_request = db.session.query(Creator).get(621)
		db_id = db_request.id
		db_img = db_request.img
		self.assertEqual(api_id, db_id)
		self.assertEqual(api_img, db_img)

    def test_event_get_request(self):

	with app.app_context():

		headers = {"Content-Type": "application/vnd.api+json", "Accept": "application/vnd.api+json"}
		api_request = requests.get("http://marveldb.net/api/events/306", headers=headers)
		api_id = (int)((json.loads(api_request.text))['data']["id"])
		api_img = (json.loads(api_request.text))['data']['attributes']["img"]

		db_request = db.session.query(Event).get(306)
		db_id = db_request.id
		db_img = db_request.img
		self.assertEqual(api_id, db_id)
		self.assertEqual(api_img, db_img)

    def test_comic_get_request(self):
	
	with app.app_context():
	
		headers = {"Content-Type": "application/vnd.api+json", "Accept": "application/vnd.api+json"}
		api_request = requests.get("http://marveldb.net/api/comics/428", headers=headers)
		api_id = (int) ((json.loads(api_request.text))['data']["id"])
		api_img = (json.loads(api_request.text))['data']['attributes']["img"]

		db_request = db.session.query(Comic).get(428)
		db_id = db_request.id
		db_img = db_request.img
		self.assertEqual(api_id, db_id)
		self.assertEqual(api_img, db_img)


    def test_character_POST_request(self):


	with app.app_context():
		headers = {"Content-Type": "application/vnd.api+json", "Accept": "application/vnd.api+json"}
	 
		data = {"data": {"attributes": {"desc": "testing", "img": "test bruh", "name": "test man", "num_comics": 7, "num_events": 7, "num_series": 7},
		"id": "3000000", "links": {"self": "http://marveldb.net/api/characters/3000000"},
		"relationships": {"comics": {"data": [], "links": {"related": "/api/characters/3000000/comics", "self": "/api/characters/3000000/relationships/comics"}},
		"events": {"data": [], "links": {"related": "/api/characters/3000000/events", "self": "/api/characters/3000000/relationships/events"}},
		"series": {"data": [], "links": {"related": "/api/characters/3000000/series", "self": "/api/characters/3000000/relationships/series"}}},
		"type": "characters" }, "jsonapi": {"version": "1.0"}, "links": {"self": "/api/characters"}, "meta": {}}

		postreq = requests.post("http://marveldb.net/api/characters", simplejson.dumps(data),  headers=headers)

		self.assertEqual(201, postreq.status_code) 
		
		data = {"type": "characters", "id":"3000000", "attributes": {"id": "3000000", "name": "bubba", "desc" : "gump", "img" : "shellfish company", "num_comics": "7", "num_series": "7", "num_events": "7"}}

		patchreq = requests.patch("http://marveldb.net/api/characters/3000000", simplejson.dumps({"data": data}), headers=headers)
		self.assertEqual(204, patchreq.status_code)

		deletereq = requests.delete("http://marveldb.net/api/characters/3000000", headers=headers)
		
		self.assertEqual(204, deletereq.status_code)


    def test_comic_HTTP_requests(self):


	with app.app_context():
		headers = {"Content-Type": "application/vnd.api+json", "Accept": "application/vnd.api+json"}
	 
		data = {"data": {"attributes": {"desc": "testing", "img": "spidey pic", "issue_num": 313, "num_characters": 22, "num_creators": 2, "num_events": 7, "pg_ct": 32, "price": 200.0, "title": "spidey test man passes the POST test", "upc": "54321"},
		"id": "3000001", "links": {"self": "http://marveldb.net/api/comics/3000001"},
		"relationships": {"characters": {"data": [], "links": {"related": "/api/comics/3000001/characters", "self": "/api/comics/3000000/relationships/characters"}},
		"creators": {"data": [], "links": {"related": "/api/comics/3000001/creators", "self": "/api/comics/3000001/relationships/creators"}},
		"events": {"data": [], "links": {"related": "/api/comics/3000001/events", "self": "/api/comics/3000001/relationships/events"}},
		"series": {"data": [], "links": {"related": "/api/comics/3000001/series", "self": "/api/comics/3000001/relationships/series"}}},
		"type": "comics" }, "jsonapi": {"version": "1.0"}, "links": {"self": "/api/comics"}, "meta": {}}

	
		postreq = requests.post("http://marveldb.net/api/comics", simplejson.dumps(data),  headers=headers)
		self.assertEqual(201, postreq.status_code) 
		
		data = {"type": "comics", "id":"3000001", "attributes": {"id": "3000001", "issue_num": "31", "desc" : "gump", "img" : "shellfish company", "num_characters": "7", "num_creators": "7", "num_events": "7"}}

		patchreq = requests.patch("http://marveldb.net/api/comics/3000001", simplejson.dumps({"data": data}), headers=headers)
		self.assertEqual(204, patchreq.status_code)

		deletereq = requests.delete("http://marveldb.net/api/comics/3000001", headers=headers)
		self.assertEqual(204, deletereq.status_code)


    def test_creator_HTTP_requests(self):


	with app.app_context():
		headers = {"Content-Type": "application/vnd.api+json", "Accept": "application/vnd.api+json"}
	 	
		data = {"data": {"attributes": {"full_name": "new creator", "img": "hulk pic", "num_comics": 5, "num_events": 1, "num_series": 2},
		"id": "3000002", "links": {"self": "http://marveldb.net/api/creators/3000002"},
		"relationships": {"comics": {"data": [], "links": {"related": "/api/creators/3000002/characters", "self": "/api/creators/3000002/relationships/comics"}},
		"events": {"data": [], "links": {"related": "/api/creators/3000002/events", "self": "/api/creators/3000002/relationships/events"}},
		"series": {"data": [], "links": {"related": "/api/creators/3000002/series", "self": "/api/creators/3000002/relationships/series"}}},
		"type": "creators" }, "jsonapi": {"version": "1.0"}, "links": {"self": "/api/creators"}, "meta": {}}

		postreq = requests.post("http://marveldb.net/api/creators", simplejson.dumps(data),  headers=headers)
		self.assertEqual(201, postreq.status_code) 
		
		data = {"type": "creators", "id":"3000002", "attributes": {"id": "3000002", "full_name": "edmond", "img" : "shellfish company", "num_comics": "4", "num_events": "7", "num_series": "7"}}

		patchreq = requests.patch("http://marveldb.net/api/creators/3000002", simplejson.dumps({"data": data}), headers=headers)
		self.assertEqual(204, patchreq.status_code)

		deletereq = requests.delete("http://marveldb.net/api/creators/3000002", headers=headers)
		self.assertEqual(204, deletereq.status_code)


    def test_events_HTTP_requests(self):


	with app.app_context():
		headers = {"Content-Type": "application/vnd.api+json", "Accept": "application/vnd.api+json"}
	 	
		data = {"data": {"attributes": {"desc": "new event bro", "img": "world war 3 pic", "num_characters": 4, "num_comics": 5, "num_creators": 1, "num_series": 2, "title": "world war 3"},
		"id": "3000003", "links": {"self": "http://marveldb.net/api/events/3000003"},
		"relationships": {"characters": {"data": [], "links": {"related": "/api/events/3000003/characters", "self": "/api/events/3000003/relationships/characters"}},
		"comics": {"data": [], "links": {"related": "/api/events/3000003/comics", "self": "/api/events/3000003/relationships/comics"}},
		"creators": {"data": [], "links": {"related": "/api/events/3000003/creators", "self": "/api/events/3000003/relationships/creators"}},
		"series": {"data": [], "links": {"related": "/api/events/3000003/series", "self": "/api/events/3000003/relationships/series"}}},
		"type": "events" }, "jsonapi": {"version": "1.0"}, "links": {"self": "/api/events"}, "meta": {}}

		postreq = requests.post("http://marveldb.net/api/events", simplejson.dumps(data),  headers=headers)
		self.assertEqual(201, postreq.status_code) 
		
		data = {"type": "events", "id":"3000003", "attributes": {"id": "3000003", "desc": "world war 3", "img" : "north korea", "num_characters": "88888", "num_comics": "334", "num_creators": "52", "num_series": "7"}}

		patchreq = requests.patch("http://marveldb.net/api/events/3000003", simplejson.dumps({"data": data}), headers=headers)
		self.assertEqual(204, patchreq.status_code)

		deletereq = requests.delete("http://marveldb.net/api/events/3000003", headers=headers)
		self.assertEqual(204, deletereq.status_code)


    def test_series_HTTP_requests(self):


	with app.app_context():
		headers = {"Content-Type": "application/vnd.api+json", "Accept": "application/vnd.api+json"}
	 	
		data = {"data": {"attributes": {"desc": "testing series", "end": 2017, "img": "spidey series pic", "num_characters": 3, "num_comics": 50, "num_creators": 1, "num_events": 7, "start": 2017, "title": "spidey test man passes the POST test for series"},
		"id": "3000004", "links": {"self": "http://marveldb.net/api/series/3000004"},
		"relationships": {"characters": {"data": [], "links": {"related": "/api/series/3000004/characters", "self": "/api/series/3000000/relationships/characters"}},
		"comics": {"data": [], "links": {"related": "/api/series/3000004/comics", "self": "/api/series/3000004/relationships/comics"}},
		"creators": {"data": [], "links": {"related": "/api/series/3000004/creators", "self": "/api/series/3000004/relationships/creators"}},
		"events": {"data": [], "links": {"related": "/api/series/3000004/events", "self": "/api/series/3000004/relationships/events"}}},
		"type": "series" }, "jsonapi": {"version": "1.0"}, "links": {"self": "/api/series"}, "meta": {}}

		postreq = requests.post("http://marveldb.net/api/series", simplejson.dumps(data),  headers=headers)
		self.assertEqual(201, postreq.status_code) 
		
		data = {"type": "series", "id":"3000004", "attributes": {"id": "3000004", "desc": "world war 3 vol. 4", "img" : "hulk pic", "num_characters": "81", "num_comics": "4", "num_creators": "52", "num_events": "4"}}

		patchreq = requests.patch("http://marveldb.net/api/series/3000004", simplejson.dumps({"data": data}), headers=headers)
		self.assertEqual(204, patchreq.status_code)

		deletereq = requests.delete("http://marveldb.net/api/series/3000004", headers=headers)
		self.assertEqual(204, deletereq.status_code)





if __name__ == "__main__":
    main()
