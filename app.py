from flask import Flask, jsonify
#from flask_cors import CORS
from urls.user.user import user_bp



app = Flask(__name__)

#CORS(app)


# '''
#   API Default Route
# '''
# @app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def index():
#   return jsonify({'message': "Hello theoceann.com ?"}), 200

# @app.route('/')
# def hello_world():
#     return 'Hello World'

app.register_blueprint(user_bp,url_prefix="/user")


 
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)