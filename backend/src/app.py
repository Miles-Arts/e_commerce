from flask import Flask
from config import config

#Rutas
from routes import Ecommerce

app=Flask(__name__)

def page_not_found(error):
    return "<h1>La página no funciona<h1>",404

if __name__=='__main__':
    app.config.from_object(config['development'])
    
    #Blue print
    app.register_blueprint(Ecommerce.main,url_prefix='/api/ecommerce')
    
    #error handlers
    app.register_error_handler(404,page_not_found)
    app.run()