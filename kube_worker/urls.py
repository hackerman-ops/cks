from django.conf.urls import url
from kube_worker import views

urlpatterns = [
    url(r"^task$", views.create_task),

]

