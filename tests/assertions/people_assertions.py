from assertpy import assert_that
import requests


class Assertions:
    @classmethod
    def post_title_is_correct(cls, response, title):
        assert_that(response.as_dict["title"],
                    description="Post title is unexpected").is_equal_to(title)

    @classmethod
    def post_id_is_correct(cls, response, post_id):
        assert_that(response.as_dict["id"],
                    description="Post id is unexpected").is_equal_to(post_id)

    @classmethod
    def status_code_ok(cls, response):
        assert_that(response.status_code,
                    description="Status code is not 'ok'").is_equal_to(requests.codes.ok)

    @classmethod
    def status_code_created(cls, response):
        assert_that(response.status_code,
                    description="Status code is not 'created'").is_equal_to(requests.codes.created)

    @classmethod
    def status_code_not_found(cls, response):
        assert_that(response.status_code,
                    description="Status code is not 'not found'").is_equal_to(requests.codes.not_found)

    @classmethod
    def payload_is_empty(cls, response):
        assert_that(response.as_dict, description="Response payload is not empty").is_empty()
