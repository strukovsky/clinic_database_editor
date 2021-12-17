from flask import (
    Flask,
    make_response,
    render_template, 
    Response
)
from clinic import clinic_blueprint
from doctor import doctor_blueprint
from patient import patient_blueprint
from procedure import procedure_blueprint
from diagnosis import diagnosis_blueprint
from seance import seance_blueprint
from os.path import exists
from db_config import setup_scheme, populate_database, get_db
from error import error_blueprint

app = Flask(__name__)
app.register_blueprint(clinic_blueprint)
app.register_blueprint(doctor_blueprint)
app.register_blueprint(patient_blueprint)
app.register_blueprint(procedure_blueprint)
app.register_blueprint(diagnosis_blueprint)
app.register_blueprint(seance_blueprint)
app.register_blueprint(error_blueprint)

@app.before_first_request
def setup_db():
    if not exists('db/database.db'):
        setup_scheme(get_db())
        populate_database(get_db())

@app.route("/")
def index() -> Response:
    return make_response(render_template("Index.html"))

if __name__ == "__main__":
    app.run()