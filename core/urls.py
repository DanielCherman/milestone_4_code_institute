from django.urls import path
from .views import ContactUsView, Home
from .views import ContactUsView, Home, QuoteOrder, OrdersViews, SendOfferView, SaveReply, \
    AcceptOffer, OrderDeliver, InProgressOrders, DeliveredOrder

app_name = "core"

urlpatterns = [
    path('', Home , name="Home"),
    path('contact-us/', ContactUsView, name="Contact"),
    path('quote/', QuoteOrder, name="UserQuote"),
    path('order/', OrdersViews, name="Order"),
    path('orderList/', SendOfferView, name="OfferSend"),
    path('save/<int:pk>/', SaveReply, name="SaveReply"),
    path('offer/<int:pk>/', AcceptOffer, name="AcceptOffer"),
    path('deliverOrder/<int:pk>', OrderDeliver, name="OrderDeliver"),
    path('inProgress/', InProgressOrders, name="InProgressOrders"),
    path('delivered/', DeliveredOrder, name="DeliveredOrder"),
]
