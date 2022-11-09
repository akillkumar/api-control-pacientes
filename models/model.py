from datetime import datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null

db = SQLAlchemy()   

class Pacientes(db.Model):
    __tablename__="pacientes"

    id = db.Column(db.Integer,primary_key=True)
    identificacion = db.Column(db.Integer, unique=True)
    primer_nombre = db.Column(db.String(100))
    segundo_nombre = db.Column(db.String(100))
    primer_apellido = db.Column(db.String(100))
    segundo_apellido = db.Column(db.String(100))
    genero = db.Column(db.String(30))
    fecha_nacimiento = db.Column(db.Date)
    telefono = db.Column(db.String(15))
    correo = db.Column(db.String(100))
    ocupacion = db.Column(db.String(100))
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    usuarios = db.relationship('Usuarios', backref='pacientes', lazy=True)
    solicitud_cita_paciente = db.relationship('Solicitud_Cita_Pacientes', backref='pacientes', lazy=True)
    consultas = db.relationship('Consultas', backref='pacientes', lazy=True)
    citas_asignadas = db.relationship('Citas_Asignadas', backref='pacientes', lazy=True)
    formula_medica = db.relationship('Formula_Medica', backref='pacientes', lazy=True)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'),
        nullable=True)


    def __init__(self, identificacion,primer_nombre, segundo_nombre, primer_appellido, segundo_apellido,
    genero, fecha_nacimiento,telefono,correo,ocupacion,estado, medico_id):
        self.identificacion=identificacion
        self.primer_nombre=primer_nombre
        self.segundo_nombre=segundo_nombre
        self.primer_apellido=primer_appellido
        self.segundo_apellido=segundo_apellido
        self.genero=genero
        self.fecha_nacimiento=fecha_nacimiento
        self.telefono=telefono
        self.correo=correo
        self.ocupacion=ocupacion
        self.estado = estado
        self.medico_id=medico_id
        

class Usuarios(db.Model):
    __tablename__="usuarios"

    id=db.Column(db.Integer,primary_key=True, autoincrement=True)
    identificacion = db.Column(db.String(15),unique=True)
    password = db.Column(db.String(200))
    estado = db.Column(db.Boolean)
    tipo_usuario = db.Column(db.String(45))
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'),
        nullable=True)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'),
        nullable=True)
    
    def __init__(self,identificacion,password,estado):
        self.identificacion=identificacion
        self.password =password
        self.estado = estado
    
class UsuariosPacientes(Usuarios):
    def __init__(self,identificacion, password,estado,tipo_usuario,paciente_id):
        Usuarios.__init__(self,identificacion,password,estado)
        self.paciente_id=paciente_id
        self.tipo_usuario=tipo_usuario

class UsuariosMedicos(Usuarios):
    def __init__(self,identificacion, password,tipo_usuario,estado,medico_id):
        Usuarios.__init__(self,identificacion,password,estado)
        self.medico_id=medico_id
        self.tipo_usuario = tipo_usuario
        
        

class Medicos(db.Model):
    __tablename__="medicos"

    id = db.Column(db.Integer, primary_key=True)
    identificacion = db.Column(db.String(100),unique=True)
    primer_nombre = db.Column(db.String(100))
    segundo_nombre = db.Column(db.String(100))
    primer_apellido = db.Column(db.String(100))
    segundo_apellido = db.Column(db.String(100))
    especializacion = db.Column(db.String(100))
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    usuarios = db.relationship('Usuarios', backref='medicos', lazy=True)
    paciente = db.relationship('Pacientes', backref='medicos', lazy=True)
    
    

    def __init__(self, identificacion, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,
    especializacion,estado):
        self.identificacion = identificacion
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.especializacion = especializacion
        self.estado = estado

