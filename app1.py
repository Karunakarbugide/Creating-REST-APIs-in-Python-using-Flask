from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/post/getfile', methods=["POST"])
def getfile():
    file = request.files['file']
    return file.read()


if __name__ == "__main__":
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(debug=True)
