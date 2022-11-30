from locust import Locust

import sys

sys.path.append("C:\CompleteProjectPart2")

from utility.time_measure import decorate_time



class SampleCustomClient:

    def __init__(self, host):
        self.host = host

    @decorate_time
    def custom_req_conn(self):
        print("perform your connection")
        return None

    @decorate_time
    def custom_req_send(self):
         print("perform your send request here !")
         return None

    @decorate_time
    def custom_req_disconn(self):
         print("perform your disconnect here !")
         return None


class CustomLocust(Locust):

    def __init__(self, *args, **kwargs):
        super(CustomLocust, self).__init__(*args, **kwargs)
        self.client = SampleCustomClient(self.host)
