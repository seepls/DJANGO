"""
authentication or identification by itself is not usually sufficient to gain information | code.
 entity requesting access must have authorization .
 
 authentication + throttling : together determine if request granted | denied 
 
 permission checks run at start of the view. before any other code.
 
 mainly and mostly uses request.user |& request.auth
 
 """
  IsAuthenticated  
  
  """
  Permissions in REST framework are always defined as a list of permission classes.
  
  before running the main body , each permision in the list is checked 
  
  if any permission fails -exceptions.PermissionDenied or
                          -exceptions.NotAuthenticated
  
  and the main body wont run 
  """
  
 """
 Object Level Permissions::
  are used to determine if a user should be allowed to act on a particular object.which will be a modal instance.
  
 - run by generic views when .get_object() is called. exceptions.PermissionDenied raised if not.
 - if want to enforce or override , ecplicitly call .check_object_permissions(request, obj) .
 at the point at which you've retrieved the object.
 
 
