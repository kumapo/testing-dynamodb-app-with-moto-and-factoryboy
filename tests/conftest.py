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
    # use stub for dynamo db
    with mock_dynamodb2():
        conn = boto3.resource('dynamodb')
        # create a table for the stub
        table = conn.create_table(
            TableName="chats",
            KeySchema=[{'AttributeName':'id','KeyType':'HASH'}],
            AttributeDefinitions=[{'AttributeName':'id','AttributeType':'S'}],
            ProvisionedThroughput={'ReadCapacityUnits':5,'WriteCapacityUnits':5})
        # run a testcase in stubbed context
        yield client

@pytest.fixture()
def mocked_client_having_messages_in_chat(client):
    # use stub for dynamo db
    with mock_dynamodb2():
        conn = boto3.resource('dynamodb')
        # create a table for the stub
        table = conn.create_table(
            TableName="chats",
            KeySchema=[{'AttributeName':'id','KeyType':'HASH'}],
            AttributeDefinitions=[{'AttributeName':'id','AttributeType':'S'}],
            ProvisionedThroughput={'ReadCapacityUnits':5,'WriteCapacityUnits':5})
        # build and insert items into the table
        messsages = tests.factory.ChatFactory.dict_factory().build_batch(5, id='ff86c522-a08e-4a2c-a222-80e62c9c059b')
        _ = [table.put_item(Item=messsage) for messsage in messsages]
        # run a testcase in stubbed context
        yield client

@pytest.fixture()
def mocked_client_having_messages_in_chat_manually(client):
    # use stub for dynamo db
    with mock_dynamodb2():
        conn = boto3.resource('dynamodb')
        # create a table for the stub
        table = conn.create_table(
            TableName="chats",
            KeySchema=[{'AttributeName':'id','KeyType':'HASH'}],
            AttributeDefinitions=[{'AttributeName':'id','AttributeType':'S'}],
            ProvisionedThroughput={'ReadCapacityUnits':5,'WriteCapacityUnits':5})
        # build and insert items into the table
        messages = [{
            'id': 'ff86c522-a08e-4a2c-a222-80e62c9c059b',
            'message_id': '0f64eaf2-fcbe-a1cb-0b88-c27234598fde',
            'message': 'What do you dislike about the city?',
            'message_date': '2018-12-05T13:28:18.175895',
            'username': 'bra' 
        }, {
            'id': 'ff86c522-a08e-4a2c-a222-80e62c9c059b',
            'message_id': '199ec6c4-fff7-12c9-0bf9-a1622a2712dd',
            'message': "Security",
            'message_date': '2018-12-05T13:29:37.132019',
            'username': 'bro' 
        }]

        _ = [table.put_item(Item=message) for message in messages]
        # run a testcase in stubbed context
        yield client