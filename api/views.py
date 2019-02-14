from rest_framework import viewsets, filters
from api.serializers import UserSerializer, ListSerializer, TaskSerializer
from core.models import User, List, Task
from django_filters import rest_framework as djangofilters

# Create your views here.


class ListFilter(djangofilters.FilterSet):
    title = djangofilters.CharFilter(lookup_expr='icontains')
    date = djangofilters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = List
        fields = ['title', 'date', 'completed', ]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    filter_backends = (djangofilters.DjangoFilterBackend, )
    filterset_class = (ListFilter)