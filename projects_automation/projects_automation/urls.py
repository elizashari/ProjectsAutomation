from django.contrib import admin
from django.urls import path
from pr_auto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('detail/<int:pk>/', views.detail, name='detail'),
    path('sign_up', views.sign_up, name='sign_up'),

]

