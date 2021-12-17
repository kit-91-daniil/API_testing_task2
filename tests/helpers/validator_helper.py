from cerberus import Validator
import json
from assertpy import assert_that


def validate_schema(response, schema):
    post = json.loads(response.text)

    validator = Validator(schema, require_all=True)
    is_valid = validator.validate(post)

    assert_that(is_valid, description=validator.errors).is_true()


def assert_schema_is_empty(response):
    post_json_text = json.loads(response.text)
    assert_that(post_json_text, description="JSON present in response").is_empty()
