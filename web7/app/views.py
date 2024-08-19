from django.shortcuts import render
from django.views import View
import requests


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', )


class ServiceView(View):
    def get(self, request):
        services = requests.get("http://127.0.0.1:8000/service-web/").json()
        context = {
            'services': services
        }
        return render(request, 'service.html', context)


class ServiceDetailView(View):
    def get(self, request):
        services = requests.get("http://127.0.0.1:8000/service-web/").json()
        context = {
            'services': services
        }
        return render(request, 'services-detail.html', context)


class UsersView(View):
    def get(self, request):
        users = requests.get("http://127.0.0.1:8000/users-web/").json()
        context = {
            'users': users
        }
        return render(request, 'users.html', context)


class UsersDetailView(View):
    def get(self, request):
        users = requests.get("http://127.0.0.1:8000/users-web/").json()
        context = {
            'users': users
        }
        return render(request, 'users-detail.html', context)


class ClientsView(View):
    def get(self, request):
        clients = requests.get("http://127.0.0.1:8000/client-web/").json()
        context = {
            'clients': clients
        }
        return render(request, 'clients.html', context)


class CommentView(View):
    def get(self, request):
        comments = requests.get("http://127.0.0.1:8000/comment-web/").json()
        context = {
            'comments': comments
        }
        return render(request, 'comment.html', context)




class FAQsView(View):
    def get(self, request):
        faqs = requests.get("http://127.0.0.1:8000/FAQs-web/").json()
        context = {
            'faqs': faqs
        }
        return render(request, 'FAQs.html', context)


class BusinessView(View):
    def get(self, request):
        business = requests.get("http://127.0.0.1:8000/business-web/").json()
        context = {
            'business': business
        }
        return render(request, 'business.html', context)



class BusinessDetailView(View):
    def get(self, request):
        business = requests.get("http://127.0.0.1:8000/business-web/").json()
        context = {
            'business': business
        }
        return render(request, 'business-detail.html', context)

