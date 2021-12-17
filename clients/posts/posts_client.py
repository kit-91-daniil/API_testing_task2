import json

from clients.posts.base_client import BaseClient
from config.urls import POSTS_URL
from utils.file_reader import read_file
from utils.logger import logger
from utils.request import APIRequest


class PostsClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.posts_url = POSTS_URL
        self.request = APIRequest()

    def create_post(self, body=None, new_title="New post title", new_body="New post body"):
        logger.info(f"Trying to create post with title: '{new_title}', body: '{new_body}' ")
        new_post_response = self.__create_post(body, new_title=new_title, new_body=new_body)
        result = new_post_response
        logger.info(f"created\n")
        return result

    def __create_post(self, body=None, new_title="New post title", new_body="New post body"):
        if body is None:

            user_payload = read_file('create_post.json')

            user_payload['title'] = new_title
            user_payload['body'] = new_body

            payload = json.dumps(user_payload)

        else:
            payload = json.dumps(body)

        response_ = self.request.post(self.posts_url, payload, self.headers)
        return response_

    def get_post_by_id(self, post_id_):
        logger.info(f"Try to get post by id: {post_id_}")
        result = self.request.get(f"{self.posts_url}/{post_id_}")
        logger.info(f"got\n")
        return result

    def read_all_posts(self):
        logger.info(f"Try to get all the posts")
        post = self.request.get(self.posts_url)
        logger.info(f"got\n")
        return post

    def update_post(self, update_post_id, new_title="post title updated", new_body="post body updated"):
        logger.info(f"Trying to update post id: {update_post_id} with title: '{new_title}', body: '{new_body}' ")
        read_post_response = self.get_post_by_id(update_post_id)
        read_post_response_code = read_post_response.status_code
        if read_post_response_code != 200:
            return read_post_response
        read_post_response_dict = read_post_response.as_dict
        read_post_response_dict["title"] = new_title
        read_post_response_dict["body"] = new_body
        result = self.__create_post(read_post_response_dict)
        logger.info(f"updated\n")
        return result

    def delete_post(self, delete_post_id):
        logger.info(f"Trying to delete post id: {delete_post_id}")
        url = f'{POSTS_URL}/{delete_post_id}'
        result = self.request.delete(url)
        logger.info(f"Deleted\n")
        return result
