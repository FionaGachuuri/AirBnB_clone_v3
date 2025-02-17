#!/usr/bin/python3
'''Index view for API status check.'''
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    '''Returns the status of the API.'''
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieves the number of each object by type"""
    objects = {
        "amenities": Amenity, 
        "cities": City, 
        "places": Place, 
        "reviews": Review, 
        "states": State, 
        "users": User
    }
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)
