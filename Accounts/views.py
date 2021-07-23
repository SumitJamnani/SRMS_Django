from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from Accounts.models import ExtendedUser
from django.views.decorators.cache import cache_control
from Batch.models import Batch_m
from Course.models import Course_m
from Division.models import Division_m
from Semester.models import Semester_m
from Subject.models import Subject_m


#For Deciding BaseTemplate
def base_template(request):

        UserRole = ExtendedUser.objects.filter(user_id = request.user.id).values('user_role')
        if UserRole[0]['user_role'] == 'Director':
            BaseTemplate = 'director_panel.html'
        elif UserRole[0]['user_role'] == 'Faculty':
            BaseTemplate = 'faculty_panel.html'
        elif UserRole[0]['user_role'] == 'Student':
            BaseTemplate = 'student_panel.html'
        elif UserRole[0]['user_role'] == 'Admin':
            BaseTemplate = 'admin_panel.html'
        return BaseTemplate



#HomePage View
def home(request):
    BaseTemplate = base_template(request)
    return render(request, 'home.html', {'BaseTemplate' : BaseTemplate})


#Registration View
def register(request):
    CourseData = Course_m.objects.all()
    SemesterData = Semester_m.objects.all()
    BatchData = Batch_m.objects.all()
    SubjectData = Subject_m.objects.all()
    DivisionData = Division_m.objects.all()
    context_reg = {'CourseData' : CourseData, 'SemesterData' : SemesterData, 'DivisionData' : DivisionData, 'BatchData' : BatchData, 'SubjectData' : SubjectData}
    if request.user.is_active:
        BaseTemplate = base_template(request)
        context = {'CourseData' : CourseData, 'SemesterData' : SemesterData, 'DivisionData' : DivisionData, 'BatchData' : BatchData, 'SubjectData' : SubjectData, 'BaseTemplate' : BaseTemplate}
        if request.method == "POST":
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    messages.error(request, "Username Has Already Been Taken!!")
                    if request.user.is_active:
                        return render(request, "add_user.html", context)
                    else:
                        return render(request, "registration.html", context_reg)
                except User.DoesNotExist:
                    user = User.objects.create_user(username = request.POST['username'], email=request.POST['email'], password = request.POST['password1'])
                    user_role = request.POST.get('user_role')
                    name = request.POST.get('name')
                    email = request.POST.get('email')
                    enrollment_number = request.POST.get('enrollment_number',0)
                    course_name = request.POST.get('course_name')
                    semester_name = request.POST.get('semester_name')
                    division_name = request.POST.get('division_name')
                    batch_name = request.POST.get('batch_name')
                    elective_subject = request.POST.get('elective_subject')
                    newextendeduser = ExtendedUser(user_role=user_role,name=name,email=email,enrollment_number=enrollment_number,course_name=course_name,semester_name=semester_name,division_name=division_name,batch_name=batch_name,elective_subject=elective_subject,user=user)
                    newextendeduser.save()
                    if user_role == 'Director':
                        Course_m.objects.filter(course_name=course_name).update(director_id=user)
                    if request.user.is_active:
                        messages.success(request, "User Registered Successfully!!")
                        return render(request, "add_user.html", context)
                    else:
                        return redirect("/accounts/login")
            else:
                messages.error(request, "Password Does Not Matched!!")
                if request.user.is_active:
                    return render(request, "add_user.html", context)
                else:
                    return render(request, "registration.html", context_reg)
        else:
            if request.user.is_active:
                return render(request, "add_user.html", context)
            else:
                return render(request, "registration.html", context_reg)
    else:
        return render(request, 'registration.html', context_reg)



#Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            messages.error(request, "Unsuccessful login. Username or password incorrect.")
            return render(request, "login.html", {})
    else:
        return render(request, "login.html", {})


#Update User Profile
def update_profile(request):
    if request.user.is_active:
        BaseTemplate = base_template(request)
        ProfileData = ExtendedUser.objects.get(user_id = request.user.id)
        context = {'ProfileData' : ProfileData, 'BaseTemplate' : BaseTemplate}
        if request.method == 'POST':
            if request.POST.get('name') != "" and request.POST.get('email') != "" and request.POST.get('password') != "":
                UserPassword = User.objects.get(id=request.user.id)
                UserPassword.set_password(request.POST.get('password'))
                UserPassword.save()
                ExtendedUser.objects.filter(user_id = request.user.id).update(name=request.POST.get('name'), email=request.POST.get('email'))
                messages.success(request, "Profile Updated Successfully!!")
                return render(request, "update_profile.html", context)
            else:
                messages.error(request, "Please Fill All The Required Fields!!")
                return render(request, "update_profile.html", context)
        else:
            return render(request, 'update_profile.html', context)
    else:
        return redirect("/")


#About Developers
def about_us(request):
    if request.user.is_active:
        BaseTemplate = base_template(request)
        return render(request, "about_us.html", {'BaseTemplate' : BaseTemplate})
    else:
        return redirect("/")


#Logout View
@cache_control(no_cache=True, must_revalidate=True)
def logout_view(request):
    logout(request)
    return redirect("/")

