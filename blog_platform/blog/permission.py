from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of a post to edit or delete it.


    """

    def has_object_permission(self, request, view, obj):
        # Allow all users to view the post (GET, HEAD, OPTIONS)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Only allow the owner of the post or an admin to update or delete
        if request.user == obj.user or request.user.is_staff:
            return True

        # If the user is not the owner and not an admin, deny the action
        return False
