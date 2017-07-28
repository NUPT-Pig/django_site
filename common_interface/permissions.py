from rest_framework.permissions import BasePermission

class TestPermission(BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser and request.method == "GET" and view.get_name() == 'Student':
            return True
        else:
            return True