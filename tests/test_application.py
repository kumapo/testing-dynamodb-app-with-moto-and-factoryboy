import pytest
import json

def test_post_chats(mocked_client):
    # fixtures
    messages = [{
        'message_id': '9f64eaf2-ecbe-41cb-ab88-b27234598fde',
        'message': 'Have ever been to NYC?',
        'message_date': '2018-12-05T13:26:28.175895',
        'username': 'ksr' 
    }, {
        'message_id': '5f9ec6c4-44f7-43c9-bbf9-ed622a2712dd',
        'message': "Yes, I was born there",
        'message_date': '2018-12-05T13:27:47.132019',
        'username': 'bro' 
    }]
    res = mocked_client.post('/chats', json=messages)
    assert len(res.json) == 2

def test_get_messages_given_id_literally(mocked_client_having_messages_in_chat_literally):
    res = mocked_client_having_messages_in_chat_literally.get('/chats/ff86c522-a08e-4a2c-a222-80e62c9c059b')
    assert len(res.json) == 2

def test_get_messages_given_id(mocked_client_having_messages_in_chat):
    res = mocked_client_having_messages_in_chat.get('/chats/ff86c522-a08e-4a2c-a222-80e62c9c059b')
    assert len(res.json) == 5

@pytest.mark.parametrize('messages_in_chat', [ { 'chat_id':'ef86c522-a08e-4a2c-a222-80e62c9c059b',
                                                 'n_messages':12 }])
def test_get_messages_given_messages_in_chat_parametrically(mocked_client_having_messages_in_chat_parametrically, messages_in_chat):
    res = mocked_client_having_messages_in_chat_parametrically.get(f"/chats/{messages_in_chat['chat_id']}")
    assert len(res.json) == messages_in_chat['n_messages']