import webapp2
from google.appengine.api import users
# [START import_ndb]
from google.appengine.ext import db
# [END import_ndb]

# [START greeting]
class Greeting(db.Model):
    """Models an individual Guestbook entry."""
    content = db.StringProperty(multiline=True)
# [END greeting]




class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Hello, World!')
	self.response.write("""<html><body>
	<a href="public/test.html">link text</a>
	
	<div id="fb-root"></div>
	<script>(function(d, s, id) {
	  var js, fjs = d.getElementsByTagName(s)[0];
	  if (d.getElementById(id)) return;
	  js = d.createElement(s); js.id = id;
	  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=254652194610781&version=v2.0";
	  fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));
	
	
	
	</script>
	<fb:login-button perms="email,user_checkins"  onlogin="window.location.replace('http://stackoverflow.com');">Login with Facebook</fb:login-button>

	""")
        self.query = Greeting.all()
	for self.greeting in self.query:
	    self.response.write('<p>%s</p>' % self.greeting.content)
     	self.response.write("""
     	<form method="post">
	<input type="textarea" name="post"></input>
	<input type="submit" ></input></form></body>
	
	
	
	</html>""")
	
    def post(self):
    	self.greeting = Greeting(content=self.request.get("post"))
    	self.greeting.put()
    	self.redirect('/')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
