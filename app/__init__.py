from flask import Flask
from pymongo import MongoClient
import boto3
import json

mongo_client = None
db = None


def get_secret():
    secret_name = "pharmaprofsbackend"
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    response = client.get_secret_value(SecretId=secret_name)
    secret = response['SecretString']

    return json.loads(secret)


def create_app():
    global mongo_client, db

    app = Flask(__name__)

    # Fetch secret from AWS Secrets Manager
    secret = get_secret()

    # Extract connection string
    mongo_uri = secret["CONNECTION_STRING"]

    # Initialize MongoDB
    mongo_client = MongoClient(mongo_uri)

    # Explicit DB selection (recommended)
    db = mongo_client["webinarprof"]

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app
