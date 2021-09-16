from django.shortcuts import render
from django.http import HttpResponse
from.models import Post,Phone,Review

from django.db.models import Q










def blog(request):
    context={'kola':Post.objects.all()}

    return render(request,'umm/blog.html',context)


def sagol(request):
    return render(request,'umm/sagol.html',{'title':'False'})


def tika(request):
    qs = Phone.objects.all()

    query = request.GET.get("q", None)

    if query is not None:
        qs = qs.filter(Model_icontains=query)
        nai={'queryset_list':qs}




    nai={'ri':Phone.objects.all()}
    return render(request,'umm/tika.html',nai)

def pada(request):
    lol={'taka':Review.objects.all()}
    return render(request,'umm/new.html',lol)











# Create your views here.
