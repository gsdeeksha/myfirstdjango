from django.shortcuts import render,redirect
from .forms import BookForms,SearchForm, ModelBookForms
from home1.models import Book
from django.utils import timezone
from django.contrib import messages
#from catalog.models import Book 
# Create your views here.
def home_view(request):
    return render(request,'home.html')

def design(request):
    return render(request,'myproject.html')

def register(request):
    return render(request,'register.html')

def form(request):
    return render(request,'form.html')

def carousel(request):
    return render(request,'carousel.html')

def form_view(request):
    msg=''
    if request.method =='POST':
        form = BookForms(request.POST)
        if form.is_valid():
            #  book =Book(
            #     name=form.cleaned_date.get('name'),
            #     purchase_date=form.cleaned_date.get('pur_date'),
            #     genre=form.cleaned_date.get('genre'),
            #     author=form.cleaned_date.get('author'),
            # ) 
            book = Book.objects.create(
                name=form.cleaned_data.get('name'),
                purchase_date=form.cleaned_data.get('pur_date'),
                author=form.cleaned_data.get('author'),
            )
            book.save()
            msg = 'Book Added Successfully!!'
        else:
            msg = form.errors
    else:
        form =BookForms()
    # book=Book.objects.all()
    return render(request,'forms.html',{ "msg":msg,"forms":form})

def html_form(request):
    value =''
    if request.method=='PoST':
        value = request.POST.get('name')
        return render(request,'values.html',{ 'values':value})
    else:
        value='wrong input'
    return render(request,'myproject.html',{ 'values':value})

def booksearch(request):
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            q=form.cleaned_data.get('q')
            #book=Book.objects.filter(name__contains=q,purchase_date__lte=timezone.now)
            book=Book.objects.filter(name__contains=q)
            #form =None
            return render(request,'showtables.html',{'book':book})
    else:
        form = SearchForm()
        book = Book.objects.all()
    return render(request, 'showtables.html',{'book':book,'form':form})

def deletebook(request,id):
    book=Book.objects.get(id=id)
    messages.success(request,'Deleted'+str(id)+'Successfully!!')
    book.delete()
    return redirect('/')

def editbook(request,id):
    book=Book.objects.get(id=id)
    if request.method=='POST':
        form =ModelBookForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'edited'+str(id)+'successfully!!')
            return redirect('/')
    else:
        form=ModelBookForms(instance=book)
    return render(request,'editbook.html',{'form':form})
# from django.shortcuts import render,redirect
# from home.models import newreg 
# from django.shortcuts import render, redirect
# from .forms import RegistrationForm 
# # Create your views here.
# def reg_redirect(request):
#     return redirect('/')

 
# def index(request):
#     if request.method =='POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/registered')
#     else:
#         form = RegistrationForm()
#         args = {'form': form}
#         return render(request, '/index.html', args)
 
# def registered(request):
#     return render(request, '/registered.html')