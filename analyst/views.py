from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

from .models import Dataset
from .forms import ModelFormCSVFile


def home(request):
	question = 1
	return render(request, 'analyst/home.html', {'question': question})
	
	
def data(request):
	
	if request.method == 'POST':
		
		#delete
		print (request.POST['deleteid'])
		if int(request.POST['deleteid'])>0:
			ds = Dataset.objects.get(id = request.POST['deleteid'])
			ds.delete()
			form = ModelFormCSVFile()
			
		#add	
		else:
			form = ModelFormCSVFile(request.POST, request.FILES)
			if form.is_valid():
				print (request.POST)
				ds = Dataset(name=request.POST['name'], content = request.FILES['csvfile'])
				ds.save()
	else:
		form = ModelFormCSVFile()
		
	datasets = Dataset.objects.order_by('-name')
	context = {'datasets': datasets, 'form': form}
	return render(request, 'analyst/data.html', context)


def dataallentries(request, data_id):
	ds = Dataset.objects.get(id =data_id)
	df = pd.read_json(ds.content)
	content = df.to_html(classes=['table', 'table-striped'])
	context = {'content':content}
	return render(request, 'analyst/data_allentries.html', context)
	
