from .models import People
from rest_framework import viewsets
from .serializers import PeopleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','DELETE','UPDATE'])
def people_list(request):
    if(request.method == 'GET'):
        return Response(status = 200,data = PeopleSerializer(People.objects.all(),many=True).data)
    elif(request.method=='POST'):
        people = PeopleSerializer(data = request.data)
        if people.is_valid():
            return Response(people.data)
        return Response(status=400)
    elif(request.method=='DELETE'):
        people = PeopleSerializer(data = request.data)
        if people.is_valid():
            return Response(people.data)
        else:
            return Response(status=400)
    else:
        people = PeopleSerializer(data = request.data)
        if people.is_valid():
            return Response(people.data)
        else:
            return Response(status=400)
