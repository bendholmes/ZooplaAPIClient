from zoopla.domain.listing import Listing
from zoopla.domain.property import Property
from zoopla.zoopla import DB
from map import Map


class ListingMap(Map):
    property_field_map = {
        "listing_id": "id",
        "num_bedrooms": "bedroom_count"
    }

    property_id_field = "listing_id"

    def map(self, rawListing):
        rawProperties = rawListing.pop('listing')

        listing = self.map_object(Listing, rawListing)
        properties = self.map_object(Property, rawProperties, map=self.property_field_map, idField=self.property_id_field)

        for property in properties:
            listing.properties.append(property)

        DB.session.commit()
