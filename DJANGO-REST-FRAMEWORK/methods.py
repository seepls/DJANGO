"""
method called before dispatching to the handler method 
"""
.check_permissions(self, request)
.check_throttles(self, request)
.perform_content_negotiation(self, request, force= False)

"""Dispatch methods
directly called by View's dispatch method
any action before or after calling handler methods
"""
.get()
.post()
.put()
.patch()
.delete()


-----------------------------------

.initial(self,request,*args,**kwargs)
 
 """ perform any actions need to occur before the handler method gets called . """
 
 .handle_exception(self, exc)
 
 """
 any exception thrown by handler method passed to this method . enforce permission and throttling and perform content negotiation
 
 """
 
 .handle_exception(self , exc)
 
 """ returns response instance or raises exception"""
 
 .initialize_request(self, request,*args, **kwargs)
 
 
 """ 
 ensures that the request object that is passed to the handler method is an instance of handler method 
"""
 
 
