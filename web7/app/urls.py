from django.contrib import admin
from django.urls import path, include
from .views import IndexView, ServiceView, ServiceDetailView,  BusinessView, BusinessDetailView, UsersView, UsersDetailView, ClientsView, CommentView, FAQsView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('services/', ServiceView.as_view(), name='services'),
    path('services/', ServiceDetailView.as_view(), name='services-detail'),
    path('business/', BusinessView.as_view(), name='business'),
    path('business-detail/', BusinessDetailView.as_view(), name='business-detail'),
    path('clients/', ClientsView.as_view(), name='clients'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('faqs/', FAQsView.as_view(), name='faqs'),
    path('users/', UsersView.as_view(), name='users'),
    path('users-detail/', UsersDetailView.as_view(), name='users-detail'),

]