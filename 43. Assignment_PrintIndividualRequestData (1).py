from locust import HttpLocust, TaskSequence, seq_task, between, events
import socket
## create 2 customized handlers and associte them with request_success & request_failure respectively
##handlers need to print individual request data to console and add some additional info pertaining to request as well

hostname=socket.gethostname()

def individual_success_handle(request_type,name,response_time,response_length,**kwargs):
    Success_Temp='"hostname": {},"request_type":{},"name": {},"result":"OK","response_time":{},"response_length":{}'\
        .format(hostname,request_type,name,response_time,response_length)
    print(Success_Temp)

def individual_fail_handle(request_type,name,response_time,response_length,exception,**kwargs):
    Fail_Temp = '"hostname": {},"request_type":{},"name": {},"result":"Not OK","response_time":{},"response_length":{}' \
        .format(hostname, request_type, name, response_time, response_length,exception)
    print(Fail_Temp)

events.request_success+=individual_success_handle
events.request_failure+=individual_fail_handle

class UserBehaviour(TaskSequence):

    @seq_task(1)
    def launch_Url(self):
        self.client.get("/InsuranceWebExtJS/")

    @seq_task(2)
    def login_Url(self):
        with self.client.post("/InsuranceWebExtJS/index.jsf"
                , data={"login-form": "login-form", "login-form:email": "qamile2@gmail.com"
                    , "login-form:password": "abc123", "login-form:login.x": "57"
                    , "login-form:login.y": "9", "javax.faces.ViewState": "j_id1:j_id2"}, catch_response=True) as res2:
            if ("Logged in") not in res2.text:
                res2.failure("User not logged in")
            else:
                res2.success()


class User(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(5, 10)
    host = "http://demo.borland.com"
