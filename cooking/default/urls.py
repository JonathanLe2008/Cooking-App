from . import views

from django.urls import path

#images
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path("", views.view_recipes, name=""),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("log_out", views.log_out, name="log_out"),
    path('view_recipes', views.view_recipes, name="view_recipes"),
    path('view_recipes/<int:id>/', views.view_recipe_details, name="view_recipe_details"),
    path('search_recipes', views.search_recipes, name="search_recipes"),
    path('create_recipes', views.create_recipes, name="create_recipes"),
    path('user_recipes', views.user_recipes, name="user_recipes"),
    path('random_recipe', views.random_recipe, name="random_recipe"),
    path('edit_recipe/<int:id>/', views.edit_recipe, name="edit_recipe"),
    path('delete_recipe/<int:id>/', views.delete_recipe, name="delete_recipe"),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)