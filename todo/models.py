from django.db import models


optional = {
	"blank": True,
	"null": True
}

class Todo(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    llm_response = models.TextField(**optional)

    def __str__(self):
        return self.title