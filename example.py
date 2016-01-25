from flask import render_template

from zoopla.factory import create_app
from zoopla import zoopla as Z

APP = create_app()

# Create an index page
@APP.route('/')
def index():
    # Get the listing
    listing = Z.LISTING_SERVICE.getListing("SK17")

    if listing:
        print listing
        return render_template('index.html', listing=listing)

if __name__ == '__main__':
    APP.run(debug=True)
