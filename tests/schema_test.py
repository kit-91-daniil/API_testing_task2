import pytest

from clients.posts.posts_client import PostsClient
from tests.data.json_schemas import Schemas
from tests.data.payload import Payload
from tests.helpers.validator_helper import validate_schema, assert_schema_is_empty

client = PostsClient()

post_schema = Schemas.POST_SCHEMA


@pytest.mark.create
@pytest.mark.create_post_schema
@pytest.mark.parametrize("new_title, new_body", Payload.CORRECT_TITLE_BODY_PAYLOAD)
def test_create_post_operation_has_expected_schema(new_title, new_body):
    create_post_response = client.create_post(new_title=new_title, new_body=new_body)
    validate_schema(create_post_response, post_schema)


@pytest.mark.read
@pytest.mark.read_post_schema
@pytest.mark.parametrize("post_id", Payload.CORRECT_POST_IDS)
def test_read_post_operation_schema_is_empty(post_id):
    read_post_response = client.get_post_by_id(post_id)
    validate_schema(read_post_response, post_schema)


@pytest.mark.read_negative
@pytest.mark.read_post_schema_negative
@pytest.mark.parametrize("post_id", Payload.INCORRECT_POST_IDS)
def test_read_post_operation_has_unexpected_schema(post_id):
    read_post_response = client.get_post_by_id(post_id)
    assert_schema_is_empty(read_post_response)


@pytest.mark.update
@pytest.mark.update_post_schema
@pytest.mark.parametrize("post_id, new_title, new_body", Payload.CORRECT_ID_TITLE_BODY_PAYLOAD)
def test_update_post_operation_has_expected_schema(post_id, new_title, new_body):
    update_response = client.update_post(update_post_id=post_id,
                                         new_title=new_title, new_body=new_body)
    validate_schema(update_response, post_schema)


@pytest.mark.update_negative
@pytest.mark.update_post_schema_negative
@pytest.mark.parametrize("post_id, new_title, new_body", Payload.INCORRECT_ID_TITLE_BODY_PAYLOAD)
def test_update_post_operation_schema_is_empty(post_id, new_title, new_body):
    update_response = client.update_post(update_post_id=post_id,
                                         new_title=new_title, new_body=new_body)
    assert_schema_is_empty(update_response)


@pytest.mark.delete
@pytest.mark.delete_post_schema
@pytest.mark.parametrize("post_id", Payload.CORRECT_POST_IDS)
def test_delete_post_operation_schema_is_empty(post_id):
    delete_post_response = client.delete_post(delete_post_id=post_id)
    assert_schema_is_empty(delete_post_response)


@pytest.mark.delete_negative
@pytest.mark.delete_post_schema_negative
@pytest.mark.parametrize("post_id", Payload.INCORRECT_POST_IDS)
def test_neg_delete_post_operation_schema_is_empty(post_id):
    delete_post_response = client.delete_post(delete_post_id=post_id)
    assert_schema_is_empty(delete_post_response)
