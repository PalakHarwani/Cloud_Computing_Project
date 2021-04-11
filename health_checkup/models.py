from django.db import models


# Create your models here.
class Detail(models.Model):
	user = models.CharField(max_length=20)
	time = models.DateTimeField(auto_now=True)
	age = models.IntegerField()
	gen = models.CharField(max_length=1)
	wei = models.IntegerField()
	hei = models.IntegerField()
	bp = models.IntegerField()
	sug = models.IntegerField()
	tem = models.IntegerField()
	hae = models.IntegerField()
	bmi = models.DecimalField(max_digits=4, decimal_places=1)
	dia = models.DecimalField(max_digits=4, decimal_places=1)
	typ = models.DecimalField(max_digits=4, decimal_places=1)
	hea = models.DecimalField(max_digits=4, decimal_places=1)
	ane = models.DecimalField(max_digits=4, decimal_places=1)
	den = models.DecimalField(max_digits=4, decimal_places=1)

	def __str__(self):
		return self.user