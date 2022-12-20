from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()

with app.app_context():
    from app.modules import views