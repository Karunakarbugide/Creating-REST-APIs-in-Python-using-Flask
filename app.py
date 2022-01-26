# app.py
from flask import Flask, json, request, jsonify
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

ALLOWED_EXTENSIONS = {'txt', 'sql'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/getfile', methods=["POST"])
def getfile():
    # check if the post request has the file part
    if 'files[]' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    files = request.files.getlist('files[]')

    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'
    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({'message': 'Files successfully uploaded'})
        resp.status_code = 201
        # we can call or pass file to execution code
        print(file)
        with open(file.filename) as f:
            lines = f.readlines()
        print(lines)
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp


if __name__ == '__main__':
    app.run(debug=True)
