import flask
import boto3
import json
import datetime
import uuid
from boto3.dynamodb.conditions import Attr

app = flask.Flask(__name__)

@app.route('/messages', methods=['POST'])
def post_messages():
	chat = {
		'id': str(uuid.uuid4()),
		'message_id': str(uuid.uuid4()),
		'message': 'Hello. World!',
		'message_date': datetime.datetime.utcnow().isoformat(),
		'username': 'bra'
	}
	chats = boto3.resource('dynamodb').Table('chats')
	chats.put_item(Item=chat)
	return flask.make_response(json.dumps(chat), 200, {'Content-Type':'application/json'})

@app.route('/chats/<id>', methods=['GET'])
def get_messages(id):
	chats = boto3.resource('dynamodb').Table('chats')
	result = chats.scan(FilterExpression=Attr('id').eq(id))
	messages = result.get('Items',[])
	return flask.make_response(json.dumps(messages), 200, {'Content-Type':'application/json'})