import os
import json
import boto3
from flask import Flask
from botocore.exceptions import ClientError

def get_secrets():
    secret_name = "pharmaprofsbackend"
    region_name = "us-east-1"
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)
    
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        return json.loads(get_secret_value_response['SecretString'])
    except Exception as e:
        print(f"Critical Error: Could not fetch secrets. {e}")
        return {}

def create_app():
    app = Flask(__name__)
    
    # 1. Load Secrets
    secrets = get_secrets()
    app.config.update(
        SQLALCHEMY_DATABASE_URI=secrets.get('CONNECTION_STRING'),
        # ... your other secrets ...
    )

    # 2. Register Blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

app = create_app()
