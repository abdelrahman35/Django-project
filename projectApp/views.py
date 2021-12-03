from django.http.response import HttpResponseBase
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from projectApp import models
from .forms import ProjectAddForm , AddCommentForm
# Create your views here.
from .models import Projects , Projectcomments


def AddProject(request):
    form = ProjectAddForm()
    if request.method == "POST":
        form = ProjectAddForm(request.POST)
        if form.is_valid():
            myform = form.save()
            myform.user = request.user
            myform.save()
            return redirect('viewprojects')
    return render(request, 'project/Addproject.html', {'form':form})

def viewproject(request):
    projectslist = Projects.objects.all()

    return render(request, 'project/viewproject.html', {'projectslist': projectslist})


def projectDetails(request,id):
    detailOfProject = Projects.objects.filter(project_id=id)

    return render(request,'project/showproject.html',{'detailOfProject':detailOfProject})


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
def viewComments(request, project_id):
    comment = Projectcomments.objects.filter(project_id__projectcomments=project_id)
    return render(request, 'project/showproject.html', {'comment':comment})
    '''

def viewComments(request):
    comment = Projectcomments.objects.all()
    return render(request, 'project/viewComment.html', {'comment':comment})
#
# def CommentAddView(request):
#     form = AddCommentForm()
#     if request.method == "POST":
#         form = AddCommentForm(request.POST)
#         if form.is_valid():
#             commentform = form.save()
#             commentform.user = request.user
#             commentform.save()
#             return redirect('projectDetails')
#     return render(request, 'project/showproject.html', {'form': form})
#
#
# def AddcommentHTML(request):
#     if(request.method=='GET'):
#
#         return render(request, 'base.html',{})
#     else:
#         print(request.POST)
#         #create student object
#         comment =Projectcomments.objects.create(comment=request.POST['comment'],project_id_id=request.POST['project_id'])
#         if (comment):
#             return render(request, 'project/showproject.html', {'msg': 'Student is added '})
#         else:
#             return render(request, 'base.html', {'msg':'Error' })

