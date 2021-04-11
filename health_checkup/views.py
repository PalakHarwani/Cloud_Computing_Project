from django.shortcuts import render
from .models import Detail
from datetime import datetime

# bmi
# diabetes
# typohid
# anemia
# dengue
# heart attack

# Create your views here.
def health_checkup(request):
	# print(request.POST)
	# age = request.POST.get('age')
	# bp = request.POST.get('bp')
	# gen = request.POST.get('gen')
	# sug = request.POST.get('sug')
	# temp = request.POST.get('temp')
	# dia = diabetes(age,sug)
	# print(dia)

	return render(request, 'home.html', {'name':request.session['user']})

def view(request):
	history = Detail.objects.filter(user=request.session['user'])
	return render(request,'view.html',{'data':history})

def patient_data(request):
	print(request)
	wei = int(request.GET.get('wei'))
	hei = float(request.GET.get('hei'))
	age = int(request.GET.get('age'))
	bp = int(request.GET.get('bp'))
	gen = request.GET.get('gen')
	sug = int(request.GET.get('sug'))
	temp = int(request.GET.get('temp'))
	blo = int(request.GET.get('blo'))
	# print(age,sug)
	dia = diabetes(age,sug)*100
	bmi = wei/(hei*hei)
	obe=2
	if(bmi<18):
		obe=0
	if(bmi>25):
		obe=1
	bmi = "{:.2f}".format(bmi)
	
	typ = typhoid(age,temp,bp)*100
	ane = anemia(blo,gen)*100
	htk = heartatk(age,blo,wei)*100
	den = dengue(blo,temp)*100
	Detail.objects.create(user=request.session['user'],time=datetime.now(),age=age,gen=gen,wei=wei,hei=hei,bp=bp,sug=sug,tem=temp,hae=blo,bmi=bmi,dia=dia,typ=typ,hea=htk,ane=ane,den=den)
	context = {'dia': dia*100 , 'bmi':bmi, 'typ':typ, 'ane':ane, 'htk':htk, 'den':den, 'obe':obe}
	return render(request, 'dia.html', context)
	# if(dia==1):
	# 	context = {'dia': 100}
	# 	return render(request, 'dia.html', context)
	# else:
	# 	context = {'dia': 0}
	# 	return render(request, 'dia.html', context)


# def tuber(age,bp,gen,sug):
	


def diabetes(age,sug):
	if(age>30 and sug>140):
		return 0.9
	if(age>30 and sug>135):
		return 0.7	
	if(age<30 and sug>160):
		return 0.45
	if(age<30 and sug>140):
		return 0.3
	return 0

def typhoid(age,temp,bp):
	if(temp>40 and bp>140):
		return 0.8
	if(temp>40 and bp>130):
		return 0.6
	if(temp>37 and bp>120):
		return 0.2
	return 0

def anemia(blo,gen):
	if(blo<6 and (gen=='M' or gen=='m')):
		return 1
	if(blo<9 and (gen=='M' or gen=='m')):
		return 0.5
	if(blo<11 and (gen=='M' or gen=='m')):
		return 0.2
	if(blo<4 and (gen=='F' or gen=='f')):
		return 1
	if(blo<7 and (gen=='F' or gen=='f')):
		return 0.6
	if(blo<9 and (gen=='F' or gen=='f')):
		return 0.3
	return 0

def heartatk(age,blo,wei):
	if(age>50 and wei>100 and bp>150):
		return 0.6
	if(age>30 and wei>80 and bp>135):
		return 0.3
	return 0

def dengue(blo,temp):
	if(blo<4 and temp>40):
		return 0.9
	if(blo<7 and temp>38):
		return 0.6
	if(blo<10 and temp>37):
		return 0.3
	return 0

