from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import create_form	
import forms
from django.http import HttpResponseRedirect
import os

# def index(request, **filed):
#     if request.method == 'POST':
#     	print request.POST
#     	# print request.POST
#      #    if form.is_valid():
#      #        return HttpResponseRedirect('/polls/')
#     else:
#         form = input_text()
#         print form
#     return render(request, 'polls/index.html', {'form': form})

@csrf_exempt
def index(request):
	# response = create_form()
	# print response
	return render(request, 'polls/index.html')
	# if request.is_ajax():
	# 	request.POST['val']
	# else:
	# 	call=forms.create_form()
	# 	response = call.text(2) 
	# return render(request, 'polls/index.html',{{ response }})

@csrf_exempt
def detail(request, link_id):
	response = create_form()
	html_str="""<html>
			<head></head>
			<body><p>Hello World! %s </p></body>
			</html>""" %(response)
	path = os.path.join(os.path.expanduser('~'), 'Desktop','work-task','mysite','polls','templates','polls', 'file.html')
	if os.path.isfile(path):
	    print 'replacing'
	    with open(path,'w') as obj:
			obj.write(html_str)
	else: 
	    with open(path,'w') as obj:
			obj.write(html_str)
	return render(request, 'polls/file.html')