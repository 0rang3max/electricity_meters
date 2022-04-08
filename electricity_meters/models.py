from datetime import date, timedelta
from decimal import Decimal
from multiprocessing.dummy import current_process

from django.db import models


class ElectricityMeter(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date_start = models.DateField(default=date.today)

    def __str__(self) -> str:
        return self.name
    
    @property
    def measurements_query(self):
        return self.measurements.order_by('date')

    @property
    def avg_consumption(self):
        if not (last_measurement := self.measurements_query.last()):
            return Decimal('0.00')
        return round(last_measurement.value / (last_measurement.date - self.date_start).days, 2)

    @property
    def current_value(self):
        if not (last_measurement := self.measurements_query.last()):
            return Decimal('0.00')
        if last_measurement.date == date.today():
            return last_measurement.value
        return ((date.today() - last_measurement.date).days * self.avg_consumption) + last_measurement.value

    @property
    def graph_data(self):
        if not self.current_value:
            return
        
        queryset = self.measurements_query.values_list('date__month', 'date__year').annotate(models.Avg('value'))
        
        return {
            'labels': [
                f'{self.date_start.month}.{self.date_start.year}', 
                *[f'{item[0]}.{item[1]}' for item in queryset],
                f'{date.today().month}.{date.today().year}',
            ],
            'current_dataset': [0, *[item[2] for item in queryset], self.current_value],
            'avg_dataset': [0, *[None for _ in range(len(queryset))], self.current_value],
        }



class Measurement(models.Model):
    electricity_meter = models.ForeignKey(
        ElectricityMeter,
        related_name='measurements',
        related_query_name='measurement',
        on_delete=models.CASCADE,
    )
    date = models.DateField(default=date.today, null=False)
    value = models.DecimalField(max_digits=7, decimal_places=2, null=False)

    def __str__(self) -> str:
        return f'{self.electricity_meter.name} {self.date}'
