from . import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('register/', views.register_instructor, name='register_instructor'),
    path('dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    path('not-approved/', views.not_approved, name='not_approved'),
    path('courses/', views.instructor_course_list, name='instructor_course_list'),
    path('courses/create/', views.instructor_course_create, name='instructor_course_create'),
    path('courses/update/<int:course_id>/', views.instructor_course_update, name='instructor_course_update'),
    path('courses/delete/<int:course_id>/', views.instructor_course_delete, name='instructor_course_delete'),
    path('course/details/<int:course_id>/', views.instructor_course_detail, name='instructor_course_detail'),


    path('modules/add/<int:course_id>/', views.add_module, name='add_module'),  # Updated to include course_id
    path('modules/<int:module_id>/add-content/', views.create_content, name='create_content'),
    path('modules/<int:module_id>/contents/', views.content_list, name='content_list'),
    path('content/<int:content_id>/', views.content_detail, name='content_detail'),

    path('module/edit/<int:module_id>/', views.edit_module, name='edit_module'),
    path('module/delete/<int:module_id>/', views.delete_module, name='delete_module'),
    path('content/edit/<int:content_id>/', views.edit_content, name='edit_content'),
    path('content/delete/<int:content_id>/', views.delete_content, name='delete_content'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)