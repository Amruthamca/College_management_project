from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name="signup"),
    path('adminhome',views.adminhome,name='adminhome'),
    path('addcourse',views.addcourse,name="addcourse"),
    path('add_coursedb',views.add_coursedb,name="add_coursedb"),
    path('add_student',views.add_student,name="add_student"),
    path('add_studentdb',views.add_studentdb,name="add_studentdb"),
    path('show_details',views.show_details,name="show_details"),
    path('edit/<int:pk>',views.edit,name="edit"),
    path('editdb<int:pk>',views.editdb,name="editdb"),
    path('delete<int:pk>',views.delete,name="delete"),
    path('add_teacher',views.add_teacher,name="add_teacher"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('logout1',views.logout1,name="logout1"),
    path('show_teacher',views.show_teacher,name="show_teacher"),
    path('delete_teacher/<int:pk>',views.delete_teacher,name="delete_teacher"),
    path('profile',views.profile,name="profile"),
    path('teacher_home',views.teacher_home,name="teacher_home"),
    path('edit_teacher',views.edit_teacher,name="edit_teacher"),
    path('edit_details_tchr/<int:pk>',views.edit_details_tchr,name="edit_details_tchr"),
]