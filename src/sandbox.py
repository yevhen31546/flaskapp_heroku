from flask import Flask, render_template
from src.common.database import Database
from src.models.items.views import item_blueprint
from src.models.alerts.views import alert_blueprint

app = Flask(__name__)

@app.route('/')
app.register_blueprint(item_blueprint, url_prefix='/items')
app.register_blueprint(alert_blueprint, url_prefix='/alerts')

if __name__ == '__main__':
    app.run(debug=True)