from docx2python import docx2python
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from core import app
import json
import hashlib
import os, sys

@app.route('/register-peserta',methods=[POST])
def getnpmnama(absensiPeserta):
    data = docx2python(absenPeserta)
    for i in data.body[7]:
        print(i[1])
        print(i[2])
