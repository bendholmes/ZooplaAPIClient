import abc
import json
import requests

from sqlalchemy.exc import OperationalError

from zoopla import constants
from zoopla import utils
from zoopla.zoopla import DB


class Endpoint(object):
	__metaclass__ = abc.ABCMeta

	PATH = ""

	@property
	def _base_params(self):
		return {
			"api_key": constants.API_KEY
		}

	@property
	def url(self):
		return "{base}{path}.json".format(base=constants.BASE_URL, path=self.PATH)

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

	def _map(self, objectType, data, map, idField='id'):
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

	def map(self, objectType, data, map=None, idField=None):
		if not map:
			map = {}

		if isinstance(data, list):
			objs = []
			for objData in data:
				objs.append(self._map(objectType, objData, map, idField=idField))
			return objs
		return self._map(objectType, data, map, idField=idField)

	def get_params_from_locals(self, locals):
		return locals.update(locals.pop('kwargs'))

	def get_test_data(self, url):
		return json.load(open(utils.getResource('data/{fileName}'.format(fileName=utils.getURLFileName(url))), 'r'))

	def get(self, url=None, params=None):
		if not url:
			url = self.url

		if not params:
			params = {}

		if constants.TEST_DATA:
			return self.get_test_data(url)
		else:
			# TODO: Handle non-success API responses here
			return json.loads(requests.get(url, params=self._base_params.update(params)).text)
