from django.db import models
from django.db.models.query import QuerySet

class QuestionQuerySet(QuerySet):
    def active(self):
        """
        Return only "active" (i.e. published) questions.
        """
        return self.filter(status__exact=self.model.ACTIVE)

class QuestionManager(models.Manager):
    def get_queryset(self):
        return QuestionQuerySet(self.model)
    get_query_set = get_queryset# backwards compatibility. see https://docs.djangoproject.com/en/1.6/releases/1.6/

    def active(self):
        return self.get_queryset().active()