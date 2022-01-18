from django.conf.urls import url
from django_celery_beat import views

urlpatterns = [
    url(r"^task$", views.create_task),

]

