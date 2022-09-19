from curses.ascii import HT
from django.shortcuts import render,HttpResponse

from . form import *

from django.contrib import messages

# Create your views here.


def RegisterView(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your Account has been Created !!!")
            #return render(request, 'show.html')
            messages.info(request, "Now you  can login")

            print(messages.get_level(request))

            messages.set_level(request,messages.DEBUG)
            messages.debug(request,"this is new debug")
                        
    else:
        form= RegistrationForm()
    return render (request, "wel.html",{'form':form})


'''
#FOR MESSAGE 

from django.contrib import messages
def RegisterView(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your Account has been Created !!!")
            #return render(request, 'show.html')
        
    else:
        form= RegistrationForm()
        return render (request, "wel.html",{'form':form})






#we can use 

messages.add_message(request,messages.SUCCESS,"Your Account has been Created !!!")  

  or 

messages.success(request,"Your accout created )


or 
messages.info(request, "Now you  can login")

We have some other method get and set level also =====

print(messages.get_level(request))

messages.set_level(request.messages.DEBUG)
messages.debug(request,"this is new debug")

#We Have 
messages.info(request, "Now you  can login")
messages.success(request, "Now you  can login")
messages.warning(request, "Now you  can login")
messages.error(request, "Now you  can login")


# change class tags 
we go in settngs.py and import 

from dango.contrib.messages import constants  as message_s


MESSAGE_TAGS = {message_s.ERROR:'danger'}    - it chane the class , this 2 line code wriiten in seing.py 
#for style the  message check form.py   


'''