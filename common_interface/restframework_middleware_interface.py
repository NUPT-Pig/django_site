from rest_framework.permissions import BasePermission


class TestPermissions(BasePermission):
    # todo check request.user.id whether match id in the url or not
    # in case some users modify the request's user_id
    # while in common case , this user_id is read from the cookie.

    def has_permission(self, request, view):
        return True
