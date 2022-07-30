from flask import Flask

import logger
from main_page.views import main_blueprint
from api.views import api_blueprint

app = Flask(__name__)

app.config.from_pyfile("config.py")
logger.create_logger()

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(port=3110)
