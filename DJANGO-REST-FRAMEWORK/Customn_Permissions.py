"""
 to implement customn permissions override base permission and impliment either or both the following method :
 - .has_permission(self,request,view)
 - .has_object_permission(self,request,view,obj)
 method  returns true if permission granted else false
 If you need to test if a request is a read operation or a write operation, you should check the request method against
 the constant SAFE_METHODS, which is a tuple containing 'GET', 'OPTIONS' and 'HEAD'.
 """
 if request.method in permissions.SAFE_METHODS:
    # Check permissions for read-only request
else:
    # Check permissions for write request
    
    
    class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
