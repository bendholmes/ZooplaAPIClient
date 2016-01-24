DB = None

class Zoopla(object):
	def __init__(self):
		from api import listings
		self.listings = listings.Listings()
