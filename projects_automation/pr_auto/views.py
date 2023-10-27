from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from form.form import Project_Registration_Form
from pr_auto.models import Student


def sign_up(request):
    if request.method == "POST":
        form = Project_Registration_Form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            call_time = form.cleaned_data['available_time']
            project_weeks = form.cleaned_data['project_weeks']
            try:
                student = Student.objects.get(email=email)
                if student.registration_status is False:
                    student.call_time = call_time
                    student.project_week = project_weeks
                    student.registration_status = True
                    student.save()
                    return HttpResponse('Регистрация на проект выполнена успешно!')
                else:
                    return HttpResponse('Вы уже зарегистрированы!')
            except Student.DoesNotExist:
                return HttpResponse('Студент не найден')

    form = Project_Registration_Form()
    return render(request, 'base.html', {'form': form})
