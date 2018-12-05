import pytest
import boto3
from moto import mock_dynamodb2

import application

@pytest.fixture
def client():
    return application.app.test_client()

@pytest.fixture()
def mocked_table():
    with mock_dynamodb2():
        conn = boto3.resource('dynamodb')
        chats = conn.create_table(
            TableName="chats",
            KeySchema=[{'AttributeName':'id','KeyType':'HASH'}],
            AttributeDefinitions=[{'AttributeName':'id','AttributeType':'S'}],
            ProvisionedThroughput={'ReadCapacityUnits':5,'WriteCapacityUnits':5})
        yield