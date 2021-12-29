from flask import Blueprint, render_template

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth = Blueprint("auth", __name__, url_prefix="/auth")


# Set the route and accepted methods
@auth.route("/signin/", methods=["GET", "POST"])
def signin():
    return render_template("auth/signin.html")


@auth.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
