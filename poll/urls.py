from django.urls import path
from . import views
 
app_name = 'polls'
urlpatterns = [
    path('', views.landing, name ='landing'),
    path('home/', views.index, name ='index'),
    path('<int:ques_id>/', views.detail, name ='detail'),
    path('<int:question_id>/results/', views.results, name ='results'),
    path('<int:question_id>/vote/', views.vote, name ='vote'),
]