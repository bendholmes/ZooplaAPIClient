from flask.ext.sqlalchemy import SQLAlchemy


# Create a DB handle from the app
DB = SQLAlchemy()

from service.listing_service import ListingService
LISTING_SERVICE = ListingService()
