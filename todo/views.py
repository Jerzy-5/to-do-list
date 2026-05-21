from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View

from .models import Task, Tag
from .forms import TaskForm, TagForm


class TaskListView(ListView):
    model = Task
    template_name = "todo/home.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all().order_by("is_done", "-created_at")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/form.html"
    success_url = reverse_lazy("home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/form.html"
    success_url = reverse_lazy("home")


class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect("home")


class ToggleTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("home")


class TagListView(ListView):
    model = Tag
    template_name = "todo/tags.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/form.html"
    success_url = reverse_lazy("tags_list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/form.html"
    success_url = reverse_lazy("tags_list")


class TagDeleteView(View):
    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        tag.delete()
        return redirect("tags_list")
