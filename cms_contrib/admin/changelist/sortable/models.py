from django.db import models

class SortableChangeListMixin(models.Model):
    ordering = models.PositiveIntegerField(default=0)
            
    class Meta:
        ordering = ["-ordering"]