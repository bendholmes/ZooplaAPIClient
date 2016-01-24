from sqlalchemy import Table, Column, Integer, ForeignKey

from zoopla.zoopla import DB


listing_properties_association_table = Table(
	'listing_properties_association',
	DB.metadata,
    Column('listing_id', Integer, ForeignKey('listing.id')),
    Column('property_id', Integer, ForeignKey('property.id'))
)
