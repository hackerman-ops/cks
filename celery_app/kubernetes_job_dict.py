job_dict = {
    "apiVersion": "batch/v1",
    "kind": "Job",
    "metadata": {
        "labels": {
            "controller-uid": "fe064c4a-d876-417a-b90c-58c09ece898c",
            "job-name": "shenqianka-core-sopab"
        },
        "name": "shenqianka-core-sopab",
        "namespace": "default",
    },
    "spec": {
        "backoffLimit": 6,
        "completionMode": "NonIndexed",
        "completions": 1,
        "parallelism": 1,
        "selector": {
            "matchLabels": {
                "controller-uid": "fe064c4a-d876-417a-b90c-58c09ece898c"
            }
        },

        "template": {
            "metadata": {
                "labels": {
                    "controller-uid": "fe064c4a-d876-417a-b90c-58c09ece898c",
                    "job-name": "shenqianka-core-sopab"
                }
            },
            "spec": {
                "containers": [
                    {
                        "args": [
                            "echo",
                            "Hello world!"
                        ],
                        "image": "alpine:3.11",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "upload",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File"
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "restartPolicy": "Never",
                "schedulerName": "default-scheduler",
                "securityContext": {},
                "terminationGracePeriodSeconds": 30
            }
        }
    }
}
