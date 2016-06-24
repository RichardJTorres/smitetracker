from app import app
from .smython import SmiteClient

client = SmiteClient(dev_id=app.config.get('DEV_ID'), auth_key=app.config.get("AUTH_KEY"))