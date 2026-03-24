from flask import current_app
from pymongo import MongoClient

def get_all_webinars():
    # Retrieve the connection string from the Flask config
    connection_string = current_app.config.get('SQLALCHEMY_DATABASE_URI') # Or CONNECTION_STRING
    
    if not connection_string:
        return {"error": "Database connection string not found"}, 500

    try:
        client = MongoClient(connection_string)
        # Assuming your database name is 'webinarprof'
        db = client['webinarprof'] 
        collection = db['webinar_data']
        
        # Fetch data and convert MongoDB cursor to a list
        # We exclude the MongoDB '_id' because it is not JSON serializable by default
        webinars = list(collection.find({}, {"_id": 0}))
        
        return webinars
    except Exception as e:
        return {"error": str(e)}, 500
