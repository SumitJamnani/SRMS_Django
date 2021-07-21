from django.shortcuts import render, redirect
from Course.models import Course_m
from Accounts.models import ExtendedUser
from django.contrib import messages
from django.contrib.auth.models import User

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


#Insert Particular Course In The Database
def add_course(request):
    if request.user.is_active:
        UserData = ExtendedUser.objects.all()
        CourseData = Course_m.objects.all().order_by('-course_id')
        if request.method == 'POST':
            if request.POST.get('course_name') != "" and request.POST.get('director_id') is not None:
                try:
                    course = Course_m.objects.get(course_name=request.POST.get('course_name'))
                    messages.error(request, "Course Already Declared!!")
                    return render(request, "course_mgmt.html", context = {'UserData' : UserData, 'CourseData' : CourseData})
                except:
                    course_name = request.POST.get('course_name')
                    director_id = User.objects.get(id=request.POST.get('director_id'))
                    CourseRecord = Course_m(course_name=course_name, director_id=director_id)
                    CourseRecord.save()
                    messages.success(request, "Course Inserted Successfully!!")
                    return render(request, "course_mgmt.html", context = {'UserData' : UserData, 'CourseData' : CourseData})
            else:
                messages.error(request, "Please Fill Required Fields!!")
                return render(request, "course_mgmt.html", context = {'UserData' : UserData, 'CourseData' : CourseData})
        else:
            BaseTemplate = base_template(request)
            return render(request, "course_mgmt.html", context = {'UserData' : UserData, 'CourseData' : CourseData, 'BaseTemplate' : BaseTemplate})
    else:
        return redirect("/")


#Update Particular Course From The Database
def update_course(request, id):
    if request.user.is_active:
        if 'course_name' in request.GET:
            print(request.POST.get('course_name'))
        else:
            print('nahi mila bhai data')
        if request.method == 'GET':
            director_names = User.objects.all
            course_data = Course_m.objects.all().order_by('-course_id')
            if id is not None :
                if request.POST.get('course_name') != "" and request.POST.get('director_id') is not None:
                    try:
                        course = Course_m.objects.get(course_name=request.POST.get('course_name'))
                        messages.error(request, "Course Already Declared!!")
                        return redirect("/course/add")
                    except:
                        course_name = request.POST.get('course_name')
                        director_id = User.objects.get(id=request.POST.get('director_id'))
                        CourseRecord = Course_m(course_name=course_name, director_id=director_id)
                        CourseRecord.save()
                        messages.success(request, "Course Updated Successfully!!")
                        return redirect("/course/add")
                else:
                    messages.error(request, "Please Fill Required Fields!!")
                    return redirect("/course/add")
            else :
                messages.error("No Record Found For Selected Course Id!!")
                return redirect("/course/add")
        else:
            return redirect("/course/add")
    else:
        return redirect("/")


#Delete Particular Course From The Database
def delete_course(request, id):
    if request.user.is_active:
        if id is not None :
                CourseSearch = Course_m.objects.filter(course_id = id)
                CourseSearch.delete()
                messages.success(request, "Course Deleted Successfully!!")
                return redirect("/course/add")
        else :
            messages.error("No Record Found For Selected Course Id!!")
            return redirect("/course/add")
    else:
        return redirect("/")


#Search Particular Course From The Database
def search_course(request, id):
    if request.user.is_active:
        UserData = ExtendedUser.objects.all()
        CourseData = Course_m.objects.all().order_by('-course_id')
        if id is not None :
            CourseSearch = Course_m.objects.get(course_id = id)
            return render(request, "course_mgmt.html", context = {'UserData' : UserData, 'CourseData' : CourseData, 'CourseSearch' : CourseSearch})
        else :
            messages.error(request, "No Record Found For Selected Course Id!!")
            return redirect("/course/add")
    else:
        return redirect("/")
