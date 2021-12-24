from flask import (Blueprint, make_response, render_template, request)
from . import db_custom_query
from .db_custom_query import DatabaseResponse
custom_query_blueprint = Blueprint('custom_query', __name__, url_prefix='/custom_query')


@custom_query_blueprint.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return make_response(render_template('custom_query/Index.html'))
    elif request.method == 'POST':
        if (query := request.form.get('query')):
            db_response: DatabaseResponse = db_custom_query.perform_query(query=query)
            if db_response.isOk():
                return render_template('custom_query/Response.html',
                                       data=db_response.data, query=query)
            else:
                return render_template('custom_query/Error.html', error=db_response.error, query=query)
