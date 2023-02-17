from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import NewTask, UpdateTask
from .models import Tasks

# Create your views here.


def home_page(request):
    if request.method == "POST":
        if request.POST.get("myInput") == "lazvi":
            add_form = NewTask(request.POST)
            if add_form.is_valid():
                new_task = Tasks(title=add_form.cleaned_data["new_task"])
                new_task.save()
                return HttpResponseRedirect(reverse("home-page"))
        
        if request.POST.get("myInput") == "chincho":
            update_form = UpdateTask(request.POST)
            if update_form.is_valid():
                update_task = update_form.cleaned_data["updated_task"]
                update_id = request.POST.get("my_task")
                task = Tasks.objects.get(id=update_id)
                task.title = update_task
                task.save()
                return HttpResponseRedirect(reverse("home-page"))
    else:
        add_form = NewTask()
        update_form = UpdateTask()
    all_tasks = Tasks.objects.all()
    
    return render(request, "to_do/index.html", {
        "form": add_form,
        "update_form": update_form,
        "tasks": all_tasks
    })


def delete_page(request, id):
    task = Tasks.objects.get(id=id)
    task.delete()
    dynamic_url = reverse("home-page")
    return HttpResponseRedirect(dynamic_url)
