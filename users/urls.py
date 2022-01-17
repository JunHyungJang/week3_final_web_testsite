from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.main, name = "main"),
    path("login", views.login_view, name = "login"),
    path("logout", views.logout_view, name = "logout"),
    path("signup", views.signup_view, name = "signup"),
    path("index", views.index, name = "index"),
    path("post", views.post, name = "post"),
    path('post/<int:id>', views.detail, name='detail'),
    path("post/edit/<int:id>", views.edit, name = 'edit'),
    path("post/delete/<int:id>", views.delete, name = 'delete')
]

