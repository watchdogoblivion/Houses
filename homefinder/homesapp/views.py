from django.shortcuts import render
from django.views import generic
from .models import Location,Property
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django import template
from django.template.defaultfilters import stringfilter
from functools import reduce
import operator
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = "homesapp/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tags'] = "default"
        return context

    def get_queryset(self):
        return Location.objects.all()

class LocationView(generic.DetailView):
    model = Location
    template_name = 'homesapp/locationview.html'

    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['primary'] = self.kwargs['pk']
        context['price_range'] = "$200,000+"
        context['q_floors'] = ""
        context['q_beds'] = ""
        context['q_baths'] = ""
        return context

class PropertyDetail(generic.DetailView):
    model = Property
    template_name = 'homesapp/propertyview.html'

def home_redirect(request):
    return HttpResponseRedirect("homesapp/")

class IndexSearchView(IndexView):

    paginate_by = 10

    def get_queryset(self):
        result = super(IndexSearchView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                    (Q(location_name__icontains=q) for q in query_list))
            )
        return result

class LocationSearchView(LocationView):

    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(LocationSearchView, self).get_context_data(**kwargs)
        price_range = self.request.GET.get('price_range')
        floors = self.request.GET.get('q_floors')
        beds = self.request.GET.get('q_beds')
        baths = self.request.GET.get('q_baths')
        context['price_range'] = price_range
        context['q_floors'] = floors
        context['q_beds'] = beds
        context['q_baths'] = baths
        return context