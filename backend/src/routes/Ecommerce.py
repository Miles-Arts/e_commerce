from flask import Blueprint, jsonify

main=Blueprint('ecommerce_blueprint', __name__)

@main.route('/')
def get_persona():
    return jsonify({'message':"Nueva Tienda"})


