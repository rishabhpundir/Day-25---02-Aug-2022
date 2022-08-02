from django.urls import path
from vsapp import views

urlpatterns = [
    # path('user/<user_id>', views.user_details),
    # path('all_user_data', views.all_user_details),
    path('create_user', views.user_create),
]