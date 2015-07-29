import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('hello.html')
        self.response.out.write(template.render())

    def post(self):
        name = self.request.get('name')
        template = jinja_environment.get_template('hello.html')
        self.response.out.write(template.render({ "your_name": name }))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
