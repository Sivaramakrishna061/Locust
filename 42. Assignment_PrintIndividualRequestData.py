from locust import HttpLocust, TaskSequence, seq_task, between, events

## create 2 customized handlers and associte them with request_success & request_failure respectively
##handlers need to print individual request data to console and add some additional info pertaining to request as well

def individual_success_handler():
    pass

def individual_failure_handler():
    pass

events.request_success+=individual_success_handler
events.request_failure+=individual_failure_handler()

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
