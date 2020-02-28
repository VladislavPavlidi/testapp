from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import RealtorForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from .models import Subdivision, Realtor


def realtor_search(request):
    query = request.GET.get('q')
    Realtors = Realtor.objects.filter(Q(surname=query) | Q(name=query))
    paginator = Paginator(Realtors, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'page': page, 'Realtors': page.object_list}
    return render(request, 'ayax/realtor_list.html', context)


class RealtorEditView(UpdateView):
    model = Realtor
    form_class = RealtorForm
    success_url = reverse_lazy('realtor_check')


class RealtorDeleteView(DeleteView):
    model = Realtor
    form_class = RealtorForm
    success_url = reverse_lazy('realtor_check')


class RealtorCreateView(CreateView):
    template_name = 'ayax/create.html'
    form_class = RealtorForm
    success_url = reverse_lazy('index')


def index(request):
    Subdivisions = Subdivision.objects.order_by('-registered')
    Realtors = Realtor.objects.order_by('-registered')
    context = {'Subdivisions': Subdivisions, 'Realtors': Realtors}
    return render(request, 'ayax/index.html', context)


def realtor_check(request):
    Realtors = Realtor.objects.order_by('-registered')
    paginator = Paginator(Realtors, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'page': page, 'Realtors': page.object_list}
    return render(request, 'ayax/realtor_check.html', context)
