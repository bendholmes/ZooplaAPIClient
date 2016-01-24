from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

from zoopla import zoopla

# Create our Flask web server
APP = Flask(__name__)

# Load the config
APP.config.from_object('config')

# Create a DB handle from the app
DB = SQLAlchemy(APP)

# Create a Zoopla handle from the DB
zoopla.DB = DB
Z = zoopla.Zoopla()

# Create an index page
@APP.route('/')
def index():
    # Get the listing
    listing = Z.listings.getListing("SK17")

    if listing:
        print listing
        return render_template('index.html', listing=listing)

if __name__ == '__main__':
    APP.run(debug=True)
