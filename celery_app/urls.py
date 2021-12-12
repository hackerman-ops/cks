from django.conf.urls import url
from celery_app import views

urlpatterns = [
    url(r"^task$", views.create_task),

]

