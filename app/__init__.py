from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    ma.init_app(app)

    #  ALLOW LOCAL DEV 
    CORS(
        app,
        origins=[
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            # add your live frontend here later if needed
            # "https://your-frontend.onrender.com"
        ],
        supports_credentials=True
    )

    from .routes import reservation_bp
    app.register_blueprint(reservation_bp)

    with app.app_context():
        db.create_all()

    return app
