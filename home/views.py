from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.views import generic
# from django.views.generic import View
# from .forms import Userform
# from django import forms
from home.forms import MyFacultyForm
from fpagecse import models
from django.http import HttpResponseRedirect


def homepage(request):
    template = loader.get_template('home/homepage.html')
    return HttpResponse(template.render())


def add_model(request):
    if request.method == "POST":
        form = MyFacultyForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')
        else:
            form = MyFacultyForm()
            return render(request, "home/signup.html", {'form': form})
    else:
        form = MyFacultyForm()
        return render(request, "home/signup.html", {'form': form})


def login(request):
    template = loader.get_template('home/login.html')
    return HttpResponse(template.render({}, request))


def signup(request):
    # register = models.Faculty.objects.all()
    template = loader.get_template('home/signup.html')
    # context = {
    #     'register':register,
    # }
    return HttpResponse(template.render({}, request))


# def submit(request):
#     if request.method == 'POST':
#         user_name = request.POST['user']
#         # password = request.POST['pass']
#         # success = user_name.check_password(request.POST['pass'])
#         # obj = models.Faculty(username=user_name, password=password)
#         # obj.save()
#         # if success:
#             return HttpResponseRedirect("/")
#         # else:
#         #     return HttpResponse("Your Password is incorrect")
#     else:
#         return HttpResponse("Error")
#     return HttpResponseRedirect("/")

# class UserFormView(View):
#     form_class = Userform
#     template_name = 'home/login.html'
#
#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     # process form data
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#
#             user = form.save(commit=False)
#
#             # cleaned data
#             username = form.changed_data['username']
#             password = form.changed_data['password']
#             user.set_password(password)
#             user.save()
#
#             # return User objects if crendentials are correct
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#
#                 if user.is_active:
#
#                     login(request, user)
#                     return redirect('home:home')
#
#         return render(request, self.template_name, {'form': form})



