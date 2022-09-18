from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchForm
from django.contrib.postgres.search import SearchVector,SearchQuery, SearchRank
from .models import NewsObject
# Create your views here.

#spewApiContent()
def index(request):
    if request.method == 'GET':
        ext = NewsObject.ext.order_by('-added')[:]
        paginator = Paginator(ext, 20)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html',{
        'posts':posts,
    })

def latest(request):
    if request.method == 'GET':
        news = NewsObject.ext.order_by('-added')[:15]
        return render(request, 'latest.html', {'latest':news})

def search(request):
    form = SearchForm()
    query = None 
    results = []
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = request.GET.get('query')
            #query = form.cleaned_data['query']
            search_vector = SearchVector('title',)
            search_query =  SearchQuery(query) 
            results = NewsObject.ext.annotate(search= search_vector,
                                                rank=SearchRank(search_vector, search_query)).filter(search=search_query).order_by('-rank')
    return render(request, 'search.html',
                        {'form':form,
                        'query':query,
                        'search_results':results})