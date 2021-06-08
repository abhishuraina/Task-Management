from django.shortcuts import render

def project_list(request):
    return render(request, 'frontend/project_list.html')

def project_detail(request,id):
    return render(request, 'frontend/project_detail.html')

def task_detail(request, id):
    return render(request, 'frontend/task_detail.html')

def task_edit(request, id, pk):
    return render(request, 'frontend/task_edit.html')
