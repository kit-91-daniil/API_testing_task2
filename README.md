Implementation Test Automation Framework for REST API automated testing https://jsonplaceholder.typicode.com/

# 1) Clone repository: 

$ clone https://github.com/kit-91-daniil/API_testing_task2.git

# 2) From the command line in the project's root directory run: 

$ pipenv install

# 3) For launch tests use commands:

# POSITIVE TESTS:
# CREATE POST
$ python -m pytest -m create_post  --alluredir=allure_reports/ -n auto --reportportal
$ python -m pytest -m create_post_schema  --alluredir=allure_reports/ -n auto --reportportal
# OR FOR BOTH THE TESTS use:
$ python -m pytest -m create  --alluredir=allure_reports/ -n auto --reportportal


# READ POST
$ python -m pytest -m read_post  --alluredir=allure_reports/ -n auto --reportportal
$ python -m pytest -m read_post_schema  --alluredir=allure_reports/ -n auto --reportportal
# OR FOR BOTH THE TESTS use:
$ python -m pytest -m read  --alluredir=allure_reports/ -n auto --reportportal


# UPDATE POST
$ python -m pytest -m update_post  --alluredir=allure_reports/ -n auto --reportportal
$ python -m pytest -m update_post_schema  --alluredir=allure_reports/ -n auto --reportportal
# OR FOR BOTH THE TESTS use:
$ python -m pytest -m update  --alluredir=allure_reports/ -n auto --reportportal


# DELETE POST
$ python -m pytest -m delete_post  --alluredir=allure_reports/ -n auto --reportportal
$ python -m pytest -m delete_post_schema  --alluredir=allure_reports/ -n auto --reportportal
# OR FOR BOTH THE TESTS use:
$ python -m pytest -m delete  --alluredir=allure_reports/ -n auto --reportportal


# NEGATIVE TESTS
# READ POST
$ python -m pytest -m read_post_negative  --alluredir=allure_reports/ -n auto --reportportal
$ python -m pytest -m read_post_schema_negative  --alluredir=allure_reports/ -n auto --reportportal
# OR FOR BOTH THE TESTS use:
$ python -m pytest -m read_negative  --alluredir=allure_reports/ -n auto --reportportal

# UPDATE POST
$ python -m pytest -m update_post_negative  --alluredir=allure_reports/ -n auto --reportportal
$ python -m pytest -m update_post_schema_negative  --alluredir=allure_reports/ -n auto --reportportal
# OR FOR BOTH THE TESTS use:
$ python -m pytest -m update  --alluredir=allure_reports/ -n auto --reportportal

# DELETE POST
$ python -m pytest -m delete_post_negative  --alluredir=allure_reports/ -n auto --reportportal
$ python -m pytest -m delete_post_schema_negative  --alluredir=allure_reports/ -n auto --reportportal
# OR FOR BOTH THE TESTS use:
$ python -m pytest -m delete  --alluredir=allure_reports/ -n auto --reportportal

# OR for launch all the tests
$ python -m pytest -m --alluredir=allure_reports/ -n auto --reportportal

# To open allure reports use command below:
$ `allure serve allure_reports/`