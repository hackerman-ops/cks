# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from beat.models import ClockedSchedule
from beat.models import PeriodicTask
from django.views.decorators.csrf import csrf_exempt


@api_view(["POST"])
@csrf_exempt
def create_task(request):
    data = request.data
    print(data)
    # ClockedSchedule.objects.create()
    # PeriodicTask.objects.create()
    return Response("OK")
