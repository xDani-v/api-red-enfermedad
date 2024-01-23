from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello_world():
    return {"message": "Hola, mundo!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
