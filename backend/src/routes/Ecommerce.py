from flask import Blueprint, jsonify

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


