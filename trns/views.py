from django.shortcuts import render
from .models import *
import pysrt
from googletrans import Translator, constants
from pprint import pprint

from django.core.files import File





def kav(request):
	if request.method == 'POST':
		na = request.FILES['myfile']
		name=request.FILES['myfile'].name
		lanq=request.POST['lan']

		print(name)
		po= Nan(file=na)
		po.save()
		subs = pysrt.open('media/'+name)
		translator = Translator()
		b=len(subs)
		print(b)
		for i in range(0,20):
			a=subs[i].text
			translation = translator.translate(a,dest=lanq)
			subs[i].text=translation.text
			print(subs[i].text)
			print(i)
		ban=subs.save('media/subtitle.srt')
		#p= Nan(file=ban)
		#p.save()
		return render(request,'trns/dam.html')
		
		#return render(request,'accounts/abc.html',{'akjh':akjh})
	return render(request,'trns/dam.html')


