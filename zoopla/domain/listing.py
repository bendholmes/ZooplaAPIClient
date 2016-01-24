from sqlalchemy.orm import relationship

from zoopla.zoopla import DB
from .listing_properties import listing_properties_association_table


class Listing(DB.Model):
	__tablename__ = 'listing'

	id = DB.Column(DB.BigInteger, primary_key=True, autoincrement=True)
	country = DB.Column(DB.String(50), index=True)
	area_name = DB.Column(DB.String(50), index=True)
	street = DB.Column(DB.String(255))
	town = DB.Column(DB.String(50), index=True)
	county = DB.Column(DB.String(50), index=True)
	latitude = DB.Column(DB.Float)
	longitude = DB.Column(DB.Float)
	result_count = DB.Column(DB.Integer)

	properties = relationship("Property", secondary=listing_properties_association_table)


	def __repr__(self):
		return '<Listing {id} [Properties ({propertyCount}): {properties}>'.format(
			id=self.id,
			propertyCount=len(self.properties),
			properties=self.properties
		)
