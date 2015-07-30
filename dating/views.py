from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

from django.views.generic.base import TemplateView

# Create your views here.
class HomePage(TemplateView):
	template_name = 'index.html'

class MemberPage(TemplateView):
	template_name = 'members.html'

def LogoutPage(request):
	auth_logout(request)
	return redirect('/')

def ErrorPage(request):
	print request
	auth_logout(request)
	redirect('/')
