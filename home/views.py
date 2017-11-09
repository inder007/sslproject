from django.http import HttpResponse
from django.template import loader
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.views import generic
# from django.views.generic import View
# from .forms import Userform


def homepage(request):
    template = loader.get_template('home/homepage.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('home/login.html')
    return HttpResponse(template.render())


def signup(request):
    template = loader.get_template('home/signup.html')
    return HttpResponse(template.render())

#
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



