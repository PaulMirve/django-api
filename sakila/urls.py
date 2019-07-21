from django.urls import path, include
from sakila.models import Actor
from sakila.router import router

app_name = 'sakila'

urlpatterns = router.urls

