from django.conf.urls import url
from beat import views

urlpatterns = [
    url(r"^task$", views.create_task),

]

