from locust import Locust, seq_task, TaskSequence, between
import sys


sys.path.append("C:\CompleteProjectPart2")
from custom_client_dir.custom_client import  CustomLocust


class UserBehaviour(TaskSequence):

    @seq_task(1)
    def my_task1(self):
        self.client.custom_req_conn()

    @seq_task(2)
    def my_task2(self):
        self.client.custom_req_send()

    @seq_task(3)
    def my_task3(self):
        self.client.custom_req_disconn()


class CustomUser(CustomLocust):
    task_set = UserBehaviour
    wait_time = between(1, 2)
    host="abc.com"