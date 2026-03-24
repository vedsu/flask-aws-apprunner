from app import db


class WebinarModel:

    @staticmethod
    def get_collection():
        return db["webinar_data"]

    @staticmethod
    def get_all_webinars(limit=10):
        webinars = list(
            WebinarModel.get_collection().find({}, {"_id": 0}).limit(limit)
        )
        return webinars

    @staticmethod
    def get_one_webinar():
        webinar = WebinarModel.get_collection().find_one({}, {"_id": 0})
        return webinar
