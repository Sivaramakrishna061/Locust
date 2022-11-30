from locust import HttpLocust, TaskSequence, seq_task, between, events
import socket
import csv

hostname = socket.gethostname()
# 2 lists
request_success_data = [list()]
request_fail_data = [list()]

##save success data in csv
def save_success_stats():
    with open('success_req_stats.csv', 'wt') as csv_file:
        writer = csv.writer(csv_file)
        for value in request_success_data:
            writer.writerow(value)

##save fail data in csv
def save_fail_stats():
    with open('fail_req_stats.csv', 'wt') as csv_file:
        writer = csv.writer(csv_file)
        for value in request_fail_data:
            writer.writerow(value)


def individual_success_handle(request_type, name, response_time, response_length, **kwargs):
    Success_Temp = '"hostname": {},"request_type":{},"name": {},"result":"OK","response_time":{},"response_length":{}' \
        .format(hostname, request_type, name, response_time, response_length)
    #print(Success_Temp)
    request_success_data.append([hostname,request_type,name,"OK",response_time,response_length])



def individual_fail_handle(request_type, name, response_time, response_length, exception, **kwargs):
    Fail_Temp = '"hostname": {},"request_type":{},"name": {},"result":"Not OK","response_time":{},"response_length":{}' \
        .format(hostname, request_type, name, response_time, response_length, exception)
    #print(Fail_Temp)
    request_fail_data.append([hostname, request_type, name, "Not OK", response_time, response_length,exception])

def quit_handler():
    save_success_stats()
    save_fail_stats()

events.request_success += individual_success_handle
events.request_failure += individual_fail_handle
events.quitting+=quit_handler


class UserBehaviour(TaskSequence):

    @seq_task(1)
    def launch_Url(self):
        self.client.get("/InsuranceWebExtJS/")

    @seq_task(2)
    def login_Url(self):
        with self.client.post("/InsuranceWebExtJS/index.jsf"
                , data={"login-form": "login-form", "login-form:email": "qamile2@gmail.com"
                    , "login-form:password": "abc1234", "login-form:login.x": "57"
                    , "login-form:login.y": "9", "javax.faces.ViewState": "j_id1:j_id2"}, catch_response=True) as res2:
            if ("Logged in") not in res2.text:
                res2.failure("User not logged in")
            else:
                res2.success()


class User(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(5, 10)
    host = "http://demo.borland.com"
