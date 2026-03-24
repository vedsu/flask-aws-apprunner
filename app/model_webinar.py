import app


class WebinarModel:

    @staticmethod
    def get_collection():
        return app.db["webinar_data"]

    @staticmethod
    def get_all_webinars(limit=10):
        return list(
            WebinarModel.get_collection().find({}, {"_id": 0}).limit(limit)
        )

    @staticmethod
    def get_one_webinar():
        return WebinarModel.get_collection().find_one({}, {"_id": 0})
