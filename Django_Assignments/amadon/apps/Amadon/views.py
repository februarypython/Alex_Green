from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'amadon/index.html')

def process(request):
    quantity = (request.POST['quantity'])
    if request.POST['product_id'] == 'tshirt':
        price = int(quantity) * 19.99
    
    if request.POST['product_id'] == 'sweater':
        price = int(quantity) * 29.99

    if request.POST['product_id'] == 'books':
        price = int(quantity) * 49.99
    
    if request.POST['product_id'] == 'cup':
        price = int(quantity) * 4.99

    try:
        request.session['count'] += int(quantity)

    except KeyError:
        request.session['count'] = int(quantity)

    try:
        request.session['total_price'] += price

    except KeyError:
        request.session['total_price'] = price
    
    request.session['price'] = price    
    return redirect("/checkout")

def checkout(request):
    return render(request, 'amadon/checkout.html')

def logout(request):
    request.session.clear()
    return redirect("/")

