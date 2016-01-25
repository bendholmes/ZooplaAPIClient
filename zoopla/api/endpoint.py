import abc
import json
import requests

from zoopla import constants
from zoopla import utils



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
