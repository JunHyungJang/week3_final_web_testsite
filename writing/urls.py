from django.urls import path


from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name = 'blog'),
    path('blog/<int:pk>',views.posting, name="posting"),
]