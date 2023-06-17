from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from hostel_app.forms import RoomSearchForm, BookingForm
from hostel_app.models import Room, Staff, Booking
from django.core.paginator import Paginator


class HostelAppView (ListView):
   model = Room
   context_object_name = 'rooms'
   template_name = 'rooms.html'
   
   
   def get_queryset(self):
       return self.model.objects.filter(hottest=True)
   
    
   def get(self, request):
       queryset = self.get_queryset()
       staff = Staff.objects.all()
       return render(request, self.template_name, context={self.context_object_name:queryset, 'staffs':staff})
        
   

class HostelAppView2 (ListView):
   model = Room
   context_object_name = 'rooms'
   template_name = 'rooms2.html'
   paginate_by = 3
   
   def get_context_data(self, *, object_list=None, **kwargs):
       context = super().get_context_data(object_list=object_list, **kwargs)
       context['object-count'] = self.model.objects.count()
       paginator = Paginator(self.model.object_list, self.paginate_by)
       try:
           page = self.request.GET.get('page')
       except:
           page = 1
           
       try:
           context[self.context_object_name] = paginator.page(page)
       except:
           context[self.context_object_name] = paginator.page(1)
           
       context['object-count'] = self.model.objects.count()
       context['paginator'] = paginator
       return context
  
   def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        
        form = RoomSearchForm(self.request.GET)
        if form.is_valid():
            pass
        
        else:
            form = RoomSearchForm()
            
        context['form'] = form
        return context
        
   def get(self, request, *args, **kwargs):
       form = RoomSearchForm(self.request.GET)
       if form.is_valid():
           cd = form.cleaned_data
           rooms = self.model.objects.filter(name__icontains=cd['search'])
       else:
           rooms = self.model.objects.all()
       return render(request, self.template_name, self.get_context_data(object_list=rooms))
   
    
   
class StaffView (ListView):
   model = Staff
   context_object_name = 'staffs'
   template_name = 'rooms.html'
   
   
def restaurant_view(request):
    context = {'page':'restaurant'}
    return render(request, 'restaurant.html',context)



   
def room_id_view(request, pk):
    pk = get_object_or_404(Room, pk=pk)
    booking = Booking.objects.all()
    if request.method=="POST": 
        form = BookingForm(request.POST) 
        if form.is_valid(): 
            booking =  form.save(commit=False) 
            booking.rooms = pk 
            booking.save() 
            form = BookingForm() 
    else:
        form = BookingForm()
    context = {"pk": pk,'page':'rooms', 'booking_list':booking, 'form':form}
    return render(request, "rooms_details.html", context)


