import webbrowser

class movie(object):
	# Class attributes in strings
	# title: movie title
	# tagline: movie's original tagline
	# trailer_url: url to a youtube video of the movie's trailer
	
	def __init__(self, title, tagline, trailer_url):
		super(movie, self).__init__()
		self.title = title
		self.tagline = tagline
		self.trailer_url = trailer_url
	def view_trailer(self):
	# Open the trailer url in a new browser tab
		webbrowser.Open(self.trailer_url)