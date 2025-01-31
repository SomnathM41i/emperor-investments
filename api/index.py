import requests 
from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Emperor Investments!"

# For Vercel to recognize the app
app = app