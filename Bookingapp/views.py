from django.shortcuts import redirect
from .models import Booking,Products
from .forms import Bookingform 
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class HomeView(ListView):
    model=Products
    template_name='home.html'
    context_object_name="products"
    pk_url_kwarg='id'

class BookingView(CreateView):
    model=Booking
    form_class=Bookingform  
    template_name="booking.html"
    success_url="home" 
    pk_url_kwarg="id"   

    def post(self, request, *args, **kwargs):
        form=Bookingform(request.POST)
        if form.is_valid():
            id=kwargs.get('id')  
            cname=form.cleaned_data.get("customer_name")
            cnum=form.cleaned_data.get("customer_num")
            caddress=form.cleaned_data.get("customer_address")
            item=Products.objects.get(id=id)
            rentdate=form.cleaned_data.get("rent_date")
            returndate=form.cleaned_data.get("return_date")
            Booking.objects.create(customer_name=cname,customer_num=cnum,customer_address=caddress,item=item,rent_date=rentdate,return_date=returndate)     
            messages.success(request,"Booking Successfully")                              
            return redirect("home")           
        else:
            messages.error(request,"Booking Failed")
            return redirect("home") 