from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from src.api.web.controllers.health_controller import health_bp
from src.api.web.controllers.password_controller import password_bp
from src.api.web.exceptions.error_handler import register_error_handlers
from src.api.web.config.swagger_config import SWAGGER_CONFIG, SWAGGER_TEMPLATE


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)
    Swagger(app, config=SWAGGER_CONFIG, template=SWAGGER_TEMPLATE)
    app.register_blueprint(health_bp)
    app.register_blueprint(password_bp)
    register_error_handlers(app)
    
    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
