from flask import Flask, jsonify, request, Response
import firebase_admin
app = Flask(__name__)
default_app = firebase_admin.initialize_app()
from firebase_admin import auth
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./config/config.json"
@app.route('/')
def hello_world():

    # Start listing users from the beginning, 1000 at a time.
    page = auth.list_users()
    results = []
    for user in auth.list_users().iterate_all():
       results.append({
           'uid' : user.uid,
           'number' : user.phone_number,
           'email' : user.email,
           'disabled' : user.disabled,
           'pic' : user.photo_url
       })
    return jsonify(status='OK', message='SuccessFull', data=results)
if __name__ == '__main__':
#    app.debug = True
#     app.run()
    app.run(debug = True)