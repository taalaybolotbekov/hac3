from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.mail import send_mail
from django.views import View
from .forms import ApplicationsForm
import telebot

bot = telebot.TeleBot('1116291257:AAFuY9YASfUnBJ6nwwLyvwJiLJykcepzgLI')

def index(request):
    form = ApplicationsForm()
    return render(request, 'shop/index.html')

def shop(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'shop/shop.html', context)

def contact(request):
    return render(request, 'shop/contact-us.html')

def product_details(request):
    return render(request, 'shop/product-details.html')

def product_affiliate(request):
    return render(request, 'shop/product-details-affiliate.html')

def product_group(request):
    return render(request, 'shop/product-details-group.html')

def product_variable(request):
    return render(request, 'shop/product-details-variable.html')

def cart(request):
    return render(request, 'shop/cart.html')

class ApplicationsView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ApplicationsForm(request.POST)
            # print(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data['mail']
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'Новая заявка на подписку!'
            from_email = 'bolotbekovtaalay@gmail.com'
            to_email = ['bolotbekovtaalay@gmail.com']
            message = 'Новая заявка!' + '\r\n' + '\r\n' + 'Почта: ' + mail + '\r\n' + '\r\n' + 'Имя:' + name + '\r\n' + 'Коммент' + comment
            send_mail(subject, message, from_email, to_email, fail_silently=False)
            bot.send_message(449062776, message)
        return redirect('home')