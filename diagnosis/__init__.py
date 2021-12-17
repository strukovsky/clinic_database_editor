from flask import (
    Blueprint,
    make_response,
    render_template,
    redirect,
    request
)
from dateutil import parser
from models import Diagnosis
from . import db_diagnosis
diagnosis_blueprint = Blueprint("diagnosis", __name__, url_prefix="/diagnosis")


@diagnosis_blueprint.route("/")
def index():
    if request.method == 'GET':
        if id_to_remove := request.args.get("id_to_remove"):
            db_diagnosis.remove_diagnosis(id_to_remove)
        diagnosiss = db_diagnosis.get_all_diagnosiss()
        return make_response(render_template("/diagnosis/Index.html", diagnosises=diagnosiss))


@diagnosis_blueprint.route("/add/", methods=['GET', 'POST'])
def add_diagnosis():
    if request.method == "GET":
        return make_response(render_template("/diagnosis/Add.html"))
    if request.method == "POST":
        diagnosis_data = request.form.to_dict()
        diagnosis_data['id'] = -1
        diagnosis = Diagnosis(**diagnosis_data)
        db_diagnosis.add_diagnosis(diagnosis=diagnosis)
        return redirect("/diagnosis")

@diagnosis_blueprint.route("/edit/", methods=['GET', 'POST'])
def edit_diagnosis():
    if request.method == 'GET':
        if diagnosis_id := request.args.get("id_to_edit"):
            diagnosis = db_diagnosis.get_diagnosis(id=diagnosis_id)
            return make_response(render_template("/diagnosis/Edit.html", diagnosis=diagnosis))
        else:
            return redirect("/diagnosis")
    elif request.method == 'POST':
        diagnosis_data = request.form.to_dict()
        diagnosis_data["id"]=-1
        db_diagnosis.update_diagnosis(diagnosis=Diagnosis(**diagnosis_data))
        return redirect("/diagnosis")
