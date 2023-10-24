from flask import Flask


def create():
    from view import views
    from auth import authentication

    app = Flask(__name__)
    # encrypt cookies and session
    app.config['SECRET_KEY'] = ':$3f"Opn*/{s4m]'
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(authentication, url_prefix='/')

    return app
