from flask import Flask 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

# from app import routes, models
from app.blueprint.main import bp as main_bp
from app.blueprint.blog import bp as blog_bp
from app.blueprint.auth import bp as auth_bp
app.register_blueprint(main_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(auth_bp)




