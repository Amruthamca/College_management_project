import os
from django.shortcuts import render,redirect
from clg_mng_app.models import Course
from clg_mng_app.models import Student
from clg_mng_app.models import Teacher
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate

# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    courses=Course.objects.all()
    return render(request,'signup.html',{'course':courses})


def adminhome(request):
    return render(request,'admin_home.html')


def addcourse(request):
    return render(request,'add_course.html')

def addstudent(request):
    return render(request,'add_student.html')


def add_coursedb(request):
    if request.method=='POST':
        course_name=request.POST.get('cname')
        course_fee=request.POST.get('cfee')
        course=Course(course_name=course_name,fee=course_fee)
        course.save()
        return redirect('adminhome')
    
def add_student(request):
    courses=Course.objects.all()
    return render(request,'add_student.html',{'course':courses})

def add_studentdb(request):
    if request.method=='POST':
        student_name=request.POST['sname']
        student_address=request.POST['address']
        age=request.POST['age']
        jdate=request.POST['date']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student=Student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        student.save()
        return redirect('adminhome')
    

def show_details(request):
    student=Student.objects.all()
    return render(request,'view_student.html',{'students':student})

def edit(request,pk):
    student=Student.objects.get(id=pk)
    course=Course.objects.all()
    return render(request,'edit_student.html',{'stud':student,'course':course})


def editdb(request,pk):
    if request.method=='POST':
        student=Student.objects.get(id=pk)
        student.student_name=request.POST['sname']
        student.student_address=request.POST['address']
        student.student_age=request.POST['age']
        student.joining_date=request.POST['date']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student.course=course1
        student.save()
        return redirect('show_details')
    return render(request,'edit_student.html')


def delete(request,pk):
    stud=Student.objects.get(id=pk)
    stud.delete()
    return redirect('show_details')

def add_teacher(request):
    if request.method == 'POST':
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        uname = request.POST['userName']
        pswd = request.POST['password']
        cpswd = request.POST['confirmPassword']
        addr = request.POST['address']
        ag = request.POST['age']
        email = request.POST['email']
        number = request.POST['contactNumber']
        sel = request.POST['course']
        img = request.FILES.get('photo')  

        if pswd == cpswd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'This username already exists!!!!')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    email=email,
                    password=pswd
                )
                user.save()
                course2=Course.objects.get(id=sel)
                u=User.objects.get(id=user.id)
                reg=Teacher.objects.create(
                    address=addr,
                    age=ag,
                    contact=number,
                    course=course2,
                    img=img,
                    user=u
                )
                reg.save()
                return redirect('home')
        else:
            messages.info(request, 'Password doesnt match')
            return redirect('signup')
    return render(request, 'home.html') 


def adminlogin(request):
    if request.method == "POST":
        username=request.POST['uname']
        password=request.POST['pswd']  
        user=authenticate(username=username, password=password)  
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('adminhome')
            else:
                login(request, user)
                #messages.info(request, f'Welcome {username}')
                return redirect('teacher_home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    return render(request, 'home.html')

def logout1(request):
    auth.logout(request)
    return redirect('home')

def show_teacher(request):
    teachers = Teacher.objects.all()  
    return render(request, 'view_teachers.html', {'teachers': teachers})

def delete_teacher(request,pk):
    teach=Teacher.objects.get(user_id=pk)
    user1=User.objects.get(id=pk)
    teach.delete()
    user1.delete()
    return redirect('show_teacher')

def teacher_home(request):
    return render(request,'teacher_home.html')

def profile(request):
    current_user=request.user.id
    user2=Teacher.objects.get(user_id=current_user)
    return render(request,'profile.html',{'users':user2})

def edit_teacher(request):
    teacher=Teacher.objects.get(user=request.user)
    courses=Course.objects.all()
    return render(request,'edit_teacher.html',{'teach':teacher,'course':courses})

def edit_details_tchr(request,pk):
    if request.method=='POST':
        teacher=Teacher.objects.get(user=pk)
        user=User.objects.get(id=pk)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.username=request.POST['uname']
        user.email=request.POST['email']
        teacher.address=request.POST['addr']
        teacher.age=request.POST['age']
        teacher.contact=request.POST['cnum']
        courseid=request.POST['sel']
        course=Course.objects.get(id=courseid)
        teacher.course=course
        if len(request.FILES)!=0:
            if len(teacher.img)>0:
                os.remove(teacher.img.path)
            teacher.img=request.FILES.get('img')
        teacher.save()
        user.save()
        messages.success(request,'Details updated successfully')
        return redirect('profile')

