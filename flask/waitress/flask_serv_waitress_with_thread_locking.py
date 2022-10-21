from flask import Flask, request, jsonify, send_file, abort
from waitress import serve
import threading
import time
from pathlib import Path
import json
test_script_lock = None

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
    test_script_lock.acquire()
    print('request: ' + str(request))
    data = request.json
    print('data: ' + str(data))
    time.sleep(0.2)
    test_script_lock.release()
    return 'python get PUT method\n'

@app.route('/get', methods = ['GET'])
def get():
    test_script_lock.acquire()
    print('request: ' + str(request))
    data = json.dumps(dict(
                email='unknown@unknown.com',
                username='unknown'))
    contect_type='application/json'
    time.sleep(0.2)
    test_script_lock.release()
    return data

@app.route('/post', methods = ['POST'])
def post():
    test_script_lock.acquire()
    print('request: ' + str(request))
    data = request.json
    print('data: ' + str(data))
    time.sleep(0.2)
    test_script_lock.release()
    return 'python get POST method\n'

@app.route('/delete', methods = ['DELETE'])
def delete():
    test_script_lock.acquire()
    print('request: ' + str(request))
    time.sleep(0.2)
    test_script_lock.release()
    return 'python get DELETE method\n'

@app.route('/showFileInBrowser', methods = ['GET'])
def showFileInBrowser():
    test_script_lock.acquire()
    _path = './'
    _fileName = '_sample_text_file.txt'
    _filePath = _path + _fileName
    time.sleep(0.2)
    test_script_lock.release()
    if Path(_filePath).exists():
        return send_file(_filePath)
    else:
        return abort(404)

@app.route('/downloadFile', methods = ['GET'])
def downloadFile():
    test_script_lock.acquire()
    _path = './'
    _fileName = '_sample_text_file.txt'
    _filePath = _path + _fileName
    time.sleep(0.2)
    test_script_lock.release()
    if Path(_filePath).exists():
        return send_file(_filePath, as_attachment=True)
    else:
        return abort(404)

if __name__ == '__main__':
    test_script_lock = threading.Lock()
    serve(app, host="0.0.0.0", port=5000)  #app.run(debug=True, host='0.0.0.0', port=5000)

