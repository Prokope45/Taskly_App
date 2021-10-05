from rest_framework import permissions


class IsAllowedEditTaskListElseNone(permissions.BasePermission):
    """
    Custom permissions for the TaskListViewSet to only allow the creator to have editing permission
    """

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.created_by


class IsAllowedToEditTaskElseNone(permissions.BasePermission):
    """
    Custom permissions for the TaskListViewSet to only allow members to have access to the tasks assigned
    """

    def has_permission(self, request, view):

        if not request.user.is_anonymous:
            return request.user.profile.house is not None

        return False

    def has_object_permission(self, request, view, obj):

        return request.user.profile.house is obj.task_list.house


class IsAllowedToEditAttchmentElseNone(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.profile.house is not None

        return False

    def has_object_permission(self, request, view, obj):

        return request.user.profile.house is obj.task.task_list.house
