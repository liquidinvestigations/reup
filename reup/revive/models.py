from django.db import models


class Document(models.Model):
    old_id = models.IntegerField()
    md5 = models.CharField(max_length=40, blank=True, db_index=True)
    sha1 = models.CharField(max_length=50, blank=True, db_index=True)
