from django.shortcuts import render, redirect
from .models import Pizza
from .forms import CommentForm

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()


    context = {'pizzas': pizzas}

    return render(request, 'MainApp/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    comments = pizza.comment_set.all()

    context = {
        'pizza': pizza,
        'toppings': toppings,
        'comments':comments
    }

    return render(request, "MainApp/pizza.html", context)

def new_comment(request):
    if request.method != 'POST':
        form = CommentForm
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save()

            url = 'MainApp'
            return redirect('MainApp:pizzas')
    context = {
        'form':form
    }
    return render(request, 'MainApp/new_comment.html', context)