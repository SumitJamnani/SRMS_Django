from django.contrib import admin
from django.urls import path, include
from Accounts import views as users_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', users_view.home, name='homepage'),
    path('', users_view.login_view, name='login'),
    path('accounts/', include(('Accounts.urls', 'accounts'), namespace='accounts')),
    path('course/', include(('Course.urls', 'course'), namespace='course')),
    path('semester/', include(('Semester.urls', 'semester'), namespace='semester')),
    path('division/', include(('Division.urls', 'division'), namespace='division')),
    path('batch/', include(('Batch.urls', 'batch'), namespace='batch')),
    path('subject/', include(('Subject.urls', 'subject'), namespace='subject')),
    path('faculty_subject/', include(('Faculty_Subject.urls', 'faculty_subject'), namespace='faculty_subject')),
    path('exam/', include(('Exam.urls', 'exam'), namespace='exam')),
    path('result/', include(('Result.urls', 'result'), namespace='result')),
]
