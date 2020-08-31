# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TKjv(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key = True)
    b = models.IntegerField(blank=True, null=True)
    c = models.IntegerField(blank=True, null=True)
    v = models.IntegerField(blank=True, null=True)
    t = models.TextField(blank=True, null=True)
    book = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 't_kjv'
