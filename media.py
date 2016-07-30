import webbrowser

class movie(object):
	# Class attributes in strings
	# title: movie title
	# description: movie's rotten tomatoes critics consensus
	# trailer_url: url to a youtube video of the movie's trailer
	# fresh_rating: % fresh rating from Rotten Tomatoes
	# rotten_tomatoes_url: url to movie's Rotten Tomatoes page
	# poster_image: link to image of movie poster
	
	def __init__(self, title, description, trailer_url, fresh_rating, rotten_tomatoes_url, poster_image):
		super(movie, self).__init__()
		self.title = title
		self.description = description
		self.trailer_url = trailer_url
		self.fresh_rating = fresh_rating
		self.rotten_tomatoes_url = rotten_tomatoes_url
		self.poster_image = poster_image
	def view_trailer(self):
	# Open the trailer url in a new browser tab
		webbrowser.Open(self.trailer_url)
	# Open the rotten tomatoes url in a new browser tab
		webbrowser.Open(self.rotten_tomatoes_url)