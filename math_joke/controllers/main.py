from flask import Blueprint, current_app,send_from_directory
from flask import request, make_response, url_for, render_template, redirect, json


main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')