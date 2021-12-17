from flask import (
    Flask,
    make_response,
    render_template,
    redirect,
    request,
    Response,
    Blueprint
)

from models import Patient
from . import db_patient
patient_blueprint = Blueprint("patient", __name__, url_prefix="/patient")

@patient_blueprint.route("/")
def index():
    if id_to_remove := request.args.get("id_to_remove"):
        db_patient.remove_patient(id_to_remove)
    patients = db_patient.get_all_patients()
    return make_response(render_template("/patient/Index.html", patients=patients))


@patient_blueprint.route("/add/", methods=['GET', 'POST'])
def add() -> Response:
    if request.method == 'GET':
        return make_response(render_template("/patient/Add.html"))
    elif request.method == 'POST':
        patient = Patient(**request.form.to_dict())
        if (status := db_patient.add_patient(patient)) == "OK":
            return redirect("/patient/")
        else:
            return redirect(f"/error/{status}")
            
@patient_blueprint.route("/edit/", methods=['POST', 'GET'])
def edit() -> Response:
    if (id_to_edit := request.args.get("id_to_edit")) and request.method == 'GET':
        patient = db_patient.get_patient(patient_id=id_to_edit)
        return make_response(render_template("/patient/Edit.html", patient=patient))
    elif request.method == 'POST':
        patient = Patient(**request.form.to_dict())
        db_patient.edit_patient(patient=patient)
        return redirect("/patient/")