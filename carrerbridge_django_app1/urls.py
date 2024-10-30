from  django.urls import path
from . import views
urlpatterns = [
    #path('',views.home,name='home'),
    path('',views.index,name='home'),
    path('Student_table/',views.student_table,name='Student_table'),
]