class Consultas(db.Model):
    __tablename__="consultas"

    id = db.Column(db.Integer,primary_key=True)
    motivo_consulta = db.Column(db.Text)
    enfermedad_actual = db.Column(db.Text)
    antecedentes_enfermedad_ac = db.Column(db.Text)
    antecedentes_familiares = db.Column(db.Text)
    fecha_consulta = db.Column(db.Date)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'),
        nullable=True)
    enfermedades = db.relationship('Enfermedades', backref='consultas', lazy=True)
    examen_fisico = db.relationship('Examen_Fisico', backref='consultas', lazy=True)
    antecedentes_personales = db.relationship('Antecedentes_Personales', backref='consultas',lazy=True)
    
    

    def __init__(self,motivo_consulta,enfermedad_actual,antecedentes_enfermedad_ac,
    antecedentes_familiares,fecha_consulta,estado, paciente_id):
        self.motivo_consulta=motivo_consulta
        self.enfermedad_actual = enfermedad_actual
        self.antecedentes_enfermedad_ac = antecedentes_enfermedad_ac
        self.antecedentes_familiares=antecedentes_familiares
        self.fecha_consulta=fecha_consulta
        self.estado=estado
        self.paciente_id=paciente_id
        
class Antecedentes_Personales(db.Model):
    __tablename__='antecedentes_personales'
    id= db.Column(db.Integer,primary_key=True)
    enfermedad_de_infancia = db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    consulta_id = db.Column(db.Integer, db.ForeignKey('consultas.id'), nullable=True)
    habitos_toxicos = db.relationship('Habitos_Toxicos',backref='antecedentes_personales', lazy=True)
    habitos_fisiologicos = db.relationship('Habitos_Fisiologicos',backref='antecedentes_personales', lazy=True)
     

    def __init__(self, enfermedad_de_infancia,estado,consulta_id):
        self.enfermedad_de_infancia=enfermedad_de_infancia
        self.estado = estado
        self.consulta_id=consulta_id
        

class Habitos_Toxicos(db.Model):
    __tablename__='habitos_toxicos'
    id = db.Column(db.Integer, primary_key=True)
    alcohol = db.Column(db.String(200))
    tabaco = db.Column(db.String(200))
    drogas = db.Column(db.String(200))
    infusiones = db.Column(db.String(200))
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    antecedentes_personales_id = db.Column(db.Integer, db.ForeignKey('antecedentes_personales.id'), nullable=True)
    

    def __init__(self, alcohol, tabaco, drogas, infusiones,estado,antecedentes_personales_id):
        self.alcohol=alcohol
        self.tabaco=tabaco
        self.drogas=drogas
        self.infusiones=infusiones
        self.estado = estado
        self.antecedentes_personales_id=antecedentes_personales_id

class Habitos_Fisiologicos(db.Model):
    __tablename__='habitos_fisiologicos'
    id = db.Column(db.Integer, primary_key=True)
    alimentacion = db.Column(db.Text)
    diuresis = db.Column(db.Text)
    catarsis = db.Column(db.Text)
    sueño = db.Column(db.Text)
    sexualidad = db.Column(db.Text)
    otros = db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    antecedentes_personales_id = db.Column(db.Integer, db.ForeignKey('antecedentes_personales.id'), nullable=True)

    def __init__(self,alimentacion,diuresis,catarsis,sueño,sexualidad,otros,estado, antecedentes_personales_id):
        self.alimentacion=alimentacion
        self.diuresis=diuresis
        self.catarsis = catarsis
        self.sueño=sueño
        self.sexualidad=sexualidad
        self.otros=otros
        self.estado = estado
        self.antecedentes_personales_id=antecedentes_personales_id



class Citas_Asignadas(db.Model):
    __tablename__="citas_asignadas"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'),
        nullable=True)
    solicitud_cita_paciente_id = db.Column(db.Integer, db.ForeignKey('solicitud_cita_pacientes.id'),
        nullable=True)
    

    def __init__(self,fecha,hora,estado,paciente_id,solicitud_cita_paciente_id):
        self.fecha=fecha
        self.hora=hora
        self.estado = estado
        self.paciente_id = paciente_id
        self.solicitud_cita_paciente_id=solicitud_cita_paciente_id

class Solicitud_Cita_Pacientes(db.Model):
    __tablename__="solicitud_cita_pacientes"
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    citas_asignadas = db.relationship('Citas_Asignadas', backref='solicitud_cita_pacientes', lazy=True)
    paciente_id = db.Column(db.Integer,db.ForeignKey('pacientes.id'), nullable=True)


    def __init__(self,estado,paciente_id):
        self.estado = estado
        self.paciente_id=paciente_id

