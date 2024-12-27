from django.shortcuts import render,get_object_or_404,redirect
from .models import Turlar,Gullar
from .forms import TurForm,GulForm,RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def turlar_list(request):
    turlar = Turlar.objects.all()
    content = {'turlar':turlar}
    return render(request,'turlar_list.html',content)

def gullar_list(request):
    gullar = Gullar.objects.all()
    content = {'gullar':gullar}
    return render(request,'gullar_list.html',content)

def tur_by_gullar(request,tur_id):
    turi = get_object_or_404(Turlar,pk = tur_id)
    gullar = Gullar.objects.filter(turi=turi)
    return render(request,'tur_by_gullar.html',{'tur':turi,'gullar':gullar})

def gul_detail(request,gul_id):
    gul = get_object_or_404(Gullar,pk = gul_id)
    return render(request,'gul_detail.html',{'gul':gul})
def add_tur(request):
    if request.method == 'POST':
        form = TurForm(request.POST)
        if form.is_valid():
            Turlar.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description']
            ) 
            return redirect('/')  
    else:
        form = TurForm()  

    return render(request, 'add_tur.html', {'form': form})


def add_gul(request):
    if request.method == 'POST':
        form = GulForm(request.POST)
        if form.is_valid():
            turi = form.cleaned_data['turi']
            Gullar.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                turi=turi 
            )
            return redirect('/')  
    else:
        form = GulForm() 
   
    return render(request, 'add_gul.html', {'form': form})

def update_tur(request, tur_id):
    tur = get_object_or_404(Turlar, pk=tur_id)

    if request.method == 'POST':
        form = TurForm(request.POST)
        if form.is_valid():
            tur.name = form.cleaned_data['name']
            tur.description = form.cleaned_data['description']
            tur.save()  
            return redirect('/')  
    else:
        form = TurForm(initial={'name': tur.name, 'description': tur.description})

    return render(request, 'add_tur.html', {'form': form})

def update_gul(request, gul_id):
    gul = get_object_or_404(Gullar, pk=gul_id)

    if request.method == 'POST':
        form = GulForm(request.POST)
        if form.is_valid():
            gul.name = form.cleaned_data['name']
            gul.description = form.cleaned_data['description']
            gul.price = form.cleaned_data['price']
            gul.turi = form.cleaned_data['turi']
            gul.save() 
            return redirect('/')
    else:
        form = GulForm(initial={
            'name': gul.name,
            'description': gul.description,
            'price': gul.price,
            'turi': gul.turi.id 
        })

    return render(request, 'add_gul.html', {'form': form})

 
def delete_tur(request, tur_id):
    tur = get_object_or_404(Turlar, pk=tur_id) 
    if request.method == 'POST':
        tur.delete() 
        return redirect('turlar_list')
    return render(request, 'delete_tur.html', {'tur': tur})

def delete_gul(request, gul_id):
    gul = get_object_or_404(Gullar, pk=gul_id)
    if request.method == 'POST':
        gul.delete() 
        return redirect('/')
    return render(request, 'delete_gul.html', {'gul': gul})


def register(request):
    if  request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            password_repeat = form.cleaned_data.get("password_repeat")
            if password_repeat == password:
               user =  User.objects.create_user(
                    form.cleaned_data.get("username"),
                    form.cleaned_data.get("email"),
                    password
                )
               
               return redirect('login')
                
    context = {
        "form":RegisterForm()
    }
    return render(request,'auth/register.html',context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password) 
            if user is not None:  
                login(request, user)  
                return redirect('turlar_list') 
            else: 
                return render(request, 'auth/login_user.html', {
                    'form': form,
                    'error': "Username yoki parol noto‘g‘ri!"
                })
    else:  
        form = LoginForm()
    return render(request, 'auth/login_user.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

    
