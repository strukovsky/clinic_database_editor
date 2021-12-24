from flask import (
    Blueprint,
    make_response,
    render_template,
    request
)
from . import db_special_query
special_query_blueprint = Blueprint('special_query', __name__, url_prefix='/special_query')

@special_query_blueprint.route('/')
def index():
    return make_response(render_template('special_query/Index.html'))

@special_query_blueprint.route('clinics_with_doctors/')
def clinics_with_doctors():
    clinics = db_special_query.get_clinics_with_doctors()
    return make_response(render_template('special_query/ClinicsWithDoctors.html', clinics=clinics))

@special_query_blueprint.route('doctors_of_patient/', methods=['GET', 'POST'])
def doctors_of_patient():
    if request.method == 'GET':
        return make_response(render_template('special_query/DoctorsOfPatient.html'))
    elif request.method == 'POST':
        if (patient_id:= request.form.get('patient_id')):
            doctors = db_special_query.get_doctors_of_patient(patient_id=patient_id)
            return make_response(render_template('special_query/ResponseDoctorsOfPatient.html', doctors=doctors, patient_id=patient_id))