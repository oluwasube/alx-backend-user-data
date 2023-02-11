#!/usr/bin/env python3
"""
    Module of Session Authentication view
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv
from auth import Auth

class SessionAuth(Auth):
    pass