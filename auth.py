from flask import Blueprint

authentication = Blueprint('authentication', __name__)


# routes for login,logout,signup
@authentication.route('/login')
def Login():
    return "<p>login</p>"


@authentication.route('/logout')
def Logout():
    return "<p>logout</p>"


@authentication.route('/sign_up')
def SignUp():
    return "<p>signup</p>"
