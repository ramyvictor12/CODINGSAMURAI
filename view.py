from flask import Blueprint ,render_template

views = Blueprint('view',__name__)
@views.route('/')
def HomePage():
    return render_template("Home.html")
