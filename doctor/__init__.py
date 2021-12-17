from flask import (
    Blueprint,
    make_response,
    render_template,
    redirect,
    request
)
from clinic import db_clinic
from models import Doctor
from . import db_doctor
doctor_blueprint = Blueprint("doctor", __name__, url_prefix="/doctor")


@doctor_blueprint.route("/")
def index():
    if request.method == 'GET':
        if id_to_remove := request.args.get("id_to_remove"):
            db_doctor.remove_doctor(id_to_remove)
        doctors = db_doctor.get_all_doctors()
        return make_response(render_template("/doctor/Index.html", doctors=doctors))


@doctor_blueprint.route("/add/", methods=['GET', 'POST'])
def add_doctor():
    if request.method == "GET":
        clinics = db_clinic.get_all_clinics()
        return make_response(render_template("/doctor/Add.html", clinics=clinics))
    if request.method == "POST":
        doctor_data = request.form.to_dict()
        doctor_data['id'] = -1
        doctor_data['address'] = "no address"
        doctor = Doctor(**doctor_data)
        db_doctor.add_doctor(doctor=doctor)
        return redirect("/doctor")

@doctor_blueprint.route("/edit/", methods=['GET', 'POST'])
def edit_doctor():
    if request.method == 'GET':
        if doctor_id := request.args.get("id_to_edit"):
            doctor = db_doctor.get_doctor(id=doctor_id)
            clinics = db_clinic.get_all_clinics()
            selected_clinic = {}
            for clinic in clinics:
                if clinic.address == doctor.address:
                    selected_clinic = clinic
                    clinics.remove(clinic)
            return make_response(render_template("/doctor/Edit.html", doctor=doctor, clinics=clinics, selected_clinic=selected_clinic))
        else:
            return redirect("/doctor")
    elif request.method == 'POST':
        doctor_data = request.form.to_dict()
        doctor_data["id"]=-1
        doctor_data["address"]="no address"
        db_doctor.update_doctor(doctor=Doctor(**doctor_data))
        return redirect("/doctor")
