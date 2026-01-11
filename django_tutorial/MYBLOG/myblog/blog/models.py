from django.db import models

class blog(model.blog):
    title = models.CharField(max_length(200))
    content = models.TextField()
    author = model.CharField(max_length(100))
    created_at = models.DateTimeField(AUTO_FIELD)
    modified_at = models.DateTimeField(AUTO_FIELD)

    def_
