from flask import Flask, request, jsonify
from flask_restx import Api, Resource, reqparse

# -----------------------------------------------------
# flask and api setting
# -----------------------------------------------------
app = Flask(__name__)
api = Api(app, version='1.0', title='test api list',description='테스트 REST API 문서',)

api_ns = api.namespace('aiagent', description='hello world API')

# -----------------------------------------------------
# api list
# -----------------------------------------------------
df_get_parser = reqparse.RequestParser()
df_get_parser.add_argument('value', type=int, default=0, help='값 입력')
df_get_parser.add_argument('text', type=str, default='', help='문자열 입력')

@api.route('/hello')
class getHelloWorld(Resource):
    @api.expect(df_get_parser)
    def get(self):
        _query_params = request.args
        print('_query_params: ' + str(_query_params))

        _value = _query_params.get('value', 0)
        _text = _query_params.get('text', '')
        print('_value: ' + str(_value))
        print('_text: ' + str(_text))

        return  {'hello': 'world'}

    def put(self):
        _json = request.json.get('data')
        print('put request json: ' + str(_json))
        return  {'hello': 'world'}

@api_ns.route('/hello')
class aiagent_getHelloWorld(Resource):
    def get(self):
        return  {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # , debug=True)
