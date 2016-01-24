from zoopla.zoopla import DB


class Property(DB.Model):
	__tablename__ = 'property'

	id = DB.Column(DB.BigInteger, primary_key=True, autoincrement=False)
	name = DB.Column(DB.String(50), index=True)
	bedroom_count = DB.Column(DB.Integer)
	property_type = DB.Column(DB.String(50), index=True)
	description = DB.Column(DB.Text)

	@property
	def name(self):
		propertyType = self.property_type if self.property_type else "property"

		if self.bedroom_count:
			return "{bedroomCount} bed {propertyType}".format(bedroomCount=self.bedroom_count, propertyType=propertyType)
		return propertyType.title()

	def __repr__(self):
		return '<Property {id}>'.format(id=self.id)
