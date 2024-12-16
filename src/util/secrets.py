"""Get secrets from AWS's Secrets Manager service."""

import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def get_secret(secret_name: str) -> str | None:
    """Return the value of the given secret."""
    region_name = "us-west-2"
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        return get_secret_value_response["SecretString"]
    except ClientError as error:
        logger.error("Unable to get secret key from AWS")
        logger.error(error)
        return None
