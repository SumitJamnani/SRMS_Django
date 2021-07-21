from django.shortcuts import render, redirect
from Accounts.models import ExtendedUser
from Course.models import Course_m
from Semester.models import Semester_m
from django.contrib import messages


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


#Insert Particular Semester In The Database
def add_semester(request):
    if request.user.is_active:
        CourseData = Course_m.objects.all()
        SemesterData = Semester_m.objects.all().order_by('-semester_id')
        BaseTemplate = base_template(request)
        context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BaseTemplate' : BaseTemplate}

        if request.method == 'POST':
            if request.POST.get('semester_name') != "" and request.POST.get('course_id') is not None:
                semester_name = request.POST.get('semester_name')
                course_id = Course_m.objects.get(course_id=request.POST.get('course_id'))
                SemesterRecord = Semester_m(semester_name=semester_name, course_id=course_id)
                SemesterRecord.save()
                messages.success(request, "Semester Inserted Successfully!!")
                return render(request, "semester_mgmt.html", context)
            else:
                messages.error(request, "Please Fill Required Fields!!")
                return render(request, "semester_mgmt.html", context)
        else:
            BaseTemplate = base_template(request)
            return render(request, "semester_mgmt.html", context)
    else:
        return redirect("/")



def update_semester(request):
    pass


#Delete Particular Course From The Database
def delete_semester(request, id):
    if request.user.is_active:
        if id is not None :
                SemesterSearch = Semester_m.objects.filter(semester_id = id)
                SemesterSearch.delete()
                messages.success(request, "Semester Deleted Successfully!!")
                return redirect("/semester/add")
        else :
            messages.error("No Record Found For Selected Semester Id!!")
            return redirect("/semester/add")
    else:
        return redirect("/")


#Search Particular Semester From The Database
def search_semester(request, id):
    if request.user.is_active:
        if id is not None :
            SemesterSearch = Semester_m.objects.get(semester_id = id)
            CourseData = Course_m.objects.all()
            SemesterData = Semester_m.objects.all().order_by('-semester_id')
            BaseTemplate = base_template(request)
            context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BaseTemplate' : BaseTemplate, 'SemesterSearch'  : SemesterSearch}
            return render(request, "semester_mgmt.html", context)
        else :
            messages.error(request, "No Record Found For Selected Course Id!!")
            return redirect("/semester/add")
    else:
        return redirect("/")
