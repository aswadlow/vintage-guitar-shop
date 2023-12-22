from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guitar, Review, Pedal
from .forms import ReviewForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all() 
    return render(request, 'guitars/index.html', 
    { 
        'guitars': guitars
    })

def guitar_detail(request, guitar_id):
  guitar = Guitar.objects.get(id=guitar_id)
  id_list = guitar.pedals.all().values_list('id')
  no_pedals = Pedal.objects.exclude(id__in=id_list)
  reviews = Review.objects.filter(guitar=guitar_id)
  print (f'{reviews}')
  review_form = ReviewForm()
  return render(request, 'guitars/detail.html', { 
     'guitar': guitar,
     'review_form': review_form,
     'reviews': reviews,
     'pedals': no_pedals
     })

class GuitarCreate(CreateView):
    model = Guitar
    fields = '__all__'

class GuitarUpdate(UpdateView):
  model = Guitar
  fields = ['price']

class GuitarDelete(DeleteView):
  model = Guitar
  success_url = '/guitars'

def add_review(request, guitar_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.guitar_id = guitar_id
        new_review.save()
    return redirect('detail', guitar_id=guitar_id)

class PedalList(ListView):
   model = Pedal

class PedalDetail(DetailView):
   model = Pedal

class PedalCreate(CreateView):
   model = Pedal
   fields = ['name', 'effect']

class PedalUpdate(UpdateView):
  model = Pedal
  fields = ['name', 'effect']

class PedalDelete(DeleteView):
   model = Pedal
   success_url = '/pedals'

def assoc_pedal(request, guitar_id, pedal_id):
  Guitar.objects.get(id=guitar_id).pedals.add(pedal_id)
  return redirect('detail', guitar_id=guitar_id)

def unassoc_pedal(request, guitar_id, pedal_id):
  Guitar.object.get(id=guitar_id).pedals.remove(pedal_id)
  return redirect('detail', guitar_id=guitar_id)