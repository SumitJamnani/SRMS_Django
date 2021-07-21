from django.contrib import messages
from django.shortcuts import render, redirect
from Accounts.models import ExtendedUser
from Course.models import Course_m
from Division.models import Division_m
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


#Insert Particular Division In The Database
def add_division(request):
    if request.user.is_active:
        CourseData = Course_m.objects.all()
        SemesterData = Semester_m.objects.all()
        DivisionData = Division_m.objects.all().order_by('-division_id')
        BaseTemplate = base_template(request)
        context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'DivisionData' : DivisionData, 'BaseTemplate' : BaseTemplate}

        if request.method == 'POST':
            if request.POST.get('division_name') != "" and request.POST.get('course_id') is not None and request.POST.get('semester_id') is not None:
                division_name = request.POST.get('division_name')
                course_id = Course_m.objects.get(course_id=request.POST.get('course_id'))
                semester_id = Semester_m.objects.get(semester_id=request.POST.get('semester_id'))
                DivisionRecord = Division_m(division_name=division_name, course_id=course_id, semester_id=semester_id)
                DivisionRecord.save()
                messages.success(request, "Division Inserted Successfully!!")
                return render(request, "division_mgmt.html", context)
            else:
                messages.error(request, "Please Fill Required Fields!!")
                return render(request, "division_mgmt.html", context)
        else:
            BaseTemplate = base_template(request)
            return render(request, "division_mgmt.html", context)
    else:
        return redirect("/")


def update_division(request):
    pass


#Delete Particular Division From The Database
def delete_division(request, id):
    if request.user.is_active:
        if id is not None :
                DivisionSearch = Division_m.objects.get(division_id = id)
                DivisionSearch.delete()
                messages.success(request, "Division Deleted Successfully!!")
                return redirect("/division/add")
        else :
            messages.error("No Record Found For Selected Division Id!!")
            return redirect("/division/add")
    else:
        return redirect("/")


#Search Particular Division From The Database
def search_division(request, id):
    if request.user.is_active:
        if id is not None :
            DivisionSearch = Division_m.objects.get(division_id = id)
            CourseData = Course_m.objects.all()
            SemesterData = Semester_m.objects.all()
            DivisionData = Division_m.objects.all().order_by('-division_id')
            BaseTemplate = base_template(request)
            context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'DivisionData' : DivisionData, 'BaseTemplate' : BaseTemplate, 'DivisionSearch' : DivisionSearch}
            return render(request, "division_mgmt.html", context)
        else :
            messages.error(request, "No Record Found For Selected Batch Id!!")
            return redirect("/division/add")
    else:
        return redirect("/")
