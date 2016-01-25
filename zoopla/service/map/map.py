from sqlalchemy.exc import OperationalError

from zoopla.zoopla import DB


class Map(object):
	def getExistingObject(self, objectType, id):
		try:
			with DB.session.no_autoflush:
				return objectType.query.filter_by(id=id).first()
		except OperationalError, oe:
			print "Error loading existing {objectType} with id {id}: {exception}".format(
				objectType=objectType,
				id=id,
				exception=oe
			)
		return None


	def _map_object(self, objectType, data, map, idField='id'):
		# If the data contains an id, check it doesn't already exist
		if idField in data:
			maybeExistingObject = self.getExistingObject(objectType, data[idField])
			if maybeExistingObject:
				return maybeExistingObject

		obj = objectType()
		for key, value in data.iteritems():
			key = map.get(key, key)

			if hasattr(obj, key):
				setattr(obj, key, value)
			else:
				# TODO: Store in HSTORE
				pass

		DB.session.add(obj)
		return obj


	def map_object(self, objectType, data, map=None, idField=None):
		if not map:
			map = {}

		if isinstance(data, list):
			objs = []
			for objData in data:
				objs.append(self._map_object(objectType, objData, map, idField=idField))
			return objs
		return self._map_object(objectType, data, map, idField=idField)
