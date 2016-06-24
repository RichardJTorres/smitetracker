from app import app
from .smython import SmiteClient

client = SmiteClient(dev_id=app.config['DEV_ID'], auth_key=app.config['AUTH_KEY'])
