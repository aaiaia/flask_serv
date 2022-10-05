from flask import Flask
from flask_restx import Api, Resource, reqparse

# -----------------------------------------------------
# flask and api setting
# -----------------------------------------------------
app = Flask(__name__)
api = Api(app, version='1.0', title='test api list',description='테스트 REST API 문서',)

api_ns = api.namespace('test', description='hello world API')

# -----------------------------------------------------
# api list
# -----------------------------------------------------

@api_ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return  {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # , debug=True)
