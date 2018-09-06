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
        context['tags'] = False
        return context

    def get_queryset(self):
        return Location.objects.all()

class LocationView(generic.DetailView):
    model = Location
    template_name = 'homesapp/locationview.html'

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
        logger.warning("")
        return result