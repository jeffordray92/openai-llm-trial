from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from todo.models import Todo
from todo.forms import CreateTodoForm


class TodoView(ListView, FormView):
    model = Todo
    template_name = 'todo_page.html'
    context_object_name = 'todos'
    form_class = CreateTodoForm
    success_url = reverse_lazy('todo_view')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)