from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from rest_framework.authtoken.views import obtain_auth_token
from .views import ServiceViewsetWeb, BusinessViewsetWeb, UserViewsetWeb, ClientViewsetWeb, CommentViewsetWeb, FaqViewsetWeb




router = routers.DefaultRouter()
router.register(r"service-web", ServiceViewsetWeb, basename='service-web')
router.register(r"business-web", BusinessViewsetWeb, basename='business-web')
router.register(r"users-web", UserViewsetWeb, basename='users-web')
router.register(r"client-web", ClientViewsetWeb, basename='client-web')
router.register(r"comment-web", CommentViewsetWeb, basename='comment-web')
router.register(r"FAQs-web", FaqViewsetWeb, basename='FAQs-web')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth-token/', obtain_auth_token),
]