from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.views.generic import DetailView
from k1.forms import CommentForm
from k1.models import Comment


def home(request):

    return render(request,"home.html")

def login1(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('home')
            else:
                return redirect('login')
        else:
            return redirect('login')
    form = AuthenticationForm()

    return render(request,"login.html",context={"form":form})

def signup(request):
    signupform=UserCreationForm(request.POST or None)
    if signupform.is_valid():
        signupform.save()
        username=signupform.cleaned_data.get("username")
        raw_password=signupform.cleaned_data.get('password1')
        user=authenticate(username=username,password=raw_password)
        login(request,user)
        return redirect('home')
    return render(request,'sign_up.html',{'form':signupform})
def logout_view(request):
    logout(request)
    return redirect('home')

def comment_table(request):
    alltodos=Comment.objects.all()
    return render(request,'comment.html',{'comments':alltodos})

@login_required
def add_comment1(request):
    todoform=CommentForm(request.POST or None)
    if todoform.is_valid():
        todoform.save()
        return redirect('comment')
    return render(request,'add_comment.html',{'form':todoform})
@login_required
def todoedit(request,pk):
    todo = get_object_or_404(Comment,pk=pk)
    todoform = CommentForm(request.POST or None,instance=todo)
    if todoform.is_valid():
        todoform.save()
        return redirect('comment')
    return render(request,'add_comment.html',{'form':todoform})
@login_required
def tododelete(request,pk):
    todo = get_object_or_404(Comment,pk=pk)
    if request.method=='POST':
        todo.delete()
        return redirect('comment')
    return render(request,'delete.html',{'todo':todo})

'''class post_detail_view(DetailView):
    model = Comment
    template_name = "comment.html"'''