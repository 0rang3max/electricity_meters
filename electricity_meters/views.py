from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from electricity_meters.models import ElectricityMeter


def items_list(request):
    template = loader.get_template('electricity_meters/list.html')
    return HttpResponse(template.render({
        'electricity_meters': ElectricityMeter.objects.all().order_by('date_start')
    }, request))


def item_detail(request, pk):
    template = loader.get_template('electricity_meters/item.html')
    electricity_meter = get_object_or_404(ElectricityMeter, pk=pk)
    return HttpResponse(template.render({
        'electricity_meter': electricity_meter,
    }, request))
