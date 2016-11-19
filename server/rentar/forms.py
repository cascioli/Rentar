from django import forms
from rentar.models import Apartment, Landlord, Apartment_Rating, Landlord_Rating
class ApartmentForm(forms.ModelForm):
	class Meta:
		model = Apartment
		fields = '__all__'

class ApartmentRatingForm(forms.ModelForm):
	class Meta:
		model = Apartment_Rating
		fields = '__all__'
