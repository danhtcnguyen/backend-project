from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('get-all-factories/', views.get_all_factories),
    path('get-all-factories/<int:id>/', views.get_factory),
    path('get-sprocket/<int:id>/', views.get_sprocket),
    path('create-sprocket/<int:teeth>/<int:pitch_diameter>/<int:outside_diameter>/<int:pitch>/', views.create_sprocket),
    path('update-sprocket/<int:id>/<int:teeth>/<int:pitch_diameter>/<int:outside_diameter>/<int:pitch>/', views.update_sprocket),

]
