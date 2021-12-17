from dataclasses import dataclass
import requests
from utils.logger import logger


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIRequest:
    def get(self, url):
        response = requests.get(url)
        logger.info(f"code: {response}, json: {response.json()}")
        return self.__get_responses(response)

    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        logger.info(f"code: {response}, json: {response.json()}")
        return self.__get_responses(response)

    def delete(self, url):
        response_ = requests.delete(url)
        logger.info(f"code: {response_}, json: {response_.json()}")
        return self.__get_responses(response_)

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return Response(
            status_code, text, as_dict, headers
        )
