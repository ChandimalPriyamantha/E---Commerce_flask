import bcrypt
from flask import Flask
from flask.helpers import _matching_loader_thinks_module_is_package
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_uploads import IMAGES,UploadSet, configure_uploads # pip install Flask-Reuploaded (flask-uploads is not working)
import os
from flask_msearch import Search
from flask_login import LoginManager
from flask_migrate import Migrate








basedir =os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SECRET_KEY']='hellochandimal'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir,'static/images')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
#patch_request_class(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)



migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u"Please login first"


from shope.admin import routes
from shope.products import routes
from shope.carts import carts
from shope.customers import routes

