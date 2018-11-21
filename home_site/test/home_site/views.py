from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context

from .forms import NameForm
from ctypes import *
import subprocess
from os import popen
import time
import os

# Create your views here.

def index(request):
        return render(request, 'home_site/index.html')


def form_function(request):
	
	
	if request.method == "POST":

		Anum=0
		Cnum=0
		Gnum=0
		Tnum=0
		ssize =0

		#return HttpResponse("success")
		#result = subprocess.check_output('ls -al | grep "user", shell=True)
		#p1 = subprocess.check_output("ifconfig",stdout=subprocess.PIPE)

		form2 = NameForm(request.POST)
		if form2.is_valid():
			cd2 = form2.cleaned_data
			#cd['test_variable']
			ex2 = cd2['test_variable']
		

		f = open('test.txt', 'w')


		#f = open('test.txt', 'w')
		#f.write(ex2)
		
		f.write('-1 2:1 6:1 17:1 24:1 38:1 42:1 50:1 64:1 71:1 73:1 74:1 76:1 82:1 83:1\n')
		#f.write('hhhh')
		f.close()
		
		
		svmc_exe = "svm-scale.exe -l 0 -u 1 -r a6a.range test.txt "+"> a6a.t.scale"
		popen(svmc_exe)
		time.sleep(5)


		svmp_exe_1 = "svm-predict.exe " 
		svmp_exe_2 = "a6a.t.scale "
		#svmp_exe_2 = "test.txt "
		svmp_exe_3 = "a6a.model " 
		svmp_exe_4 = "a6a.result"
		svmp_exe = svmp_exe_1+svmp_exe_2+svmp_exe_3+svmp_exe_4
		p1 = popen(svmp_exe)		
		#p1 = subprocess.check_output(["ipconfig","/all"], universal_newlines=True)






		form = NameForm(request.POST)
		#form = form + p1
		if form.is_valid():
			cd = form.cleaned_data
			#cd['test_variable']
			ex1 = cd['test_variable']
			#type(cd)
			#hh = int(ex1)
			#print(type(ex1))
			for i in ex1 :
    				ssize+=1
			for i in range(0,ssize,1):
				if ex1[i] == 'A' : Anum+=1
				if ex1[i] == 'C' : Cnum+=1
				if ex1[i] == 'G' : Gnum+=1
				if ex1[i] == 'T' : Tnum+=1
			AAA = "<p>"+ex1+"</p>" + "\n" + "A = " + str(Anum)+ ", C = " + str(Cnum)+ ", G = " + str(Gnum)+ ", T = "+str(Tnum)

			time_ck=0
			print("check point")
			yyy = False
			i=0
			j=1
			while True:
				time.sleep(2)
				i = os.path.getsize('a6a.result')
				time.sleep(3)
				j = os.path.getsize('a6a.result')
				if i==j and i != 0 and j != 0:
					break							
			

			file_read = open('a6a.result','r').read()



			return HttpResponse(file_read)



	else:
		f = NameForm()
		return render(request, "home_site/index.html", {'form': f})
#	try:
#		f = NameForm()
#		return render(request, "home_site/index.html", {'form': f})
#
#	except:
#		return HttpResponseNotFound(u'<h1>not access</h1>')
		

def doc_home(request):
    return render(request, 'home_site/aaa.html')


#def file_home(request):
#   return render(request, 'home_site/Supplementary Table 1.xlsx')

def file_home(request, scripts_id):
    scripts = get_object_or_404(Scripts, id=scripts_id)
    title = scripts.title.encode('euc-kr')
    response = HttpResponse(content_type='plain/text')
    response['Content-Disposition'] = 'attachment; filename=' + title
    response.write(scripts.contents.encode('euc-kr'))
    return response
