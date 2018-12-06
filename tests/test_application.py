import pytest
import json

MESSAGES_IN_A_CHAT=5
CHAT_ID='ff86c522-a08e-4a2c-a222-80e62c9c059b'

def test_post_chats(mocked_client):
	messages = [{
		'message_id': '9f64eaf2-ecbe-41cb-ab88-b27234598fde',
		'message': 'Where do you stay?',
		'message_date': '2018-12-05T13:26:28.175895',
		'username': 'bra' 
	}, {
		'message_id': '5f9ec6c4-44f7-43c9-bbf9-ed622a2712dd',
		'message': "NYC",
		'message_date': '2018-12-05T13:27:47.132019',
		'username': 'bro' 
	}]
	res = mocked_client.post('/chats', json=messages)
	assert len(res.json) == 2

def test_get_messages_given_id(mocked_client_having_messages_in_chat):
	res = mocked_client_having_messages_in_chat.get('/chats/'+CHAT_ID)
	assert res.json is not None