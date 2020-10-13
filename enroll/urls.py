from django.urls import path
from.import views


urlpatterns =[
  path('', views.index, name='index'),
  path('delete/<int:id>/', views.delete_data,name='deletedata'),
  path('<int:id>/', views.update,name='update'),
]