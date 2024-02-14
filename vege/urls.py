from django.contrib import admin
from django.urls import path, include
from vege.views import *
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from vege.views import recipes, delete_recipe, update_recipe, login_page, register_page, logout_page


urlpatterns = [
    path('recipes/', recipes, name="recipes"),
    path('delete-recipe/<int:id>/', delete_recipe, name="delete_recipe"),
    path('update-recipe/<int:id>/', update_recipe, name="update_recipe"),
    path('', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('logout/', logout_page, name="logout_page"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)