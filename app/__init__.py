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
        service_name="secretsmanager",
        region_name=region_name
    )

    response = client.get_secret_value(SecretId=secret_name)
    secret_string = response["SecretString"]
    return json.loads(secret_string)


def create_app():
    global mongo_client, db

    app = Flask(__name__)

    try:
        secret = get_secret()
        mongo_uri = secret["CONNECTION_STRING"]

        mongo_client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        mongo_client.admin.command("ping")
        db = mongo_client["webinarprof"]

        print("MongoDB connected successfully")
    except Exception as e:
        print(f"Startup error: {e}")
        raise

    from .routes import main
    app.register_blueprint(main)

    return app
