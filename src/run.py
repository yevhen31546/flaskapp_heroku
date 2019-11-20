from src.app import app

__author__ = 'jpk'

app.run(debug=app.config['DEBUG'], port=4990)
