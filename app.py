from flask import Flask
from flask_session import Session
from routers import login, plate
import datetime


class SessionConfig:
    SESSION_COOKIE_NAME = 'auth'
    SESSION_FILE_DIR = 'tmp'
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=1)
    SESSION_PERMANENT = True


app = Flask(__name__)
app.config.from_object(SessionConfig)
session = Session(app)

app.secret_key = bytes.fromhex(
    '21a8b87ef1555845cd589ceccbc3ce99171949450636e89bd012a9b0a3221a86'
)


app.register_blueprint(login.blue)
app.register_blueprint(plate.blue)


if __name__ == "__main__":
    app.run(debug=True)