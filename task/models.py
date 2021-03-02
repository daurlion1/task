from django.db import models
from django_mysql.models import ListTextField


class fill_types(models.Model):
    name = models.TextField()

class fill_type_attributes(models.Model):
    fill_type = models.ForeignKey(fill_types, on_delete=models.CASCADE)
    name = models.TextField()


class areas(models.Model):
    name = models.TextField()
    description = models.TextField()
    points = ListTextField(
        base_field = models.IntegerField(),
        size = 2,
    )
    fill_type = models.ForeignKey(fill_types, on_delete=models.CASCADE)


class area_type_attributes(models.Model):
    area = models.ForeignKey(areas, on_delete=models.CASCADE,related_name='attributes')
    fill_type_attribute = models.ForeignKey(fill_type_attributes, on_delete=models.CASCADE)
    value = models.TextField()

