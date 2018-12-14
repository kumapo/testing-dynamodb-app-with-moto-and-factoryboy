import flask
import boto3
import json
import datetime
import uuid
from boto3.dynamodb.conditions import Attr

app = flask.Flask(__name__)

@app.route('/chats', methods=['POST'])
def post_chat():
    messages = flask.request.json if isinstance(flask.request.json, list) else [flask.request.json]

    chats = boto3.resource('dynamodb').Table('chats')
    chat_id = str(uuid.uuid4())
    items = []
    for message in messages:
        item = {
            'id': chat_id,
            'message_id': message.get('message_id'),
            'message': message.get('message'),
            'message_date': message.get('message_date'),
            'username': message.get('username')
        }
        result = chats.put_item(Item=item)
        if result.get('ResponseMetadata',{}).get('HTTPStatusCode') == 200:
            items.append(item)

    if 0 < len(items):
        return flask.make_response(json.dumps(items), 
                                   200, {'Content-Type':'application/json'})
    else:
        return flask.make_response(json.dumps({'message':'something went wrong'}), 
                                   500, {'Content-Type':'application/json'})

@app.route('/chats/<id>', methods=['GET'])
def get_messages(id):
    chats = boto3.resource('dynamodb').Table('chats')
    result = chats.scan(FilterExpression=Attr('id').eq(id))
    items = result.get('Items',[])
    return flask.make_response(json.dumps(items), 200, {'Content-Type':'application/json'})