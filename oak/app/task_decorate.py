import requests

from app import app_name


class Task:
    name = None

    def delay(self, *args, **kwargs):
        self.apply_async(*args, **kwargs)

    def apply_async(self, *args, **kwargs):
        url = "http://127.0.0.1:8000/api/cks/beat/task"

        kwargs["func_name"] = self.name
        kwargs["app_name"] = app_name
        kwargs["project"] = "shenqianka"
        res = requests.post(url, json={"args": args, "kwargs": kwargs})
 

def task(*args, **opts):
    def inner_create_task_cls(**opts):
        def _create_task_cls(fun):
            task_class = type(fun.__name__, (Task,), dict({
                'name': fun.__name__,
                '_decorated': True,
                '__doc__': fun.__doc__,
                '__module__': fun.__module__,
                'run': staticmethod(fun),
            }, **opts
            ))()

            return task_class

        return _create_task_cls

    return inner_create_task_cls(**opts)(*args)


@task
def task_test(x, y=None):
    print(x)


@task
def task_test1(x, y):
    print(x + y)


# if __name__ == "__main__":
#     task_test.delay(1, y=None)
#     task_test.apply_async(("card_number", "order_number", "price",
#                      "order_status", "unique_id", "user_source", "out_order_id"), kwargs={"1":2},
#                     countdown=5 * 60)
#     task_test.run(1)

#     task_test1.delay(1, 5)
#     task_test1.run(1, 5)


ALL_INTERVAL_TASK = {}

def interval_task(parameter):
    def deco_func(func):
        ALL_INTERVAL_TASK.update({func.__name__: {
            "description": parameter.description,
            "schedule": parameter.schedule,
            "params": parameter.params,
        }})
        def wrapper(*args, **kwargs):
            print(parameter)
            func(*args, **kwargs)
        return wrapper
    return deco_func

class ParamsCreator:
    description = "更新租户$$$"
    schedule = "25, 5, 0, 0,0"
    params = {
        "xiaoying": {
            "args": [1,2,3,4],
            "kwargs": {"namespace": "xy,df,wefe,ewfwe"}
        },
        "xs": {
             "args": [1,2,3,4],
            "kwargs": {"namespace": "xy,df,wefe,ewfwe"}
        },
        "all": {
             "args": [1,2,3,4],
            "kwargs": {"namespace": "xy,df,wefe,ewfwe"}
        }

    }

@interval_task(ParamsCreator)
def test():
    pass

print(ALL_INTERVAL_TASK)