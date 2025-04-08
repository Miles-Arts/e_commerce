from decouple import config as decouple_config
class Config:
    SECRET_KEY=decouple_config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG=True
    
config={
    'development': DevelopmentConfig
}    