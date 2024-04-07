from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
from .views import views
from .auth import auth
from .models import User, Post, Comment, Like

def create_database(app):
        if not path.exists("website/" + DB_NAME):
            with app.app_context():
                db.create_all()
            print("Created Database!")
            
db = SQLAlchemy()
DB_NAME = "database.db"
app = Flask(__name__)
app.config["SECRET_KEY"] = "MadhavKhandelwal"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

app.register_blueprint(views, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")



create_database(app)

login_manager = LoginManager()   # uses a session
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id)) # query from the user model for the user object with the given id
    # session is a temporary storage , generally for 30 days, it is stored. Then , that session data is dumped

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    
    

    


