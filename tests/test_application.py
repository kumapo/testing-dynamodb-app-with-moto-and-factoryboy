import pytest

def test_post_chats(mocked_table, client):
	res = client.post('/messages')
	assert res.json is not None

def test_get_chat_given_id(client):
	res = client.get('/chats/ff86c522-a08e-4a2c-a222-80e62c9c059b')
	assert res.json is not None