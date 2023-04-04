from django.db import models


class Category(models.Model):
    """ Category Model """
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
