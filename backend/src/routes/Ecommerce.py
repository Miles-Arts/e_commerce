from flask import Blueprint, jsonify, request
import uuid
#entities
from models.entities.Ecommerce import Ecommerce

#models

from models.Ecommerce_models import Ecommerce_Model

main=Blueprint('ecommerce_blueprint', __name__)

@main.route('/')
def get_persona():
    
    try:
        
        persona=Ecommerce_Model.get_ecommerce()
        return jsonify(persona)
        
    except Exception as ex:  
    
        return jsonify({'message':str(ex)}),500


@main.route('/<id_persona>')
def get_persona_by_id(id_persona):  # Cambié el nombre de la función
    try:
        ecommerce = Ecommerce_Model.get_ecommerce_by_id(id_persona)
        if ecommerce is not None:
            return jsonify(ecommerce)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_persona_by_id():
    try:
        # Obtén los datos del cuerpo de la solicitud
        documento = int(request.json['documento'])
        nombres = request.json['nombres']
        apellidos = request.json['apellidos']
        correo = request.json['correo']
        #metodo_de_pago = bool(request.json['metodo_de_pago'])  # Convertir a booleano
        metodo_de_pago = request.json['metodo_de_pago']  # Convertir a booleano
        fecha_nacimiento = request.json['fecha_nacimiento']
        direccion = request.json['direccion']
        celular = int(request.json['celular'])

        # Valida y convierte la fecha de nacimiento
        from utils.DateFormat import DateFormat
        fecha_nacimiento = DateFormat.convert_data(fecha_nacimiento)

        # Genera un UUID para el ID
        id = uuid.uuid4()

        # Crea un objeto Ecommerce
        id_personas = Ecommerce(
            str(id), documento, nombres, apellidos, correo, metodo_de_pago, fecha_nacimiento, direccion, celular
        )

        # Llama al modelo para insertar los datos
        affected_rows = Ecommerce_Model.add_ecommerce(id_personas)

        # Verifica si la inserción fue exitosa
        if affected_rows == 1:
            return jsonify(id_personas.to_JSON()), 201  # Devuelve el objeto en formato JSON
        else:
            return jsonify({'message': "Error on insert 😅"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500