from . import db_clinic
from flask import (
    Blueprint,
    make_response,
    render_template,
    request,
    redirect,
    Response
)

from models import Clinic

clinic_blueprint = Blueprint("clinic", __name__, url_prefix="/clinic")


@clinic_blueprint.route("/", methods=['POST', 'GET'])
def get_all() -> Response:
    id_to_remove = request.args.get('id_to_remove')
    if id_to_remove is not None:
        db_clinic.remove_clinic(id_to_remove)
    all_clinics = db_clinic.get_all_clinics()
    return make_response(render_template("/clinic/Index.html", clinics=all_clinics))


@clinic_blueprint.route("/add/", methods=['GET', 'POST'])
def add_clinic() -> Response:
    if request.method == 'POST':
        clinic_dict = request.form.to_dict()
        clinic_dict['id'] = -1
        clinic = Clinic(**clinic_dict)
        db_clinic.add_clinic(clinic)
        return redirect("/clinic")
    elif request.method == 'GET':
        return make_response(render_template("/clinic/Add.html"))


@clinic_blueprint.route("/edit/", methods=['GET', 'POST'])
def edit_clinic() -> Response:
    if request.method == "GET":
        if clinic_id := request.args.get("id_to_edit"):
            clinic = db_clinic.get_clinic(id=clinic_id)
            return make_response(render_template("/clinic/Edit.html",
                                               clinic=clinic))
        return redirect("/clinic/")
    elif request.method == "POST":
        clinic = Clinic(**{
            "id": request.form.get("id"),
            "address": request.form.get("address"),
            "speciality": request.form.get("speciality"),
            "clinic_type": request.form.get("clinic_type")
        })
        db_clinic.update_clinic(clinic)
        return redirect("/clinic/")
