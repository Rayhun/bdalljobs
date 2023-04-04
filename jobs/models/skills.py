from django.db import models


class Skill(models.Model):
    '''
        Skill Model
    '''
    skill_name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['skill_name']

    def save(self, *args, **kwargs):
        if self.skill_name:
            self.skill_name = self.skill_name.title()
        super(Skill, self).save(*args, **kwargs)

    def __str__(self):
        return self.skill_name
