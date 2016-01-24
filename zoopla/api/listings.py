from .endpoint import Endpoint
from zoopla.domain.listing import Listing
from zoopla.domain.property import Property
from zoopla.zoopla import DB

class Listings(Endpoint):
	PATH = "property_listings"

	property_field_map = {
		"listing_id": "id",
		"num_bedrooms": "bedroom_count"
	}

	property_id_field = "listing_id"

	def getListing(self, area, page_number=1, page_size=100, **kwargs):
		raw_listing = self.get(self.get_params_from_locals(locals()))
		raw_properties = raw_listing.pop('listing')

		listing = self.map(Listing, raw_listing)
		properties = self.map(Property, raw_properties, map=self.property_field_map, idField=self.property_id_field)

		for property in properties:
			listing.properties.append(property)

		DB.session.commit()

		return listing
