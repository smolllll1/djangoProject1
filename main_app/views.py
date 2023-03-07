from django.shortcuts import render
from .models import DishCategory, Dish, About
# Create your views here.
def main_view(request):
	categories = DishCategory.objects.filter(is_visible=True)
	dishes = Dish.objects.filter(is_visible=True, is_special=False, is_signature=False)
	is_signature = Dish.objects.filter(is_visible=True, is_signature=True)
	special = Dish.objects.filter(is_visible=True, is_special=True)
	ubout = About.objects.filter(is_visible=True)
	return render(request, 'main_page.html', context={
		'categories': categories,
		'dishers': dishes,
		'signature': is_signature,
		'offers': special,
		'ubout': ubout,
	})