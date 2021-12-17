from flask import (
    Blueprint,
    make_response,
    render_template,
    request
)

error_blueprint = Blueprint('error', __name__, url_prefix='/error')

@error_blueprint.route("/already_exists")
def already_exists():
    return make_response(render_template("error/AlreadyExists.html"))