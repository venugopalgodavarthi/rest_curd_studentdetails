from django.urls import path
from curd import views
urlpatterns= [
    path(r'studentlist/',views.student_list,name="student_list"),
    path(r'studentdetail/<pk>/',views.student_detail,name="student_detail"),
    path(r'student/<pk>/',views.studentd,name="student"),
]