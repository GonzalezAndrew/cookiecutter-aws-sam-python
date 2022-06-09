import pytest

from app import app


@pytest.fixture()
def cron_event():
    """ Generates Scheduled CloudWatch Event"""

    return {
        "id": "cdc73f9d-aea9-11e3-9d5a-835b769c0d9c",
        "detail-type": "Scheduled Event",
        "source": "aws.events",
        "account": "123456789012",
        "time": "1970-01-01T00:00:00Z",
        "region": "us-east-1",
        "resources": [
            "arn:aws:events:us-east-1:123456789012:rule/ExampleRule"
        ],
        "detail": {}
    }



def test_lambda_handler(cron_event, mocker):

    ret = app.lambda_handler(cron_event, "")

    assert ret["source"] == "aws.events"
    assert "Scheduled Event" in ret["detail-type"]
