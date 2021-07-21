from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Accounts.models import ExtendedUser
from Batch.models import Batch_m
from Course.models import Course_m
from Exam.models import Exam_m
from Result.models import Result_m
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


#Insert Particular Result In The Database
def add_result(request):
    if request.user.is_active:
        CourseData = Course_m.objects.all()
        SemesterData = Semester_m.objects.all()
        BatchData = Batch_m.objects.all()
        UserData = ExtendedUser.objects.all()
        SubjectData = Subject_m.objects.all()
        ExamData = Exam_m.objects.all()
        PassingMarks = Exam_m.objects.filter(exam_id = request.POST.get('exam_id')).values('passing_marks')
        ResultData = Result_m.objects.all().order_by('-result_id')
        BaseTemplate = base_template(request)
        context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BatchData' : BatchData, 'UserData' : UserData, 'SubjectData' : SubjectData, 'ExamData' : ExamData, 'ResultData' : ResultData, 'BaseTemplate' : BaseTemplate}

        if request.method == 'POST':
            if request.POST.get('enrollment_number') != "" and request.POST.get('marks_obtained') != "" and request.POST.get('course_id') is not None and request.POST.get('semester_id') is not None and request.POST.get('subject_id') is not None and request.POST.get('exam_id') is not None:
                course_id = Course_m.objects.get(course_id=request.POST.get('course_id'))
                batch_id = Batch_m.objects.get(semester_id=request.POST.get('batch_id'))
                semester_id = Semester_m.objects.get(semester_id=request.POST.get('semester_id'))
                faculty_id = User.objects.get(id=request.POST.get('faculty_id'))
                subject_id = Subject_m.objects.get(subject_id=request.POST.get('subject_id'))
                exam_id = Exam_m.objects.get(exam_id=request.POST.get('exam_id'))
                enrollment_number = request.POST.get('enrollment_number')
                marks_obtained = request.POST.get('marks_obtained')
                if Decimal(marks_obtained) >= PassingMarks[0]['passing_marks']:
                    status = 'Pass'
                elif Decimal(marks_obtained) < PassingMarks[0]['passing_marks']:
                    status = 'Fail'
                ResultRecord = Result_m(course_id=course_id, semester_id=semester_id, batch_id=batch_id, faculty_id=faculty_id, subject_id=subject_id, exam_id=exam_id, enrollment_number=enrollment_number, marks_obtained=marks_obtained, status=status)
                ResultRecord.save()
                messages.success(request, "Result Declared Successfully For Given Enrollment Number!!")
                return render(request, "manual_result.html", context)
            else:
                messages.error(request, "Please Fill Required Fields!!")
                return render(request, "manual_result.html", context)
        else:
            BaseTemplate = base_template(request)
            return render(request, "manual_result.html", context)
    else:
        return redirect("/")


#View Particular Exam's Result Report
def reports(request):
    if request.user.is_active:
        CourseData = Course_m.objects.all()
        SemesterData = Semester_m.objects.all()
        BatchData = Batch_m.objects.all()
        UserData = ExtendedUser.objects.all()
        SubjectData = Subject_m.objects.all()
        ExamData = Exam_m.objects.all()
        BaseTemplate = base_template(request)
        context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BatchData' : BatchData, 'UserData' : UserData, 'SubjectData' : SubjectData, 'ExamData' : ExamData, 'BaseTemplate' : BaseTemplate}

        if request.method == 'POST':
            if request.POST.get('enrollment_number') != "" and request.POST.get('marks_obtained') != "" and request.POST.get('course_id') is not None and request.POST.get('semester_id') is not None and request.POST.get('subject_id') is not None and request.POST.get('exam_id') is not None:
                course_id = Course_m.objects.get(course_id=request.POST.get('course_id'))
                batch_id = Batch_m.objects.get(semester_id=request.POST.get('batch_id'))
                semester_id = Semester_m.objects.get(semester_id=request.POST.get('semester_id'))
                faculty_id = User.objects.get(id=request.POST.get('faculty_id'))
                subject_id = Subject_m.objects.get(subject_id=request.POST.get('subject_id'))
                exam_id = Exam_m.objects.get(exam_id=request.POST.get('exam_id'))
                ReportData = Result_m.objects.filter(course_id=course_id, subject_id=subject_id, exam_id=exam_id).order_by('result_id')
                ExamCommonData = Result_m.objects.filter(course_id=course_id, subject_id=subject_id, exam_id=exam_id).first()
                context = {'SemesterData' : SemesterData, 'CourseData' : CourseData, 'BatchData' : BatchData, 'UserData' : UserData, 'SubjectData' : SubjectData, 'ExamData' : ExamData, 'ExamCommonData' : ExamCommonData, 'ReportData' : ReportData, 'BaseTemplate' : BaseTemplate}
                return render(request, "report.html", context)
            else:
                messages.error(request, "Please Select Correct options for Generate Reports!!")
                return render(request, "report.html", context)
        else:
            return render(request, "report.html", context)
    else:
        return redirect("/")


# For Generating Particular Student's Result
def student_result(request):
    if request.user.is_active:
        SubjectData = Subject_m.objects.all()
        ExamData = Exam_m.objects.all()
        enrollment_number = ExtendedUser.objects.filter(user_id = request.user.id).values('enrollment_number','name')
        semester_name = ExtendedUser.objects.filter(user_id = request.user.id).values('semester_name')
        semester_id = Semester_m.objects.filter(semester_name = semester_name[0]['semester_name']).values('semester_id')
        print(semester_id)
        context = {'SubjectData' : SubjectData, 'ExamData' : ExamData}
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            exam_id = request.POST.get('exam_id')
            ResultData = Result_m.objects.filter(enrollment_number=enrollment_number[0]['enrollment_number'], semester_id=semester_id[0]['semester_id'], subject_id=subject_id, exam_id=exam_id)
            ExamInfo = Exam_m.objects.filter(exam_id=exam_id)
            context = {'SubjectData' : SubjectData, 'ExamData' : ExamData, 'ExamInfo' : ExamInfo, 'ResultData' : ResultData, 'StudentName' : enrollment_number[0]['name']}
            return render(request, "student_result.html", context)
        else:
            return render(request, "student_result.html", context)
    else:
        return redirect("/")







