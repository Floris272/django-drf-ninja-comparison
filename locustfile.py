import time

from locust import HttpUser, task, events
import json
import requests
import sys


@events.init_command_line_parser.add_listener
def init_parser(parser):
    parser.add_argument(
        "--endpoint",
        help="endpoint like /employees",
    )

    parser.add_argument(
        "--n",
        help="amount of objects created on start",
    )

    parser.add_argument(
        "--data",
        help="json file used for create request",
    )


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    try:
        requests.post(environment.host + "/ninja/restart", timeout=10)
    except:
        sys.exit(0)

    with open(environment.parsed_options.data, "r") as f:
        json_data = json.load(f)

        for _ in range(int(environment.parsed_options.n)):
            requests.post(
                environment.host + environment.parsed_options.endpoint,
                json=json_data,
                timeout=10,
            )
            time.sleep(0.1)


class TestUser(HttpUser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.endpoint = self.environment.parsed_options.endpoint
        self.n = int(self.environment.parsed_options.n)
        json_file_name = self.environment.parsed_options.data

        with open(json_file_name, "r") as f:
            self.data = json.load(f)

    @task
    def create_and_delete(self):
        data = self.client.post(self.endpoint, json=self.data).json()
        time.sleep(0.1)
        self.client.delete(
            f"{self.endpoint}/{data['id']}", name=f"{self.endpoint}/{{id}}"
        )

    @task
    def get_objects(self):
        self.client.get(self.endpoint)
