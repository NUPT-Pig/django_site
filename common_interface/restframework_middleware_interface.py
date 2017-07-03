from rest_framework.permissions import BasePermission


class TestPermissions(BasePermission):

    def has_permission(self, request, view):
        return True
