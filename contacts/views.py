from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import ContactsApp


# Create your views here.


def contacts_home(request) :
    #return HttpResponse('ok')
    return render(request,'home.html')


# To handle requests from signup page 
def signup(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['pass1']
        secret_code = request.POST['secret_code']
        email = ""

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect('contacts_home')
       
        my_user = User.objects.create_user(username, email, password)

        my_user.is_active = True
        
        return render(request,'home.html', {'email' : username})

    return render(request, 'signup.html')


# To handle requests from signin page
def signin(request):

    if request.method == 'POST':

        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            #fname = user.first_name
            username = request.user.id
            user_details = User.objects.get(id=request.user.id)

            # gets the username here
            name = user_details.username
            
            return redirect('contacts')
        else:
            messages.error(request, "Username doesn't exist")
            return redirect('contacts_home')

    return render(request, 'signin.html')
    



# To display the contacts based on the loggedin user.
def contacts(request) :
    if request.user.id is not None :
        # Instance of ContactsApp class
        contacts = ContactsApp()
        user_details = User.objects.get(id=request.user.id)
        name = user_details.username
        contacts.user = name
        contacts_list = ContactsApp.objects.filter(user=name)
        logged_in = True
        context = {
            'contacts_list' : contacts_list,
            'status' : logged_in,
        }
        # Once the client gives the input
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('mobile') :
                contacts.name = request.POST.get('name')
                contacts.email = request.POST.get('email')
                contacts.phone_number = request.POST.get('mobile')
                contacts.save()
                messages.success(request, "Record saved successfully")
                return render(request, 'contacts.html', context)
            else :
                return render(request, 'contacts.html', context)
        #else :
            #return render(request, 'contacts.html', context)
        return render(request, 'contacts.html', context)
    else :
        return redirect('contacts_home')


# Not using at the moment
def contacts_display(request) :
    user_details = User.objects.get(id=request.user.id)
    name = user_details.username
    contacts_list = ContactsApp.objects.get(user=name)
    context = {
        'contacts_list' : contacts_list,
    }
    return render(request, 'contacts_display.html', context)



# To Terminate the user session.
def signout(request):
    
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('contacts_home')

