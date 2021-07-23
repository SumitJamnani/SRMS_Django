from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Accounts.models import ExtendedUser
from Batch.models import Batch_m
from Course.models import Course_m
from Exam.models import Exam_m
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


#Insert Particular Exam In The Database
def add_exam(request):
    if request.user.is_active:
        CourseData = Course_m.objects.all()
        SemesterData = Semester_m.objects.all()
        BatchData = Batch_m.objects.all()
        UserData = ExtendedUser.objects.all()
        SubjectData = Subject_m.objects.all()
        ExamData = Exam_m.objects.all().order_by('-exam_id')
        BaseTemplate = base_template(request)
        context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BatchData' : BatchData, 'UserData' : UserData, 'SubjectData' : SubjectData, 'ExamData' : ExamData, 'BaseTemplate' : BaseTemplate}

        if request.method == 'POST':
            if request.POST.get('exam_name') != "" and request.POST.get('total_marks') != "" and request.POST.get('course_id') is not None and request.POST.get('semester_id') is not None and request.POST.get('subject_id') is not None:
                exam_name = request.POST.get('exam_name')
                total_marks = request.POST.get('total_marks')
                passing_marks = request.POST.get('passing_marks')
                exam_date = request.POST.get('exam_date')
                course_id = Course_m.objects.get(course_id=request.POST.get('course_id'))
                semester_id = Semester_m.objects.get(semester_id=request.POST.get('semester_id'))
                batch_id = Batch_m.objects.get(batch_id=request.POST.get('batch_id'))
                faculty_id = User.objects.get(id=request.POST.get('faculty_id'))
                subject_id = Subject_m.objects.get(subject_id=request.POST.get('subject_id'))
                ExamRecord = Exam_m(exam_name=exam_name, total_marks=total_marks, passing_marks=passing_marks, exam_date=exam_date, course_id=course_id, semester_id=semester_id, batch_id=batch_id, faculty_id=faculty_id, subject_id=subject_id)
                ExamRecord.save()
                messages.success(request, "Exam Declared Successfully!!")
                return render(request, "exam_mgmt.html", context)
            else:
                messages.error(request, "Please Fill Required Fields!!")
                return render(request, "exam_mgmt.html", context)
        else:
            BaseTemplate = base_template(request)
            return render(request, "exam_mgmt.html", context)
    else:
        return redirect("/")



def update_exam(request):
    pass


#Delete Particular Exam From The Database
def delete_exam(request, id):
    if request.user.is_active:
        if id is not None :
                ExamSearch = Exam_m.objects.get(exam_id = id)
                ExamSearch.delete()
                messages.success(request, "Exam Deleted Successfully!!")
                return redirect("/exam/add")
        else :
            messages.error("No Record Found For Selected Exam Id!!")
            return redirect("/exam/add")
    else:
        return redirect("/")


#Search Particular Exam From The Database
def search_exam(request, id):
    if request.user.is_active:
        if id is not None :
            ExamSearch = Exam_m.objects.get(exam_id = id)
            CourseData = Course_m.objects.all()
            SemesterData = Semester_m.objects.all()
            BatchData = Batch_m.objects.all()
            SubjectData = Subject_m.objects.all()
            UserData = ExtendedUser.objects.all()
            ExamData = Exam_m.objects.all().order_by('-exam_id')
            BaseTemplate = base_template(request)
            context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BatchData' : BatchData, 'UserData' : UserData, 'SubjectData' : SubjectData, 'ExamData' : ExamData, 'ExamSearch' : ExamSearch, 'BaseTemplate' : BaseTemplate}
            return render(request, "exam_mgmt.html", context)
        else :
            messages.error(request, "No Record Found For Selected Exam Id!!")
            return redirect("/exam/add")
    else:
        return redirect("/")
