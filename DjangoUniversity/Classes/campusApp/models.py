from django.db import models

class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_Id = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    def __str__(self):
        return self.campus_name

    class Meta:
        verbose_name_plural = "University Campus"
