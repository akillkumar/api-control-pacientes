from flask import Flask
from config import config
from models.model import *
from utils.schema_pacientes import *
from routes.medicos import medicos_blueprint
from routes.pacientes import pacientes_blueprint
from routes.consultas import consultas_blueprint
from routes.examen_fisico.examen_fisico import examen_fisico_blueprint
from routes.examen_fisico.cuello import cuello_blueprint
from routes.examen_fisico.abdomen import abdomen_blueprint
from routes.examen_fisico.respiratorio import respiratorio_blueprint
from routes.examen_fisico.cardiovascular import cardiovascular_blueprint
from routes.examen_fisico.piel_faneras_tejido_celular_subcutaneo import pftcs_blueprint
from routes.examen_fisico.neurologico import neurologico_blueprint
from routes.examen_fisico.sensibilida_profunda import sensibilidad_profunda_blueprint
from routes.examen_fisico.sensibilidad_superficial import sensibilidad_superficial_blueprint
from routes.examen_fisico.cabeza import cabeza_blueprint
from routes.antecedentes_personales.antecedentes_personales import antecedentes_personales_blueprint
from routes.antecedentes_personales.habitos_toxicos import habitos_toxicos_blueprint
from routes.antecedentes_personales.habitos_fisiologicos import habitos_fisiologicos_blueprint
from routes.enfermedades import enfermedades_blueprint
from routes.ginecologicos import ginecologicos_blueprint
from routes.usuarios_medicos import usuarios_medicos_blueprint
from routes.usuarios_pacientes import usuarios_pacientes_blueprint
from routes.solicitud_cita_pacientes import s_c_p_blueprint
from routes.citas_asignadas import citas_asignadas_blueprint
from routes.formula_medica import formula_medica_blueprint
from routes.medicamentos import medicamentos_blueprint
from routes.index import principal
from jwt_web import jwt
from flask_cors import CORS
from mail import mail


def create_app(enviroment):
    app = Flask(__name__)
    app.register_blueprint(medicos_blueprint)
    app.register_blueprint(pacientes_blueprint)
    app.register_blueprint(consultas_blueprint)
    app.register_blueprint(examen_fisico_blueprint)
    app.register_blueprint(cuello_blueprint)
    app.register_blueprint(abdomen_blueprint)
    app.register_blueprint(respiratorio_blueprint)
    app.register_blueprint(cardiovascular_blueprint)
    app.register_blueprint(pftcs_blueprint)
    app.register_blueprint(neurologico_blueprint)
    app.register_blueprint(sensibilidad_profunda_blueprint)
    app.register_blueprint(sensibilidad_superficial_blueprint)
    app.register_blueprint(cabeza_blueprint)
    app.register_blueprint(antecedentes_personales_blueprint)
    app.register_blueprint(habitos_toxicos_blueprint)
    app.register_blueprint(habitos_fisiologicos_blueprint)
    app.register_blueprint(enfermedades_blueprint)
    app.register_blueprint(ginecologicos_blueprint)
    app.register_blueprint(usuarios_medicos_blueprint)
    app.register_blueprint(usuarios_pacientes_blueprint)
    app.register_blueprint(s_c_p_blueprint)
    app.register_blueprint(citas_asignadas_blueprint)
    app.register_blueprint(formula_medica_blueprint)
    app.register_blueprint(medicamentos_blueprint)
    app.register_blueprint(principal)
    app.config.from_object(enviroment)
    app.config['JWT_SECRET_KEY'] = 'secretpooo'
    # Configuración del email
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'jesusjoelgonzalezcastro@gmail.com'
    app.config['MAIL_PASSWORD'] = 'lxrbqtjwoupkqtnu'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    CORS(app)

    

    with app.app_context():
        db.init_app(app)
        db.create_all()
        ma.init_app(app)
        jwt.init_app(app)
        mail.init_app(app)
        

        
    return app

enviroment = config['development']
app = create_app(enviroment)








def pagina_no_encontrada(error):
    return '<h1>La Página Que Intentas Buscar, No Existe</h1>'


if __name__=='__main__':
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(host='0.0.0.0', port=5000, debug=True)
