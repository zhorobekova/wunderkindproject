from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from article.models import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from article.views import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def home(request):
#     return render(request , 'index.html', {})

# def home(request):
    # a=Author.objects.get(id=15)
    #return render(request, 'index.html', {'author':a})

    #return render a =get_object_404(Author, id=15)
    # try:
    #     a=Author.objects.get(id=15)
    # except Author.DoesNotExist:
    #     raise Http404
    # return render(request, 'index.html', {'author':a})
     #башка варианты
      #raisedi kosho ochurobuz
      #return HttpResponse('Ne naideno')
def home(request):
    authors=Author.objects.all()
    return render(request,'index.html',{'list': authors})

def news(request):
    news_event= Author.objects.all()
    context={
        "auth":news_event,
        "title":" Список авторов",
    }
    return render(request, "news.html",context)
class DetailNews(DetailView):
    template_name = "detail.html"
    queryset = Author.objects.all()
    context_oject_name= "d_news"


# def detail_news(request,auth_id):
#     # d_news=Author.objects.get(id=auth_id)
#     d_news = get_object_or_404(Author, id=auth_id)
#     return render(request,"detail.html",{"d_news" : d_news})
class AuthorDelete(DeleteView):
    template_name ="delete_author.html"
    model = Author
    fields = '__all__'
    template_name="authors.html"
    success_url = "/index/"

# def delete_news(request, auth_id):
#     news=Author.objects.get(id=auth_id)
#     news.delete()
#     return redirect('news')                                                                                              

# def comment(request):
#     comm=comment.objects.get.all()
#     return render(request,"comment.html",{"comm": comm})   
   
# def com_detail(request,comment_id):
#     d_comm= get_object_or_404(comment,id=comment_id) 
#     return render(request,"com_detail.html",{"d_comm": d_comm})    

class AuthorCreateAndListView(CreateView):
    model = Author
    fields = '__all__'
    template_name="authors.html"
    success_url = "/author/all/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context

class AuthorUpdate(UpdateView):
    template_name ="update-author.html"
    model = Author
    fields =('fio', 'address','email')   
    success_url = "/index/"
    context_objext_name = "author"  


class AuthorCreate(CreateView):
    model = Author
    fields = ('fio', 'address','email')
    success_url = "/author/all/"
    context_objext_name = "author"
    template_name = "author-create.html" 
# def create_author(request):
#     if request.method=="POST":
#         fio_author=request.POST["fio"]
#         address_author=request.POST['address']
#         email_author=request.POST['email']
#         address_author=request.POST['address']
#         Author.objects.create(fio=fio_author, address=address_author,email=email_author)
#         return HttpResponse("Save successfully")
#     context={}
#     return render(request,"author-create.html", context)

def update_author(request,auth_id):
    author = get_object_or_404(Author,id=auth_id)
    if request.method=="POST":
        fio_author=request.POST["fio"]
        email_author=request.POST['email']
        address_author=request.POST['address']
        author.fio = fio_author
        author.email = email_author
        author.address = address_author
        author.save()
        return HttpResponse("Updated successfully")
    context={
          "author":author
      }  
    return render(request, "update-author.html",context)


def readers(request):
    readers=Readers.objects.all()
    return render(request,'readers.html',{'d_read': readers, 'title':'Readers list'})  

def detail_readers(request,read_id):
    # d_news=Author.objects.get(id=auth_id)
    d_read = get_object_or_404(Readers, id=read_id)
    return render(request,"readers.html",{"d_read" : d_read}) 

def create_readers(request):
    if request.method=="POST":
        fio_readers=request.POST["fio"]
        address_readers=request.POST['address']
        email_readers=request.POST['email']
        Readers.objects.create(fio=Readers, address=address_readers,email=email_readers)
        return HttpResponse("Save successfully")
    context={}
    return render(request,"readers.html", context)

def update_readers(request,read_id):
    readers = get_object_or_404(Author,id=read_id)
    if request.method=="POST":
        fio_readers=request.POST["fio"]
        email_readers=request.POST['email']
        address_readers=request.POST['address']
        readers.fio = fio_readers
        readers.email = email_readers
        readers.address = address_readers
        readers.save()
        return HttpResponse("Updated successfully")
    context={
          "readers":readers
      }  
    return render(request, "update-readers.html",context)


class NewsViews(ListView):
    template_name = "news.html"
    queryset = Author.objects.all()
    context_object_name= "auth"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Список читателей"
        return context 



def index(request):
    author_list = Author.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(author_list, 2)
    try:
        author = paginator.page(page)
    except PageNotAnInteger:
        author = paginator.page(1)
    except EmptyPage:
        author = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'author': author })        




    
    





 



