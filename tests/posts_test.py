import pytest
from clients.posts.posts_client import PostsClient
from tests.assertions.people_assertions import Assertions
from tests.data.payload import Payload
from utils.logger import logger

client = PostsClient()


@pytest.mark.create
@pytest.mark.create_post
@pytest.mark.parametrize("new_title, new_body", Payload.CORRECT_TITLE_BODY_PAYLOAD)
def test_new_post_can_be_created(new_title, new_body):
    response = client.create_post(new_title=new_title, new_body=new_body)
    Assertions.status_code_created(response)
    Assertions.post_title_is_correct(response, new_title)


@pytest.mark.read
@pytest.mark.read_post
@pytest.mark.parametrize("post_id", Payload.CORRECT_POST_IDS)
def test_post_can_be_read(post_id):
    response = client.get_post_by_id(post_id)

    Assertions.status_code_ok(response)
    Assertions.post_id_is_correct(response, post_id)


@pytest.mark.read_negative
@pytest.mark.read_post_negative
@pytest.mark.parametrize("post_id", Payload.INCORRECT_POST_IDS)
def test_post_can_be_read_neg(post_id):
    response = client.get_post_by_id(post_id)
    Assertions.status_code_not_found(response)
    Assertions.payload_is_empty(response)


@pytest.mark.update
@pytest.mark.update_post
@pytest.mark.parametrize("post_id, new_title, new_body",
                         Payload.CORRECT_ID_TITLE_BODY_PAYLOAD)
def test_post_can_be_updated(post_id, new_title, new_body):
    update_response = client.update_post(update_post_id=post_id,
                                         new_title=new_title, new_body=new_body)
    Assertions.status_code_created(update_response)
    Assertions.post_title_is_correct(update_response, new_title)


@pytest.mark.update_negative
@pytest.mark.update_post_negative
@pytest.mark.parametrize("post_id, new_title, new_body",
                         Payload.INCORRECT_ID_TITLE_BODY_PAYLOAD)
def test_post_can_be_updated_neg(post_id, new_title, new_body):
    update_response = client.update_post(update_post_id=post_id,
                                         new_title=new_title, new_body=new_body)
    Assertions.status_code_not_found(update_response)
    Assertions.payload_is_empty(update_response)


@pytest.mark.delete
@pytest.mark.delete_post
@pytest.mark.parametrize("post_id", Payload.CORRECT_POST_IDS)
def test_post_can_be_deleted(post_id):
    response = client.delete_post(delete_post_id=post_id)
    Assertions.status_code_ok(response)


@pytest.mark.delete_negative
@pytest.mark.delete_post_negative
@pytest.mark.parametrize("post_id", Payload.INCORRECT_POST_IDS)
def test_post_can_be_deleted_neg(post_id):
    response = client.delete_post(delete_post_id=post_id)
    Assertions.status_code_ok(response)
