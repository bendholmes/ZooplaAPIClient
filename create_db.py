#!/usr/bin/env/python2.7

# Must import all DB models / tables
from example import DB
import zoopla.domain.listing_properties
from zoopla.domain.listing import Listing
from zoopla.domain.property import Property

# Create & commit them
DB.create_all()
DB.session.commit()
