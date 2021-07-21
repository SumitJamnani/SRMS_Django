from django.contrib import messages
from django.shortcuts import render, redirect
from Accounts.models import ExtendedUser
from Batch.models import Batch_m
from Course.models import Course_m
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


#Insert Particular Batch In The Database
def add_subject(request):
    if request.user.is_active:
        CourseData = Course_m.objects.all()
        SemesterData = Semester_m.objects.all()
        BatchData = Batch_m.objects.all()
        SubjectData = Subject_m.objects.all().order_by('-subject_id')
        BaseTemplate = base_template(request)
        context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BatchData' : BatchData, 'SubjectData' : SubjectData ,'BaseTemplate' : BaseTemplate}

        if request.method == 'POST':
            if request.POST.get('subject_name') != "" and request.POST.get('subject_code') != "" and request.POST.get('course_id') is not None and request.POST.get('semester_id') is not None:
                subject_name = request.POST.get('subject_name')
                subject_code = request.POST.get('subject_code')
                subject_type = request.POST.get('subject_type')
                course_id = Course_m.objects.get(course_id=request.POST.get('course_id'))
                semester_id = Semester_m.objects.get(semester_id=request.POST.get('semester_id'))
                batch_id = Batch_m.objects.get(semester_id=request.POST.get('batch_id'))
                SubjectRecord = Subject_m(subject_name=subject_name, subject_code=subject_code, subject_type=subject_type, course_id=course_id, semester_id=semester_id, batch_id=batch_id)
                SubjectRecord.save()
                messages.success(request, "Subject Inserted Successfully!!")
                return render(request, "subject_mgmt.html", context)
            else:
                messages.error(request, "Please Fill Required Fields!!")
                return render(request, "subject_mgmt.html", context)
        else:
            BaseTemplate = base_template(request)
            return render(request, "subject_mgmt.html", context)
    else:
        return redirect("/")



def update_subject(request):
    pass


#Delete Particular Subject From The Database
def delete_subject(request, id):
    if request.user.is_active:
        if id is not None :
                SubjectSearch = Subject_m.objects.get(subject_id = id)
                SubjectSearch.delete()
                messages.success(request, "Subject Deleted Successfully!!")
                return redirect("/subject/add")
        else :
            messages.error("No Record Found For Selected Semester Id!!")
            return redirect("/subject/add")
    else:
        return redirect("/")


#Search Particular Subject From The Database
def search_subject(request, id):
    if request.user.is_active:
        if id is not None :
            SubjectSearch = Subject_m.objects.get(subject_id = id)
            CourseData = Course_m.objects.all()
            SemesterData = Semester_m.objects.all()
            BatchData = Batch_m.objects.all()
            SubjectData = Subject_m.objects.all().order_by('-subject_id')
            BaseTemplate = base_template(request)
            context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BatchData' : BatchData, 'SubjectData' : SubjectData , 'SubjectSearch' : SubjectSearch ,'BaseTemplate' : BaseTemplate}
            return render(request, "subject_mgmt.html", context)
        else :
            messages.error(request, "No Record Found For Selected Subject Id!!")
            return redirect("/subject/add")
    else:
        return redirect("/")
