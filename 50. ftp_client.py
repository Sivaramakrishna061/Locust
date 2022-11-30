###Assignment
# Connect to FTP server
# Login to FTP server
# Change to desired directory
# Retrieve File
# Disconnect FTP Server

from locust import Locust
from ftplib import FTP

import sys

sys.path.append("C:\CompleteProjectPart2")

from utility.time_measure import decorate_time


class SampleFTPClient:

    def __init__(self, host):
        self.host = host

    @decorate_time
    def FTP_req_conn(self):
        print("perform your connection")
        return None

    @decorate_time
    def FTP_req_send(self):
        print("perform your send request here !")
        return None

    @decorate_time
    def FTP_req_disconn(self):
        print("perform your disconnect here !")
        return None


class FTPLocust(Locust):

    def __init__(self, *args, **kwargs):
        super(FTPLocust, self).__init__(*args, **kwargs)
        self.client = SampleFTPClient(self.host)
