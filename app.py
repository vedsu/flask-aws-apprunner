# root/app.py
from app import app

if __name__ == "__main__":
    # This part only runs when you run "python app.py" locally
    # App Runner will use Gunicorn instead
    app.run(host='0.0.0.0', port=8080)
