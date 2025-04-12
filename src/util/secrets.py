"""Get secrets from AWS's Secrets Manager service."""

import logging
import os

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def get_secret(secret_name: str) -> str | None:
    """Return the value of the given secret."""
    session = boto3.session.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )
    client = session.client(
        service_name="secretsmanager",
        region_name="us-west-2",
    )
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret_string = get_secret_value_response["SecretString"]
        if not isinstance(secret_string, str):
            logger.error("SecretString is not a string")
            return None
        return secret_string
    except ClientError as error:
        logger.error("Unable to get secret key from AWS")
        logger.error(error)
        return None
