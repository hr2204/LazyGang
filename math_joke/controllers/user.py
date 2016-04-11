
from flask import Blueprint, current_app,send_from_directory
from flask import request, make_response, url_for, render_template, redirect, json


user = Blueprint('user', __name__)

@user.route('/mathjoke/api/v1.0/getAllUsers', methods=['POST'])
def getAllUsers():
    req_obj = jsonpickle.decode(request.data)
    
    
    users = [  
        {'name': 'Little Horse'}, 
        {'name': 'Who'}, 
        {'name': 'Gig Ben'}
    ]

    return JSONEncoder().encode(users)