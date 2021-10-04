from rest_framework import viewsets, mixins
from .serializers import TaskListSerializer
from .models import Task, TaskList, Attachment
from .permissions import IsAllowedEditTaskListElseNone


class TaskListViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet
                      ):
    permission_classes = [IsAllowedEditTaskListElseNone]
    queryset =  TaskList.objects.all()
    serializer_class = TaskListSerializer
