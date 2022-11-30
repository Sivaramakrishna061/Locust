from locust import Locust, task, TaskSet, between
import locust.events

custom_event1=locust.events.EventHook()
custom_event2=locust.events.EventHook()

def handler1(a,b,**kwargs):print("add",a+b)
def handler2(a,b,**kwargs):print("diff",b-a)

custom_event1+=handler1
custom_event2+=handler2

class UserBehaviour(TaskSet):
    @task
    def my_task(self):
        myFlag=True
        print("I am task and doing task")
        if(myFlag is False):
         custom_event1.fire(a=1, b=2,msg="I am done")
        else:
            custom_event2.fire(a=1, b=2, msg="I am done")

class User(Locust):
    task_set = UserBehaviour
    wait_time = between(1, 5)
