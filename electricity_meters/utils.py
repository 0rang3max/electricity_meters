from django.db import models
from django.db.models import Func

class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.DecimalField()
