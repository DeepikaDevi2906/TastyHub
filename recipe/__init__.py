from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from badge import badges_bp
from badge.icons import BADGE_ICONS
app = Flask(__name__)
app.register_blueprint(badges_bp)
migrate=Migrate()
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message = ""

@app.context_processor
def inject_badge_icons():
    return dict(badge_icons=BADGE_ICONS)

from recipe.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from recipe import routes
