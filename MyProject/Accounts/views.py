from django.shortcuts import render,redirect
from django.views import View
from . forms import RegisterForm

from . models import AccountModel
from django.contrib.auth import authenticate,login , logout

# Create your views here.


# class Home_view(View):
#     def get(self , request):
#         return render(request , 'Accounts/home.html')

#     def post(self , request):
#         email = request.POST['email']
#         password = request.POST['password']

#         user = authenticate(email = email , password = password)
#         print(user)

#         return redirect('home')


def Home_view(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email = email , password = password)
        print("Email is :",email)
        print("User is :",user)

        if user is not None:
            login(request , user)
            return render(request , 'Accounts/application.html')

    print("invalid form")
    return render(request , 'Accounts/home.html' )



class register_view(View):
    def get(self , request):
        forms = RegisterForm()
        context = { 'forms' : forms}
        return render(request , 'Accounts/register.html' , context)

    def post(self , request):

        forms = RegisterForm(request.POST)
        if forms.is_valid():
            

            first_name = forms.cleaned_data.get('first_name')
            last_name = forms.cleaned_data.get('last_name')
            username = forms.cleaned_data.get('username')
            email = forms.cleaned_data.get('email')
            phone_number = forms.cleaned_data.get('phone_number')
            password = forms.cleaned_data.get('password')

            user = AccountModel.objects.create_user(first_name = first_name , last_name = last_name , username = username , email = email , password = password)

            user.phone_number = phone_number

            user.save()

            return redirect('home')
        else:
            return redirect('register')

def signout(request):
    logout(request)

    return redirect('home')