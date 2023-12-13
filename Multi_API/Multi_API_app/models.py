from django.db import models


class Schooling(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    tenth = models.FloatField()
    twelveth = models.FloatField()

    class Meta:
        managed = False
        db_table = 'schooling'


class Graduation(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    sem1 = models.FloatField(blank=True, null=True)
    sem2 = models.FloatField(blank=True, null=True)
    sem3 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'graduation'
