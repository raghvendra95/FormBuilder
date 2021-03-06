from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from .forms import create_form	
import forms
from django.http import HttpResponseRedirect
import json
import os
from django.shortcuts import redirect
from django.template.loader import render_to_string

@csrf_exempt
def index(request):
	return render(request, 'form_builder_app/index.html')

# @csrf_exempt
# def your_form(request,link_id):
# 	response=''
# 	#if request.is_ajax():
# 	form_json=request.POST
# 	obj_form = forms.create_form(form_json)
# 	response = obj_form.create_input(form_json)
# 	#t = loader.get_template('form_builder_app/your_form.html')
# 	#html = render_to_string('form_builder_app/your_form.html', {'response':response})
# 	#html = t.render(RequestContext(request, {'response': response})
# 	return render(request, 'form_builder_app/your_form.html',{'response':response})

@csrf_exempt
def your_form(request,link_id):
		if request.is_ajax():
			form_json=request.POST
			obj_form = forms.create_form(form_json)
			response = obj_form.create_input(form_json)
			html_str="""<!DOCTYPE html>
			<html>
			<head>
			  <title>Form Builder</title>
			  
			  <meta charset="utf-8">
			  <meta name="viewport" content="width=device-width, initial-scale=1">
			  <!-- Latest compiled and minified CSS -->
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	
			<!-- jQuery library -->
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
			<!-- Latest compiled JavaScript -->
			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

			</head>
			<body>
			<form class="form-horizontal">
			<fieldset>
			<legend>Your Form</legend>
			%s
			<div class="form-group">
			  <label class="col-md-4 control-label" for="singlebutton">Submit</label>
			  <div class="col-md-4">
			    <button id="submit" onclick='submit_form();' name="btn-submit" class="center btn btn-primary">Submit</button>
			  </div>
			</div>
			</fieldset>
			</form>
			</body>
			</html>""" %(response)
			# print response
			path = os.path.join(os.path.expanduser('~'), 'Desktop','task-work2','env','FormBuilder','form_builder_app','templates','form_builder_app', 'your_form.html')
			if os.path.isfile(path):
			    print 'replacing'
			    with open(path,'w') as obj:
					obj.write(html_str)
			else: 
				with open(path,'w') as obj:
					obj.write(html_str)
			return HttpResponse(response)
		else:
			return render(request, 'form_builder_app/your_form.html')