from locust import TaskSet, task, Locust, between,events
import time

#customclient -->prints("hello I am custom request")

# Step 1 --define request in custom client class
# Step 2 measure time
#Step 3 -Indicating request success or failure --> fire events
class CustomClient:
    def __init__(self,host):
        self.host =host
    def custom_req(self):
        try:
         start_time=time.time()

         print("hello I am custom request")
        except Exception as e:

            total_time=int ((time.time() - start_time)*1000)
            events.request_failure.fire(request_type="custom_req", name="req_name", response_time=total_time, exception=e)
        else:
            total_time=int ((time.time() - start_time)*1000)
            events.request_success.fire(request_type="custom_req", name="req_name", response_time=total_time,response_length=0)

#Step 4 Create custom locust class

class CustomLocust(Locust):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.client = CustomClient(self.host)

class UserBehaviour(TaskSet):
    @task
    def my_task(self):
        self.client.custom_req()

#Step 4 Create user with custom locust class
class User(CustomLocust):
    task_set = UserBehaviour
    wait_time = between(1, 5)
    host = "example.com"
