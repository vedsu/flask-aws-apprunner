from flask import Blueprint, jsonify
from .model_webinar import WebinarModel

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify({"message": "App is running"})


@main.route("/webinars", methods=["GET"])
def get_webinars():
    try:
        data = WebinarModel.get_all_webinars()
        return jsonify({
            "status": "success",
            "count": len(data),
            "data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@main.route("/webinar", methods=["GET"])
def get_one_webinar():
    try:
        data = WebinarModel.get_one_webinar()
        return jsonify({
            "status": "success",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
