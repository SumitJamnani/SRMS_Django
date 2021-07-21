from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Accounts.models import ExtendedUser
from Batch.models import Batch_m
from Course.models import Course_m
from Faculty_Subject.models import Faculty_m
from Semester.models import Semester_m
from Subject.models import Subject_m


# For Deciding BaseTemplate For Page.
def base_template(request):
    UserRole = ExtendedUser.objects.filter(user_id = request.user.id).values('user_role')
    if UserRole[0]['user_role'] == 'Director':
        BaseTemplate = 'director_panel.html'
    elif UserRole[0]['user_role'] == 'Faculty':
        BaseTemplate = 'faculty_panel.html'
    elif UserRole[0]['user_role'] == 'Admin':
        BaseTemplate = 'admin_panel.html'
    return BaseTemplate

#For Allocating Subject To Respected Faculty
def allocate_subject(request):
    if request.user.is_active:
        CourseData = Course_m.objects.all()
        SemesterData = Semester_m.objects.all()
        BatchData = Batch_m.objects.all()
        UserData = ExtendedUser.objects.all()
        SubjectData = Subject_m.objects.all()
        FactSubjectData = Faculty_m.objects.all().order_by('-fact_subject_id')
        BaseTemplate = base_template(request)
        context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BatchData' : BatchData, 'UserData' : UserData, 'SubjectData' : SubjectData, 'FactSubjectData' : FactSubjectData, 'BaseTemplate' : BaseTemplate}

        if request.method == 'POST':
            if request.POST.get('course_id') is not None and request.POST.get('faculty_id') is not None and request.POST.get('semester_id') is not None and request.POST.get('subject_id') is not None:
                course_id = Course_m.objects.get(course_id=request.POST.get('course_id'))
                batch_id = Batch_m.objects.get(semester_id=request.POST.get('batch_id'))
                faculty_id = User.objects.get(id=request.POST.get('faculty_id'))
                semester_id = Semester_m.objects.get(semester_id=request.POST.get('semester_id'))
                subject_id = Subject_m.objects.get(subject_id=request.POST.get('subject_id'))
                FactSubjectRecord = Faculty_m(course_id=course_id, semester_id=semester_id, batch_id=batch_id, faculty_id=faculty_id, subject_id=subject_id)
                FactSubjectRecord.save()
                messages.success(request, "Subject Allocated To Faculty Successfully!!")
                return render(request, "faculty_mgmt.html", context)
            else:
                messages.error(request, "Please Select Proper options From Dropdown!!")
                return render(request, "faculty_mgmt.html", context)
        else:
            BaseTemplate = base_template(request)
            return render(request, "faculty_mgmt.html", context)
    else:
        return redirect("/")
