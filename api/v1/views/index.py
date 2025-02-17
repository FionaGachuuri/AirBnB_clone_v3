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
    objects_count = {}
    for class_name in storage.classes.values():
        objects_count[class_name.__name__.lower()] = storage.count(class_name)
    return jsonify(objects_count)
