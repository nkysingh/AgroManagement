from django.urls import path
from .views import signup_view, login_view, overview_view, logout_view, workers_list_view, add_worker_view, edit_worker_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('overview/', overview_view, name='overview'),
    path('logout/', logout_view, name='logout'),
    path('workers/', workers_list_view, name='workers_list'),
    path('workers/add/', add_worker_view, name='add_worker'),
    path('workers/edit/<int:worker_id>/', edit_worker_view, name='edit_worker'),
]