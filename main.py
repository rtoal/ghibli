import os
import json
import webapp2
import jinja2
from urllib import urlencode
from google.appengine.api import urlfetch

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render())

class SearchHandler(webapp2.RequestHandler):
    def post(self):
        base_url = 'http://ghibli.herokuapp.com/films' # JUST FOR NOW
        # params = {
        #     'q': self.request.get('query'),
        #     'i': self.request.get('ingredients')}
        # response = json.loads(urlfetch.fetch(base_url + urlencode(params)).content)
        template = jinja_env.get_template('templates/results.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/search', SearchHandler),
], debug=True)
