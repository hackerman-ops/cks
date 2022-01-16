import random

from kubernetes.client import BatchV1Api
from kubernetes.config import load_kube_config


def create_job(*args, **kwargs):
    app = kwargs["app_name"]
    project = kwargs["project_name"]
    namespace = kwargs.get("namespace", "default")
    job_name = f"{project}-{app}-{''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 5))}"
    cfg = {
        'apiVersion': 'batch/v1',
        'kind': 'Job',
        'metadata': {
            'name': job_name
        },
        'spec': {
            'template': {
                'spec': {
                    'restartPolicy':
                        'Never',
                    'containers': [{
                        'name': 'upload',
                        'image': 'alpine:3.11',
                        'args': ['echo', 'Hello world!'],
                        "imagePullPolicy": "IfNotPresent",
                    }]
                }
            }
        }
    }

    load_kube_config(config_file="/home/hacker/.kube/config")
    batch = BatchV1Api()

    api_response = batch.create_namespaced_job(
        body=cfg,
        namespace=namespace)
    print("Job created. status='%s'" % str(api_response.status))
