from .endpoint import Endpoint


class Listings(Endpoint):
	PATH = "property_listings"

	def getListing(self, area, page_number=1, page_size=100, **kwargs):
		return self.get(self.get_params_from_locals(locals()))
