from django import forms
from hostel_app.models import Booking

class RoomSearchForm(forms.Form):
    search = forms.CharField(max_length=128)
    
    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ('is_checkout','services')
        
        
    
        
        
