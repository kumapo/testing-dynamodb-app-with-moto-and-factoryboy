import pytest
import boto3
from moto import mock_dynamodb2

import application
import tests.factory
import tests.test_application

@pytest.fixture()
def client():
    return application.app.test_client()

@pytest.fixture()
def mocked_client(client):
    with mock_dynamodb2():
        conn = boto3.resource('dynamodb')
        table = conn.create_table(
            TableName="chats",
            KeySchema=[{'AttributeName':'id','KeyType':'HASH'}],
            AttributeDefinitions=[{'AttributeName':'id','AttributeType':'S'}],
            ProvisionedThroughput={'ReadCapacityUnits':5,'WriteCapacityUnits':5})
        yield client

@pytest.fixture()
def mocked_client_having_messages_in_chat(client):
    with mock_dynamodb2():
        conn = boto3.resource('dynamodb')
        table = conn.create_table(
            TableName="chats",
            KeySchema=[{'AttributeName':'id','KeyType':'HASH'}],
            AttributeDefinitions=[{'AttributeName':'id','AttributeType':'S'}],
            ProvisionedThroughput={'ReadCapacityUnits':5,'WriteCapacityUnits':5})

        chats = tests.factory.ChatFactory.dict_factory().build_batch(tests.test_application.MESSAGES_IN_A_CHAT, id=tests.test_application.CHAT_ID)
        _ = [table.put_item(Item=chat) for chat in chats]
        yield client