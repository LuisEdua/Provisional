from flask import Flask
from routes import Area
from routes import Floor
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(Area.DataRoutes, url_prefix='/api')
app.register_blueprint(Floor.DataRoutes, url_prefix='/api')
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
