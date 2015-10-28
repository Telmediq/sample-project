from django.shortcuts import render

from django.views.generic import ListView

from users.models import CustomUser

# Create your views here.

class CustomeUserListView(ListView):
    queryset = CustomUser.objects.all()
    template_name = 'users/user_list.html'



user_list = CustomeUserListView.as_view()
