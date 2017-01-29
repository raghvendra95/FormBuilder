from django import forms
import json

class create_form(object):
	"""docstring for create_form"""
	def __init__(self,form_json):
		self.form_json = form_json
		# dict_form=dict(form_json)
		# new_dict={}
		# keys_list1=[]
		# for key, value in dict_form.iteritems():
		# 	new_dict[str(key)]=str((str(value)[1:-1]))
		# for key,value in new_dict:
		# 	keys_list1.append(key)	

	def create_input(self,form_json=None,*args,**kwargs):
		dict_form=dict(form_json)
		new_dict={}
		keys_list1=[]
		for key, value in dict_form.iteritems():
			new_dict[str(key)]=str((str(value)[1:-1]))
		# for key,value in new_dict:
		# 	keys_list1.append(key)	
		input_box=''
		len_dict =len(new_dict)/7
	 	for i in range(len_dict):
	 		if (new_dict['form['+str(i)+'][check_flag]']).replace("u'","").replace("'","")=='1':
				input_box+='<div class="form-group"><label class="col-md-4 control-label" for="textinput">'
				input_box+=str(new_dict['form['+str(i)+'][title]']).replace("u'","").replace("'","")
				input_box+='</label><div class="col-md-4">'
				input_box+='<input id="'+str(new_dict['form['+str(i)+'][name]']).replace("u'","").replace("'","")+'"'
				input_box+='name="'+str(new_dict['form['+str(i)+'][name]']).replace("u'","").replace("'","")+'"'
				input_box+='type="'+str(new_dict['form['+str(i)+'][sub_type]']).replace("u'","").replace("'","")+'"'
				input_box+='placeholder="'+str(new_dict['form['+str(i)+'][placeholder]']).replace("u'","").replace("'","")+'"'
				input_box+='class="form-control input-md"></div></div>'
			if ((new_dict['form['+str(i)+'][check_flag]']).replace("u'","").replace("'","")=='2'):
				num_of_radio=int((new_dict['form['+str(i)+'][number_of_radio]']).replace("u'","").replace("'",""))
				radios_val=radios_name=[]
				
				str_radio_val=str(new_dict['form['+str(i)+'][radios_value][]']).replace("u'","").replace("'","")
				str_radio_name=str(new_dict['form['+str(i)+'][radios_name][]']).replace("u'","").replace("'","")
			
				radios_value=str_radio_val.split(",")
				radios_name=str_radio_name.split(",")

				if ((new_dict['form['+str(i)+'][sub_type]']).replace("u'","").replace("'","")=='c'):
					input_box+='<div class="form-group"><label class="col-md-4 control-label"'
					input_box+='for="'+str(new_dict['form['+str(i)+'][name]']).replace("u'","").replace("'","")+'">'
					input_box+=str(new_dict['form['+str(i)+'][title]']).replace("u'","").replace("'","")
					input_box+='</label>'
					input_box+='<div class="col-md-4">'
					for j in range(num_of_radio):
						input_box+='<div class="checkbox"><label for="radio'+str(j)+'"'+'><input type="checkbox"'
						input_box+='name="'+str(new_dict['form['+str(i)+'][name]']).replace("u'","").replace("'","")+'"'
						input_box+='value="'+str(radios_value[j]).replace("u'","").replace("'","")+'">'
						input_box+=str(radios_name[j]).replace("u'","").replace("'","")+'</label></div>'
					input_box+='</div></div>'
	      		if ((new_dict['form['+str(i)+'][sub_type]']).replace("u'","").replace("'","")=='r'):
					num_of_radio=int((new_dict['form['+str(i)+'][number_of_radio]']).replace("u'","").replace("'",""))
					radios_val=radios_name=[]
					
					str_radio_val=str(new_dict['form['+str(i)+'][radios_value][]']).replace("u'","").replace("'","")
					str_radio_name=str(new_dict['form['+str(i)+'][radios_name][]']).replace("u'","").replace("'","")
				
					radios_value=str_radio_val.split(",")
					radios_name=str_radio_name.split(",")
					input_box+='<div class="form-group"><label class="col-md-4 control-label"'
					input_box+='for="'+str(new_dict['form['+str(i)+'][name]']).replace("u'","").replace("'","")+'">'
					input_box+=str(new_dict['form['+str(i)+'][title]']).replace("u'","").replace("'","")
					input_box+='</label>'
		  			input_box+='<div class="col-md-4">'
		  			for j in range(num_of_radio):
		  				input_box+='<div class="radio"><label for="radio'+str(j)+'"'+'><input type="radio"'
						input_box+='name="'+str(new_dict['form['+str(i)+'][name]']).replace("u'","").replace("'","")+'"'
						input_box+='value="'+str(radios_value[j]).replace("u'","").replace("'","")+'">'
						input_box+=str(radios_name[j]).replace("u'","").replace("'","")+'</label></div>'
					input_box+='</div></div>'
			if ((new_dict['form['+str(i)+'][sub_type]']).replace("u'","").replace("'","")=='s'):
				num_of_radio=int((new_dict['form['+str(i)+'][number_of_radio]']).replace("u'","").replace("'",""))
				radios_val=radios_name=[]
				
				str_radio_val=str(new_dict['form['+str(i)+'][radios_value][]']).replace("u'","").replace("'","")
				str_radio_name=str(new_dict['form['+str(i)+'][radios_name][]']).replace("u'","").replace("'","")
			
				radios_value=str_radio_val.split(",")
				radios_name=str_radio_name.split(",")

				input_box+='<div class="form-group"><label class="col-md-4 control-label"'
				input_box+='for="'+str(new_dict['form['+str(i)+'][name]']).replace("u'","").replace("'","")+'">'
				input_box+=str(new_dict['form['+str(i)+'][title]']).replace("u'","").replace("'","")
				input_box+='</label>'
				input_box+='<div class="col-md-4">'
				input_box+='<select id='+str(new_dict['form['+str(i)+'][name]']).replace("u'","").replace("'","")+' name='
				input_box+=str(new_dict['form['+str(i)+'][name]']).replace("u'","").replace("'","")+' class=form-control>'
				for j in range(num_of_radio):
					input_box+='<option value='+str(radios_value[j]).replace("u'","").replace("'","")+'>'
					input_box+=str(radios_name[j]).replace("u'","").replace("'","")
					input_box+='</option>'
				input_box+='</select></div></div>'
  		return input_box