class Formula_Medica(db.Model):
    __tablename__="formula_medica"

    id = db.Column(db.Integer, primary_key=True)
    preescribe = db.Column(db.String(100))
    recomendacion = db.Column(db.Text)
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    observaciones = db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    medicamentos = db.relationship('Medicamentos', backref='formula_medica', lazy=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'),
        nullable=True)

    def __init__(self,preescribe, recomendacion, fecha_inicio, fecha_fin,
    observaciones,estado,paciente_id):
        self.preescribe=preescribe
        self.recomendacion=recomendacion
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.observaciones=observaciones
        self.estado = estado
        self.paciente_id=paciente_id
        

class Medicamentos(db.Model):
    __tablename__="medicamentos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    cantidad = db.Column(db.Integer)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    formula_medica_id = db.Column(db.Integer, db.ForeignKey('formula_medica.id'),
        nullable=True)

    def __init__(self, nombre, cantidad,estado ,formula_medica_id):
        self.nombre = nombre
        self.cantidad = cantidad
        self.estado = estado
        self.formula_medica_id=formula_medica_id


class Enfermedades(db.Model):
    __tablename__ = "enfermedades"

    id = db.Column(db.Integer, primary_key=True)
    cv = db.Column(db.String(400))
    respiratorio = db.Column(db.String(400))
    nefrourologicos = db.Column(db.String(400))
    neurologicos = db.Column(db.Text)
    hematologicos = db.Column(db.String(400))
    infectologicos = db.Column(db.Text)
    endocrinologicos = db.Column(db.Text)
    quirurgicos = db.Column(db.Text)
    traumatologicos = db.Column(db.Text)
    alergicos = db.Column(db.Text)
    epidemiologicos = db.Column(db.Text)
    antecedentes_heredofamiliares = (db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    consulta_id = db.Column(db.Integer, db.ForeignKey('consultas.id'),nullable=True)
    ginecologicos = db.relationship('Ginecologicos', backref='enfermedades', lazy=True)

    def __init__(self, cv, respiratorio, nefrourologicos, neurologicos ,hematologicos, infectologicos ,endocrinologicos, quirurgicos,
    traumatologicos, alergicos, epidemiologicos, antecedentes_heredofamiliares,estado, consulta_id):
        self.cv = cv
        self.respiratorio=respiratorio
        self.nefrourologicos=nefrourologicos
        self.nefrourologicos=neurologicos
        self.hematologicos=hematologicos
        self.infectologicos=infectologicos
        self.endocrinologicos=endocrinologicos
        self.quirurgicos=quirurgicos
        self.traumatologicos=traumatologicos
        self.alergicos=alergicos
        self.epidemiologicos=epidemiologicos
        self.antecedentes_heredofamiliares=antecedentes_heredofamiliares
        self.estado = estado
        self.consulta_id = consulta_id


class Ginecologicos(db.Model):
    __tablename__='Ginecologicos'
    id = db.Column(db.Integer, primary_key=True)
    e = db.Column(db.String(100))
    p = db.Column(db.String(100))
    c = db.Column(db.String(100))
    a = db.Column(db.String(100))
    mac = db.Column(db.String(100))
    fum = db.Column(db.String(100))
    menarca = db.Column(db.String(100))
    menopausia = db.Column(db.String(100))
    estado = db.Column(db.Boolean)
    fecha_cracion = db.Column(db.DateTime,default=db.func.current_timestamp())
    enfermedades_id = db.Column(db.Integer, db.ForeignKey('enfermedades.id'), nullable=True)

    def __init__(self, e, p, c, a, mac, fum, menarca, menopausia,estado ,enfermedades_id):
        self.e=e
        self.p=p
        self.c=c
        self.a=a
        self.mac=mac
        self.fum=fum
        self.menarca=menarca
        self.menopausia=menopausia
        self.estado = estado
        self.enfermedades_id=enfermedades_id


class Examen_Fisico(db.Model):
    __tablename__='examen_fisico'
    id = db.Column(db.Integer,primary_key=True)
    ta = db.Column(db.String(500))
    fc = db.Column(db.String(500))
    fr = db.Column(db.String(500))
    temperatura = db.Column(db.String(30))
    altura = db.Column(db.String(30))
    peso =  db.Column(db.String(30))
    impresion_general = db.Column(db.String(500))
    constitucion = db.Column(db.String(500))
    facies = db.Column(db.String(500))
    actitud = db.Column(db.String(500))
    decubito = db.Column(db.String(500))
    marcha = db.Column(db.String(500))
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    consulta_id= db.Column(db.Integer, db.ForeignKey('consultas.id'), nullable=True)
    cabeza = db.relationship('Cabeza',backref='examen_fisico',lazy=True)
    cuello = db.relationship('Cuello',backref='examen_fisico',lazy=True)
    abdomen = db.relationship('Abdomen',backref='examen_fisico',lazy=True)
    respitratorio = db.relationship('Respiratorio',backref='examen_fisico',lazy=True)
    cardiovascular = db.relationship('Cardiovascular',backref='examen_fisico',lazy=True)
    piel_faneras_tejido_celular_subcutaneo = db.relationship('Piel_Faneras_Tejido_Celular_Subcutaneo',backref='examen_fisico',lazy=True)
    neurologico = db.relationship('Neurologico',backref='examen_fisico',lazy=True)

    def __init__(self, ta,fc,fr,temperatura, altura, peso, impresion_general, constitucion, 
    facies, actitud, decubito, marcha,estado ,consulta_id):
        self.ta=ta
        self.fc=fc
        self.fr=fr
        self.temperatura=temperatura
        self.altura=altura
        self.peso=peso
        self.impresion_general = impresion_general
        self.constitucion = constitucion
        self.facies = facies
        self.actitud = actitud
        self.decubito = decubito
        self.marcha = marcha
        self.estado = estado
        self.consulta_id = consulta_id
        

    

class Cabeza(db.Model):
    __tablename__='cabeza'
    id = db.Column(db.Integer,primary_key=True)
    craneo_y_cara = db.Column(db.Text)
    cuero_cabelludo= db.Column(db.Text)
    region_frontal= db.Column(db.Text)
    region_obitonasal= db.Column(db.Text)
    region_orinfarengea= db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    examen_fisico_id = db.Column(db.Integer,db.ForeignKey('examen_fisico.id'), nullable=True)

    def __init__(self,craneo_y_cara, cuero_cabelludo, region_frontal, region_obitonasal, 
    region_orinfarengea, estado,examen_fisico_id):
        self.craneo_y_cara=craneo_y_cara
        self.cuero_cabelludo=cuero_cabelludo
        self.region_frontal=region_frontal
        self.region_obitonasal=region_obitonasal
        self.region_orinfarengea=region_orinfarengea
        self.estado = estado
        self.examen_fisico_id=examen_fisico_id

class Cuello(db.Model):
    __tablename__='cuello'
    id = db.Column(db.Integer, primary_key=True)
    inspeccion = db.Column(db.Text)
    palpacion = db.Column(db.Text)
    percusion = db.Column(db.Text)
    auscultacion = db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    examen_fisico_id = db.Column(db.Integer,db.ForeignKey('examen_fisico.id'), nullable=True)

    def __init__(self, inspeccion, palpacion, percusion, auscultacion,estado,
    examen_fisico_id):
        self.inspeccion=inspeccion
        self.palpacion=palpacion
        self.percusion=percusion
        self.auscultacion=auscultacion
        self.estado = estado
        self.examen_fisico_id=examen_fisico_id

class Abdomen(db.Model):
    __tablename__='abdomen'
    id = db.Column(db.Integer, primary_key=True)
    inspeccion = db.Column(db.Text)
    palpacion = db.Column(db.Text)
    percusion = db.Column(db.Text)
    auscultacion = db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    examen_fisico_id = db.Column(db.Integer,db.ForeignKey('examen_fisico.id'), nullable=True)

    def __init__(self, inspeccion, palpacion, percusion, auscultacion,estado,
    examen_fisico_id):
        self.inspeccion=inspeccion
        self.palpacion=palpacion
        self.percusion=percusion
        self.auscultacion=auscultacion
        self.estado = estado
        self.examen_fisico_id=examen_fisico_id

class Respiratorio(db.Model):
    __tablename__='respiratorio'
    id = db.Column(db.Integer, primary_key=True)
    inspeccion = db.Column(db.Text)
    palpacion = db.Column(db.Text)
    percusion = db.Column(db.Text)
    auscultacion = db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    examen_fisico_id = db.Column(db.Integer,db.ForeignKey('examen_fisico.id'), nullable=True)

    def __init__(self, inspeccion, palpacion, percusion, auscultacion,estado,
    examen_fisico_id):
        self.inspeccion=inspeccion
        self.palpacion=palpacion
        self.percusion=percusion
        self.auscultacion=auscultacion
        self.estado = estado
        self.examen_fisico_id=examen_fisico_id

class Cardiovascular(db.Model):
    __tablename__='cardiovascular'
    id = db.Column(db.Integer, primary_key=True)
    inspeccion = db.Column(db.Text)
    palpacion = db.Column(db.Text)
    auscultacion = db.Column(db.Text)
    pulsos = db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    examen_fisico_id = db.Column(db.Integer,db.ForeignKey('examen_fisico.id'), nullable=True)

    def __init__(self, inspeccion, palpacion, auscultacion,pulsos,estado,
    examen_fisico_id):
        self.inspeccion=inspeccion
        self.palpacion=palpacion
        self.auscultacion=auscultacion
        self.pulsos=pulsos
        self.estado = estado
        self.examen_fisico_id=examen_fisico_id


class Piel_Faneras_Tejido_Celular_Subcutaneo(db.Model):
    __tablename__="piel_faneras_tejido_celular_subcutaneo"
    id = db.Column(db.Integer, primary_key=True)
    aspecto = db.Column(db.Text)
    distribucion_pilosa = db.Column(db.Text)
    lesiones = db.Column(db.Text)
    faneras = db.Column(db.Text)
    t_c_subcutaneo = db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    examen_fisico_id = db.Column(db.Integer, db.ForeignKey('examen_fisico.id'), nullable=True)

    def __init__(self,aspecto, distribucion_pilosa,lesiones, faneras, t_c_subcutaneo,estado,examen_fisico_id):
        self.aspecto=aspecto
        self.distribucion_pilosa=distribucion_pilosa
        self.lesiones=lesiones
        self.faneras=faneras
        self.t_c_subcutaneo=t_c_subcutaneo
        self.estado = estado
        self.examen_fisico_id=examen_fisico_id

class Neurologico(db.Model):
    __tablename__='neurologico'
    id = db.Column(db.Integer, primary_key=True)
    glasgow = db.Column(db.Text)
    motilidad_activa = db.Column(db.Text)
    motildiad_pasiva = db.Column(db.Text)
    motilidad_refleja = db.Column(db.Text)
    pares_craneales = db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    examen_fisico_id = db.Column(db.Integer, db.ForeignKey('examen_fisico.id'), nullable=True)
    sensibilidad_profunda = db.relationship('Sensibilidad_Profunda',backref='neurologico',lazy=True)
    sensibilidad_superficial = db.relationship('Sensibilidad_Superficial', backref='neurologico', lazy=True)

    def __init__(self, glasgow,motilidad_activa,motilidad_pasiva,motilidad_refleja,
    pares_craneales, estado ,examen_fisico_id):
        self.glasgow=glasgow
        self.motilidad_activa=motilidad_activa
        self.motildiad_pasiva=motilidad_pasiva
        self.motilidad_refleja=motilidad_refleja
        self.pares_craneales=pares_craneales
        self.estado = estado
        self.examen_fisico_id=examen_fisico_id

    
class Sensibilidad_Profunda(db.Model):
    __tablename__='sensibilidad_profunda'
    id = db.Column(db.Integer, primary_key=True)
    dolor_profunda = db.Column(db.Text)
    vibratoria= db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    neurlogico_id = db.Column(db.Integer,db.ForeignKey('neurologico.id'), nullable=True)

    def __init__(self,dolor_profunda,vibratoria,estado ,neurologico_id):
        self.dolor_profunda=dolor_profunda
        self.vibratoria=vibratoria
        self.estado=estado
        self.neurlogico_id=neurologico_id
    
class Sensibilidad_Superficial(db.Model):
    __tablename__='sensibilidad_superficial'
    id = db.Column(db.Integer, primary_key=True)
    tactil = db.Column(db.Text)
    dolorosa = db.Column(db.Text)
    termica = db.Column(db.Text)
    estado = db.Column(db.Boolean)
    fecha_creacion = db.Column(db.DateTime,default=db.func.current_timestamp())
    neurologico_id = db.Column(db.Integer, db.ForeignKey('neurologico.id'), nullable=True)

    def __init__(self, tactil, dolorosa, termica, estado ,neurologico_id):
        self.tactil=tactil
        self.dolorosa=dolorosa
        self.termica=termica
        self.estado = estado
        self.neurologico_id = neurologico_id