from flask import Flask, request, jsonify
from flask_restx import Api, Resource, reqparse, Namespace, fields

# -----------------------------------------------------
# flask and api setting
# -----------------------------------------------------
app = Flask(__name__)
api_default = Api(app, version='1.0', title='test api list',description='테스트 REST API 문서',)
api_sub_0 = api_default.namespace('sub_0', description='hello world API')
api_dl_file = api_default.namespace('download', description='download files')

# -----------------------------------------------------
# api list
# -----------------------------------------------------
@api_default.route('/hello')
class getHelloWorld(Resource):
    _parser = reqparse.RequestParser()
    _parser.add_argument('value', type=int, default=0, help='값 입력')
    _parser.add_argument('text', type=str, default='', help='문자열 입력')

    @api_default.expect(_parser)
    def get(self):  # get method can't have body, means that can't use json to argument
        _query_params = request.args
        print('_query_params: ' + str(_query_params))

        _value = _query_params.get('value', 0)
        _text = _query_params.get('text', '')
        print('_value: ' + str(_value))
        print('_text: ' + str(_text))

        _response = {
            'hello': 'world',
            'value': str(_value),
            'text': str(_text)
        }
        return _response

    _parser = reqparse.RequestParser()
    _parser.add_argument('value', type=int, default=0, help='값 입력')
    _parser.add_argument('text', type=str, default='', help='문자열 입력')

    _model = api_default.model('put', {
            'key1': fields.String(description='value of key1', required=True, example='value1'),
            'key2': fields.String(description='value of key2', required=True, example='value2'),
            })

    @api_default.expect(_parser, _model)
    def put(self):
        _query_params = request.args
        print('_query_params: ' + str(_query_params))

        _value = _query_params.get('value', 0)
        _text = _query_params.get('text', '')
        print('_value: ' + str(_value))
        print('_text: ' + str(_text))

        _data = request.json
        print('_data: ' + str(_data))

        _key1_value = _data.get('key1', '')
        _key2_value = _data.get('key2', '')
        print('_key1_value: ' + str(_key1_value))
        print('_key2_value: ' + str(_key2_value))

        _response = {
            'hello': 'world',
            'value': str(_value),
            'text': str(_text),
            'data': {
                'key1': str(_key1_value),
                'key2': str(_key2_value)
            }
        }
        return _response

    _parser = reqparse.RequestParser()
    _parser.add_argument('value', type=int, default=0, help='값 입력')
    _parser.add_argument('text', type=str, default='', help='문자열 입력')

    _model = api_default.model('put', {
            'key1': fields.String(description='value of key1', required=True, example='value1'),
            'key2': fields.String(description='value of key2', required=True, example='value2'),
            })

    @api_default.expect(_parser, _model)
    def post(self):
        _query_params = request.args
        print('_query_params: ' + str(_query_params))

        _value = _query_params.get('value', 0)
        _text = _query_params.get('text', '')
        print('_value: ' + str(_value))
        print('_text: ' + str(_text))

        _data = request.json
        print('_data: ' + str(_data))

        _key1_value = _data.get('key1', '')
        _key2_value = _data.get('key2', '')
        print('_key1_value: ' + str(_key1_value))
        print('_key2_value: ' + str(_key2_value))

        _response = {
            'hello': 'world',
            'value': str(_value),
            'text': str(_text),
            'data': {
                'key1': str(_key1_value),
                'key2': str(_key2_value)
            }
        }
        return _response

    def delete(self):
        return {'hello': 'world'}

# -----------------------------------------------------
# -----------------------------------------------------
@api_sub_0.route('/hello')
class aiagent_getHelloWorld(Resource):
    _parser = reqparse.RequestParser()
    _parser.add_argument('value', type=int, default=0, help='값 입력')
    _parser.add_argument('text', type=str, default='', help='문자열 입력')

    @api_default.expect(_parser)
    def get(self):
        _query_params = request.args
        print('_query_params: ' + str(_query_params))

        _value = _query_params.get('value', 0)
        _text = _query_params.get('text', '')
        print('_value: ' + str(_value))
        print('_text: ' + str(_text))

        _response = {
            'hello': 'world',
            'value': str(_value),
            'text': str(_text),
            'data': {
                'dummykey0': 'value0',
                'dummykey1': 'value1'
            }
        }
        return _response

# -----------------------------------------------------
# -----------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # , debug=True)
