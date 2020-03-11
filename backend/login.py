from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import json

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'd1c06464c4'  # Change this!
jwt = JWTManager(app)


# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
@app.route('/login', methods=['POST'])
def login():
    credentials=RequestsHTTPTransport(
    url='https://api-uglpec.cloud.okteto.net/v1/graphql',
    use_json=True,
    headers={
        "Content-type": "application/json",
        "x-hasura-admin-secret": "d1c06464c4"
    },
    )

    client = Client(
      retries=3,
      transport=credentials,
      fetch_schema_from_transport=True,
    )

    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    #if username != 'test' or password != 'test':
    #    return jsonify({"msg": "Bad username or password"}), 401

    params = dict({
        'username': username,
	'password': password
    })

    query = gql('''
    query listUsers($username: String!, $password: String!) {
      users(where: {username: {_eq: $username}, password: {_eq: $password}}) {
        npm
      }
    }
    ''')

    id = json.loads(json.dumps(client.execute(query,params)))
    if len(id['users']):
       
       npm = id['users'][0]['npm']
       # Identity can be any data that is json serializable
       access_token = create_access_token(identity=npm)
       return jsonify(access_token=access_token), 200
    
    else:
       return jsonify({"msg": "Bad username or password"}), 401

# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == '__main__':
    app.run()
