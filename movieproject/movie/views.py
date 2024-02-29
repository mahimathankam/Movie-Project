from django.shortcuts import render
from movie.models import Movie
from movie.forms import Movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# def addmovie(request):
#     if(request.method=='POST'):
#         form=Movieform(request.POST,request.FILES)
#         if(form.is_valid()):
#             form.save()
#             return viewmovie(request)
#     form=Movieform()
#     return render(request,template_name='addmovie.html',context={'form':form})

class MovieAdd(CreateView):
    model=Movie
    template_name = 'addmovie.html'
    fields = '__all__'
    success_url = reverse_lazy('movie:viewmovie')

# def viewmovie(request):
#     b=Movie.objects.all()
#     return render(request,template_name='viewmovie.html',context={'b':b})

class MovieList(ListView):
    model=Movie
    template_name='viewmovie.html'
    context_object_name='b'

# def detail(request,p):
#     b=Movie.objects.get(name=p)
#     return render(request,template_name='detail.html',context={'b':b})
class MovieDetail(DetailView):
    model=Movie
    template_name='detail.html'
    context_object_name='b'

# def delete(request,p):
#     b=Movie.objects.get(name=p)
#     b.delete()
#     return viewmovie(request)

class MovieDelete(DeleteView):
    model=Movie
    success_url = reverse_lazy('viewmovie')
    template_name = 'delete.html'

# def update(request,p):
#     b = Movie.objects.get(name=p)
#     if (request.method == 'POST'):
#         form = Movieform(request.POST,request.FILES,instance=b)
#         if form.is_valid():
#             form.save()
#             return viewmovie(request)
#
#     form=Movieform(instance=b)
#     return render(request,template_name='update.html',context={'form':form})

class MovieUpdate(UpdateView):
    model = Movie
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('viewmovie')