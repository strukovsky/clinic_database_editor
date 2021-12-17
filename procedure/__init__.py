from flask import (
    Blueprint,
    make_response,
    render_template,
    redirect,
    request
)
from clinic import db_clinic
from models import Procedure
from . import db_procedure
procedure_blueprint = Blueprint("procedure", __name__, url_prefix="/procedure")


@procedure_blueprint.route("/")
def index():
    if request.method == 'GET':
        if id_to_remove := request.args.get("id_to_remove"):
            db_procedure.remove_procedure(id_to_remove)
        procedures = db_procedure.get_all_procedures()
        return make_response(render_template("/procedure/Index.html", procedures=procedures))


@procedure_blueprint.route("/add/", methods=['GET', 'POST'])
def add_procedure():
    if request.method == "GET":
        clinics = db_clinic.get_all_clinics()
        return make_response(render_template("/procedure/Add.html", clinics=clinics))
    if request.method == "POST":
        procedure_data = request.form.to_dict()
        procedure_data['id'] = -1
        procedure = Procedure(**procedure_data)
        db_procedure.add_procedure(procedure=procedure)
        return redirect("/procedure")

@procedure_blueprint.route("/edit/", methods=['GET', 'POST'])
def edit_procedure():
    if request.method == 'GET':
        if procedure_id := request.args.get("id_to_edit"):
            procedure = db_procedure.get_procedure(id=procedure_id)
            return make_response(render_template("/procedure/Edit.html", procedure=procedure))
        else:
            return redirect("/procedure")
    elif request.method == 'POST':
        procedure_data = request.form.to_dict()
        procedure_data["id"]=-1
        db_procedure.update_procedure(procedure=Procedure(**procedure_data))
        return redirect("/procedure")
