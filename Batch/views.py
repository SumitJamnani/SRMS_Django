from django.contrib import messages
from django.shortcuts import render, redirect
from Accounts.models import ExtendedUser
from Batch.models import Batch_m
from Course.models import Course_m
from Semester.models import Semester_m


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
def add_batch(request):
    if request.user.is_active:
        CourseData = Course_m.objects.all()
        SemesterData = Semester_m.objects.all()
        BatchData = Batch_m.objects.all().order_by('-batch_id')
        BaseTemplate = base_template(request)
        context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BatchData' : BatchData, 'BaseTemplate' : BaseTemplate}

        if request.method == 'POST':
            if request.POST.get('batch_name') != "" and request.POST.get('course_id') is not None and request.POST.get('semester_id') is not None:
                batch_name = request.POST.get('batch_name')
                course_id = Course_m.objects.get(course_id=request.POST.get('course_id'))
                semester_id = Semester_m.objects.get(semester_id=request.POST.get('semester_id'))
                BatchRecord = Batch_m(batch_name=batch_name, course_id=course_id, semester_id=semester_id)
                BatchRecord.save()
                messages.success(request, "Batch Inserted Successfully!!")
                return render(request, "batch_mgmt.html", context)
            else:
                messages.error(request, "Please Fill Required Fields!!")
                return render(request, "batch_mgmt.html", context)
        else:
            BaseTemplate = base_template(request)
            return render(request, "batch_mgmt.html", context)
    else:
        return redirect("/")


def update_batch(request):
    pass


#Delete Particular Batch From The Database
def delete_batch(request, id):
    if request.user.is_active:
        if id is not None :
                BatchSearch = Batch_m.objects.get(batch_id = id)
                BatchSearch.delete()
                messages.success(request, "Batch Deleted Successfully!!")
                return redirect("/batch/add")
        else :
            messages.error("No Record Found For Selected Semester Id!!")
            return redirect("/batch/add")
    else:
        return redirect("/")


#Search Particular Batch From The Database
def search_batch(request, id):
    if request.user.is_active:
        if id is not None :
            BatchSearch = Batch_m.objects.get(batch_id = id)
            CourseData = Course_m.objects.all()
            SemesterData = Semester_m.objects.all()
            BatchData = Batch_m.objects.all().order_by('-batch_id')
            BaseTemplate = base_template(request)
            context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BatchData' : BatchData, 'BaseTemplate' : BaseTemplate, 'BatchSearch' : BatchSearch}
            return render(request, "batch_mgmt.html", context)
        else :
            messages.error(request, "No Record Found For Selected Batch Id!!")
            return redirect("/batch/add")
    else:
        return redirect("/")


def batch_semester_update(request):
    if request.user.is_active:
        CourseData = Course_m.objects.all()
        SemesterData = Semester_m.objects.all()
        BatchData = Batch_m.objects.all()
        BaseTemplate = base_template(request)
        context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BatchData' : BatchData,  'BaseTemplate' : BaseTemplate}
        if request.method == 'POST':
            course_name = request.POST.get('course_name')
            batch_name = request.POST.get('batch_name')
            semester_name = request.POST.get('semester_name')
            if course_name is not None and batch_name is not None and semester_name is not None:
                ExtendedUser.objects.filter(course_name=course_name,batch_name=batch_name).update(semester_name=semester_name)
                messages.success(request, "Semester Updated Successfully!!")
                return render(request, "semester_update.html", context)
            else:
                messages.error(request, "Please Select Correct options!!")
                return render(request, "semester_update.html", context)
        else:
            return render(request, "semester_update.html", context)
    else:
        return redirect("/")
