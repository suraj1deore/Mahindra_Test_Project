from import_export import resources
from .models import ImportData

class ImportDataResources(resources.ModelResource):
    class meta:
        model = ImportData