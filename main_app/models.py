from django.db import models

# Create your models here.
class DishCategory(models.Model):
	title = models.CharField(max_length=50, unique=True)
	position = models.PositiveSmallIntegerField(unique=True)
	is_visible = models.BooleanField(default=True)

	def __iter__(self):
		for dishe in self.dishes.all():
			yield dishe

	def __str__(self):
		return f'{self.title}'

	class Meta:
		ordering = ('position', )


class Dish(models.Model):
	title = models.CharField(max_length=50, unique=True)
	position = models.PositiveSmallIntegerField()
	is_visible = models.BooleanField(default=True)
	category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dishes')
	is_special = models.BooleanField(default=True)
	is_signature = models.BooleanField(default=True)
	is_recomendet = models.BooleanField(default=True)
	desc = models.TextField(max_length=200, blank=True)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	discount = models.DecimalField(max_digits=8, decimal_places=2)
	ingradients = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='dishes')

	def __str__(self):
		return f'{self.title}'

	def total_price(self):
		return (self.price - self.discount / 100 * self.price) * 100

	def fix_price(self):
		return self.price * 100

	class Meta:
		ordering = ('position', )