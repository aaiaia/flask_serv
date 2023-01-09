from flask import Flask, request, jsonify, send_file, abort
from pathlib import Path
import json
app = Flask(__name__)
@app.route('/')
def root():
    return 'Hello World!\n'

@app.route('/home')
def home():
    return 'Home Directory\n'

@app.route('/user/<user_name>/<int:user_int>')
def user(user_name, user_int):
    return f'User Directory, user_name: {user_name}, user_int: {user_int}!!!\n'

@app.route('/set', methods = ['PUT'])
def set():
    print('request: ' + str(request))
    data = request.json
    print('data: ' + str(data))
    return 'python get PUT method\n'

@app.route('/get', methods = ['GET'])
def get():
    print('request: ' + str(request))
    data = json.dumps(dict(
                email='unknown@unknown.com',
                username='unknown'))
    contect_type='application/json'
    return data

@app.route('/post', methods = ['POST'])
def post():
    print('request: ' + str(request))
    data = request.json
    print('data: ' + str(data))
    return 'python get POST method\n'

@app.route('/delete', methods = ['DELETE'])
def delete():
    print('request: ' + str(request))
    return 'python get DELETE method\n'

@app.route('/showFileInBrowser', methods = ['GET'])
def showFileInBrowser():
    _path = './'
    _fileName = '_sample_text_file.txt'
    _filePath = _path + _fileName
    if Path(_filePath).exists():
        return send_file(_filePath)
    else:
        return abort(404)

@app.route('/downloadFile', methods = ['GET'])
def downloadFile():
    _path = './'
    _fileName = '_sample_text_file.txt'
    _filePath = _path + _fileName
    if Path(_filePath).exists():
        return send_file(_filePath, as_attachment=True)
    else:
        return abort(404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

