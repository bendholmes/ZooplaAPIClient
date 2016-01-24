import urlparse
import os.path


def getURLFileName(url):
	return os.path.basename(urlparse.urlsplit(url).path)

def getResource(path):
	return os.path.join(os.path.dirname(__file__), path)
