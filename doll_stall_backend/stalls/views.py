
from django.http import JsonResponse
from .models import Dolls
from .serializers import DollSerializer

# Create your views here.

def doll_list(request):

    dolls = Dolls.objects.all()
    serializer = DollSerializer(dolls, many=True)
    return JsonResponse(serializer.data, safe=False)
    
    
