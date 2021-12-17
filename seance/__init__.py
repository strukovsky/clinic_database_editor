from typing import Any
from dateutil import parser
from flask import (
    Blueprint,
    make_response,
    render_template,
    redirect,
    request
)
from doctor import db_doctor
import doctor
from patient import db_patient
from diagnosis import db_diagnosis
import patient
from procedure import db_procedure

from datetime import date
from datetime import time
from models import Seance
import procedure
from . import db_seance
seance_blueprint = Blueprint("seance", __name__, url_prefix="/seance")


@seance_blueprint.route("/")
def index():
    if request.method == 'GET':
        if id_to_remove := request.args.get("id_to_remove"):
            db_seance.remove_seance(id_to_remove)
        seances = db_seance.get_all_seances()
        return make_response(render_template("/seance/Index.html", seances=seances))


@seance_blueprint.route("/add/", methods=['GET', 'POST'])
def add_seance():
    if request.method == "GET":
        doctors = db_doctor.get_all_doctors()
        patients = db_patient.get_all_patients()
        diagnosises = db_diagnosis.get_all_diagnosiss()
        procedures = db_procedure.get_all_procedures()
        return make_response(render_template("/seance/Add.html",
                                             doctors=doctors, patients=patients, diagnosises=diagnosises, procedures=procedures))
    if request.method == "POST":
        seance_data = request.form.to_dict()
        seance_data['seance_datatime'] = parser.parse(
            f"{seance_data['seance_date']} {seance_data['seance_time']}")
        seance_data['id'] = -1
        seance_data["doctor"] = "no data"
        seance_data["patient"] = "no data"
        seance_data["procedure"] = "no data"
        seance_data["diagnosis"] = "no data"
        seance = Seance(**seance_data)
        db_seance.add_seance(seance=seance)
        return redirect("/seance")


def remove_selected_from_list(array: list[Any], value_to_compare: Any, field_to_compare: str) -> list[Any]:
    selected: Any = None
    for item in array:
        field_value_in_item = getattr(item, field_to_compare)
        if field_value_in_item == value_to_compare:
            selected = item
            array.remove(item)
    return selected


@seance_blueprint.route("/edit/", methods=['GET', 'POST'])
def edit_seance():
    if request.method == 'GET':
        if seance_id := request.args.get("id_to_edit"):
            seance = db_seance.get_seance(id=seance_id)
            seance_datetime = seance.seance_datatime
            seance_date = seance_datetime.date()
            seance_time = seance_datetime.time()
            doctors = db_doctor.get_all_doctors()
            patients = db_patient.get_all_patients()
            diagnosises = db_diagnosis.get_all_diagnosiss()
            procedures = db_procedure.get_all_procedures()
            selected_doctor = remove_selected_from_list(
                doctors, seance.doctor, 'surname')
            selected_patient = remove_selected_from_list(
                patients, seance.patient, 'surname')
            selected_diagnosis = remove_selected_from_list(
                diagnosises, seance.diagnosis, 'description')
            selected_procedure = remove_selected_from_list(
                procedures, seance.procedure, 'name')

            return make_response(render_template("/seance/Edit.html",
                                                 seance_date=seance_date, seance_time=seance_time,
                                                 seance=seance, doctors=doctors, patients=patients,
                                                 diagnosises=diagnosises, procedures=procedures,
                                                 selected_doctor=selected_doctor, selected_patient=selected_patient,
                                                 selected_diagnosis=selected_diagnosis, selected_procedure=selected_procedure
                                                 ))
        else:
            return redirect("/seance")
    elif request.method == 'POST':
        seance_data = request.form.to_dict()
        seance_data["id"] = -1
        seance_data["doctor"] = "no data"
        seance_data["patient"] = "no data"
        seance_data["procedure"] = "no data"
        seance_data["diagnosis"] = "no data"
        seance_data["seance_datatime"] = parser.parse(
            f"{seance_data['seance_date']} {seance_data['seance_time']}")
        db_seance.update_seance(seance=Seance(**seance_data))
        return redirect("/seance")
