from django.contrib import admin
from .models import *


admin.site.register([Services, Business, Users, Clients, Comments, FAQs])
