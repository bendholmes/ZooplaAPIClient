from zoopla.api.listings import Listings
from .service import Service
from map.listing_map import ListingMap


class ListingService(Service):
	def __init__(self):
		"""
		Is this the best place for these or should it be in an api.py module in zoopla/api/ and map.py module in zoopla/map/?
		"""
		self.listingsAPI = Listings()
		self.map = ListingMap()

	def getListing(self, *args, **kwargs):
		"""
		TODO: How to maintain API interface without duplication?
		"""
		return self.map.map(self.listingsAPI.getListing(*args, **kwargs))
