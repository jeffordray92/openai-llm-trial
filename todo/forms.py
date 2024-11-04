from django import forms

from todo.models import Todo
from todo.utils import generate_llm_response


class CreateTodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title']

    def save(self, commit=True):
        instance = super().save(commit=False)

        llm_response = generate_llm_response(instance.title)

        if llm_response:
            instance.llm_response = llm_response
            instance.status = True
        else:
            instance.status = False

        if commit:
            instance.save()
        return instance