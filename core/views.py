from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import ContactForm, QuoteForm
from .models import CustomerQuery, Order

def check_admin(user):
    return user.is_superuser

def Home(request):
    return render(request, 'core/index.html')

def ContactUsView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:Home')
    else:

        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'core/contactus.html', context)

def QuoteOrder(request):
    if request.user.is_superuser:
        return redirect('core:OfferSend')

    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            save_user = form.save(commit=False)
            save_user.user = request.user
            save_user.status = False
            save_user.save()
            return redirect('core:UserQuote')
    else:

        form = QuoteForm()

    context = {
        'form': form,
    }
    return render(request, 'core/profile.html', context)


def OrdersViews(request):
    queryset = CustomerQuery.objects.filter(user=request.user)

    context = {
        'customer_query': queryset,
    }
    return render(request, 'core/orders.html', context)


def AcceptOffer(request, pk):
    accept_offer = CustomerQuery.objects.get(id=pk)
    accept_offer.status = True
    accept_offer.save()
    Order.objects.create(buyer=accept_offer.user, title=accept_offer.title, description=accept_offer.description,
                         final_price=accept_offer.final_price)
    return redirect('core:Order')


@user_passes_test(check_admin)
def SendOfferView(request):
    queryset = CustomerQuery.objects.all()
    context = {
        'customer_query': queryset,
    }
    return render(request, 'core/admin_dashboard/orders.html', context)


@user_passes_test(check_admin)
def SaveReply(request, pk):
    if request.method == 'POST':
        message = request.POST.get("description_message")
        final_price = request.POST.get("final_price")
        save_reply = CustomerQuery.objects.get(id=pk)
        save_reply.description_message = message
        save_reply.final_price = final_price
        save_reply.save()
    return redirect("core:OfferSend")


@user_passes_test(check_admin)
def OrderDeliver(request, pk):
    if request.method == 'POST':
        file = request.FILES['delivery_file']
        status = "Delivered"
        getOrder = Order.objects.get(id=pk)
        getOrder.status = status
        getOrder.delivery_file = file
        getOrder.save()
    return redirect('core:InProgressOrders')


def DeliveredOrder(request):
    if request.user.is_superuser:
        getOrders = Order.objects.filter(status="Delivered")
        context = {
            'orders': getOrders
        }
        return render(request, 'core/admin_dashboard/delivery.html', context)
    else:
        getOrders = Order.objects.filter(status="Delivered", buyer=request.user)
        context = {
            'orders': getOrders
        }
        return render(request, 'core/delivered.html', context)


def InProgressOrders(request):
    if request.user.is_superuser:
        orders = Order.objects.filter(status="In_Progress")
        context = {
            'orders': orders,
        }
        return render(request, 'core/admin_dashboard/inprogress.html', context)
    else:
        orders = Order.objects.filter(status="In_Progress", buyer=request.user)
        context = {
            'orders': orders,
        }
        return render(request, 'core/inprogress.html', context)