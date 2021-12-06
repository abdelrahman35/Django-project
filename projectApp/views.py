from django.http.response import HttpResponseBase
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from projectApp import models
from .forms import ProjectAddForm , AddCommentForm ,AddReportForm ,Commentsreport
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, generics
from .api import Studentser
from .models import Projects , Projectcomments

# Create your views here.

@login_required
def AddProject(request):
    form = ProjectAddForm()
    if request.method == "POST":
        form = ProjectAddForm(request.POST or None)
        if form.is_valid():
            myform = form.save()
            myform.user = request.user
            myform.save()
            return redirect('viewprojects')
    return render(request, 'project/Addproject.html', {'form':form})
@login_required
def viewproject(request):
    projectslist = Projects.objects.all()

    return render(request, 'project/viewproject.html', {'projectslist': projectslist})

@login_required
def projectDetails(request,id):
    detailOfProject = Projects.objects.filter(project_id=id)
    commentsOnproject = Projectcomments.objects.filter(project_id = id)
    form = AddCommentForm()
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            myform = form.save()
            myform.user = request.user
            myform.save()
    return render(request,'project/showproject.html',{'detailOfProject':detailOfProject, 'commentsOnproject':commentsOnproject,'form':form})


class ApiStudent(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = Studentser


@login_required
def viewComments(request):
    comment = Projectcomments.objects.all()
    return render(request, 'project/viewComment.html', {'comment':comment})
@ login_required
def AddReportView(request):
    forms = AddReportForm()
    if request.method == "POST":
        forms = AddReportForm(request.POST)
        if forms.is_valid():
            myforms= forms.save()
            myforms.user = request.user
            myforms.save()
            return redirect('viewprojects')
    return render(request, 'project/AddReport.html', {'forms': forms})
@login_required
def viewReports(request):
    report = Commentsreport.objects.all()
    return render(request, 'project/viewReport.html', {'report':report})


def viewLatest(request):
    latestProjects = Projects.objects.all().order_by('-project_id')[:5][::-1]
   

    highestRate = Projects.objects.filter(
    avg_rate__gte=Projects.objects.order_by('-avg_rate')[4].avg_rate
)
    print(highestRate)

    return render(request, 'project/home.html', {'latestProjects': latestProjects, 'highestRate':highestRate})


def highestRate(request):
    highestRate = Projects.objects.all().aggregate(max("Avg_rate"))[:5]

    print(highestRate)
    # for i in viewavr:
    #     print(i.Avg_rate)
    dataproject = Projects.objects.all()

    return render(request, 'project/viewproject.html', {'data': dataproject,'highestRate':highestRate})



    # hash
    '''
@login_required
def AddCommentView(request):
    form = AddCommentForm()
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            myform = form.save()
            myform.user = request.user
            myform.save()
            return redirect('viewprojects')
    return render(request, 'project/AddComment.html', {'form': form})
'''