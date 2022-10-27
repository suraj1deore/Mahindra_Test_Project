from django.db import models

# This class stores data from input files.
Category = (
    ("A", "A"),
    ("B","B"),
    ("C","C"),
)
class ImportData(models.Model):
    category = models.CharField(max_length = 10, choices = Category)
    X = models.IntegerField()
    Y = models.IntegerField()
    created = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "Export"