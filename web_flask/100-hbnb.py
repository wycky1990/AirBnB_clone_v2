<<<<<<< HEAD
"""Script starts a Flask web application"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    """Render template with states
    """
    path = '100-hbnb.html'
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template(path, states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
=======
#!/usr/bin/python3
"""
Starts a Flask web application.
Listens on 0.0.0.0  on port 5000.
Routes:
  *  /hbnb: Display the HTML page for hbnb home page.
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display the HTML page for hbnb home page."""
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    states = storage.all("State")
    return render_template("100-hbnb.html",
                           amenities=amenities,
                           places=places,
                           states=states)


@app.teardown_appcontext
def teardown(excpt=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 582bbe91fbb3aea99cf3e75ecf858c3a133e1361
