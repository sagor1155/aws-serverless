import time
import uuid
import boto3

# dynamodb = boto3.resource('dynamodb')

def create(event, context):
    print("Lambda Invoked\n")
    data = event['body']
    timestamp = str(time.time())
    item = {
        'id': str(uuid.uuid1()),
        'data': data,
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # # write the todo to the database
    # table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    # table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": item
    }

    return response