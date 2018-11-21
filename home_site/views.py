from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context

from .forms import NameForm
from .forms import NameForm_2

from ctypes import *
import subprocess
from os import popen
import time
import os
import math


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
			ex2 = cd2['Sequence']
		

		f = open('test_sequence_hg19.txt', 'w')


		
		# (human_hg19)
		residue_a = [0.0339020876279031, 0.123788876479506, 0.0261214885969252, 0.141659994018403, -0.0877227401220542,
            		 -0.197661507895266, 0.0219457356439961, 0.0253261978053977, 0.155774176530364, 0.121502461264815,
             		-0.0446054164377878, 0.0755844927266934, -0.0213822030028255, 0.241171784897495, -0.0663987515834963,
             		0.0652727925158541, 0.212215067123469, 0.09782174761623, 0.107733540927861, 0.0552399241311124,
             		0.0693319616268975, 0.0853220720550266, 0.106459725343324, 0.0968678832267071, 0.0992998057216273]
		residue_c = [-0.266056010814566, -0.480117402037125, -0.110111097458962, -0.137440985969591, -0.0627218202684861,
             		0.232254069222025, 0.0230640007496732, -0.0259508324990214, -0.141721784823212, -0.305095412946933,
             		-0.273076245868164, -0.29722312605788, -0.109688455393834, -0.242630272857486, -0.133809641075751,
             		-0.0486032885246652, -0.227628184622934, -0.0731223590327968, -0.178746342364583, -0.121953040803263,
             		-0.106764908204301, -0.0721557233716481, -0.12788288639316, -0.12346608613399, -0.0734712692277474]
		residue_g = [0.256001074506024, 0.282301880866723, 0.276190279780631, 0.154151149535032, 0.0443119095526713,
             		0.0151309077818889, -0.159608368890426, -0.151203264055423, -0.01329913888232, 0.236890754731803,
             		0.23372033594794, 0.162244744234689, 0.166517746895458, 0.0477371014541588, 0.0824540845073825,
             		-0.0567306558213953, -0.0495965911366149, -0.0600167396034346, -0.00151865320143668, -0.0451898186563374,
             		-0.0638298089213101, -0.130428204474034, -0.111056058134691, -0.106079024302638, -0.152592741396241]
		residue_t = [-0.073288985095525, -0.0330463897378403, -0.244309853869626, -0.192761709693736, 0.0980769293257618,
             		-0.0849377106943723, 0.102038334838977, 0.137002508455823, -0.0163661968827132, -0.113576372335072,
             		0.038476460790372, 0.0191580173630881, -0.0505362508949716, -0.0904919978300694, 0.103990273226776,
             		0.0361937023231806, 0.0303929460131021, 0.0285862203954056, 0.0566495770447523, 0.10146590131151,
             		0.0913682265608114, 0.10339636862204, 0.114144930753532, 0.115647924258474, 0.109381608261575]


		def isTest_1(text):
    			global abc_1
    			if text[0] == 'A' or text[0] == 'a':
        			abc_1 = residue_a[i]
        			return abc_1
    			if text[0] == 'C' or text[0] == 'c':
        			abc_1 = residue_c[i]
        			return abc_1
    			if text[0] == 'G' or text[0] == 'g':
        			abc_1 = residue_g[i]
        			return abc_1
    			if text[0] == 'T' or text[0] == 't':
        			abc_1 = residue_t[i]
        			return abc_1
    			if text[0] == 'N' or text[0] == 'n':
        			abc_1 = -0.1
        			return abc_1
        			

        			
		def isTest_2(text):
			global abc_2
			if text[0] == 'A' or text[0] == 'a':
				abc_2 = 0.4
				return abc_2
			if text[0] == 'C' or text[0] == 'c':
				abc_2 = 0.6
				return abc_2
			if text[0] == 'G' or text[0] == 'g':
				abc_2 = 0.6
				return abc_2
			if text[0] == 'T' or text[0] == 't':
				abc_2 = 0.4
				return abc_2
			if text[0] == 'N' or text[0] == 'n':
				abc_2 = 0.4
				return abc_2



		residue_HHH = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,]

		def isTest_3(text):
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-2.08)
				residue_HHH[0] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-3.08)
				residue_HHH[1] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.33)
				residue_HHH[2] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.31)
				residue_HHH[3] += zzz

			if text[0] == 'A' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.82)
				residue_HHH[4] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-4.01)
				residue_HHH[5] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.48)
				residue_HHH[6] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.33)
				residue_HHH[7] += zzz

			if text[0] == 'A' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-2.95)
				residue_HHH[8] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-3.99)
				residue_HHH[9] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.26)
				residue_HHH[10] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-3.33)
				residue_HHH[11] += zzz
				
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.39)
				residue_HHH[12] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.93)
				residue_HHH[13] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.05)
				residue_HHH[14] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.31)
				residue_HHH[15] += zzz



			if text[0] == 'C' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-1.82)
				residue_HHH[16] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-2.82)
				residue_HHH[17] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.07)
				residue_HHH[18] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.05)
				residue_HHH[19] += zzz

			if text[0] == 'C' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.75)
				residue_HHH[20] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-3.94)
				residue_HHH[21] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.41)
				residue_HHH[22] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.26)
				residue_HHH[23] += zzz

			if text[0] == 'C' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-3.1)
				residue_HHH[24] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-4.14)
				residue_HHH[25] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.41)
				residue_HHH[26] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-3.48)
				residue_HHH[27] += zzz

			if text[0] == 'C' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.41)
				residue_HHH[28] += zzz
				#residue_HHH.insert(28, zzz)
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.95)
				residue_HHH[29] += zzz
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.07)
				residue_HHH[30] += zzz
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.33)
				residue_HHH[31] += zzz




			if text[0] == 'G' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-2.7)
				residue_HHH[32] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-3.7)
				residue_HHH[33] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.95)
				residue_HHH[34] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.93)
				residue_HHH[35] += zzz

			if text[0] == 'G' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-3.48)
				residue_HHH[36] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-4.67)
				residue_HHH[37] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-4.14)
				residue_HHH[38] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.99)
				residue_HHH[39] += zzz

			if text[0] == 'G' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-3.63)
				residue_HHH[40] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-4.67)
				residue_HHH[41] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.94)
				residue_HHH[42] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-4.01)
				residue_HHH[43] += zzz

			if text[0] == 'G' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-2.16)
				residue_HHH[44] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-3.7)
				residue_HHH[45] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.82)
				residue_HHH[46] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-3.08)
				residue_HHH[47] += zzz




			if text[0] == 'T' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-1.16)
				residue_HHH[48] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-2.16)
				residue_HHH[49] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-1.41)
				residue_HHH[50] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-1.39)
				residue_HHH[51] += zzz

			if text[0] == 'T' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.44)
				residue_HHH[52] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-3.63)
				residue_HHH[53] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.1)
				residue_HHH[54] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-2.95)
				residue_HHH[55] += zzz

			if text[0] == 'T' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-2.44)
				residue_HHH[56] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-3.48)
				residue_HHH[57] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-2.75)
				residue_HHH[58] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-2.82)
				residue_HHH[59] += zzz

			if text[0] == 'T' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.16)
				residue_HHH[60] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.7)
				residue_HHH[61] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-1.82)
				residue_HHH[62] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.08)
				residue_HHH[63] += zzz




		cg_ct = [1,1]
		residue_gg_tt = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
		
		def isTest_4(text):
			if text[0] == 'G' and text[1] == 'G':
				cg_ct[0] = cg_ct[0]+1
				residue_gg_tt[ff] += (0.04) * (cg_ct[0])
			elif text[0] == 'G' and text[1] != 'G':
				residue_gg_tt[ff] += (0.04) * 1
			elif text[0] == 'T' and text[1] == 'T':
				cg_ct[1] = cg_ct[1]+1
				residue_gg_tt[ff] += math.exp(cg_ct[1]) / (math.exp(cg_ct[1]) +1)
			elif text[0] == 'T' and text[1] != 'T':
				residue_gg_tt[ff] += math.exp(1) / (math.exp(1)+1)
			elif text[0] == 'N' or text[0] == 'M' or text[0] == 'R':
				asdfsdf =5
			else:
				residue_gg_tt[ff] += 0









		f.write("1 ")
		print('\n-------1-------')

		for i in range(len(ex2)):
			chunk_1 = ex2[i:i + 1]
			if isTest_1(chunk_1):
				print(abc_1)
			f.write("%d:%f " % (i+1, abc_1))


		print('\n-------2------')

		for a in range(len(ex2)):  
			chunk_2 = ex2[a:a + 1]
			if isTest_2(chunk_2):
				print(abc_2)
			f.write("%d:%f " % (a+26, abc_2))

		print('\n-------3------')
		
		for a in range(len(ex2) - 2):
			chunk_3 = ex2[a:a + 3]
			isTest_3(chunk_3)
			# print(abc_3)
			
		for aa in range(64):
			print(residue_HHH[aa])
			f.write("%d:%f " % (aa + 51, residue_HHH[aa]))


		print('\n-------4------')
		
		for ff in range(len(ex2) - 1):
			chunk_4 = ex2[ff:ff + 2]
			isTest_4(chunk_4)
			
		for uu in range(24):
			print(residue_gg_tt[uu])
			f.write("%d:%f " % (uu + 115, residue_gg_tt[uu]))

		f.write("\n")



	
		#f.write('-1 2:1 6:1 17:1 24:1 38:1 42:1 50:1 64:1 71:1 73:1 74:1 76:1 82:1 83:1\n')
		#f.write('hhhh')
		f.close()
		

	
		
		svmc_exe = "svm-scale.exe -l 0 -u 1 -r train_model_hg19.range test_sequence_hg19.txt "+"> test_sequence_hg19.t.scale"
		popen(svmc_exe)
		time.sleep(5)


		svmp_exe_1 = "svm-predict_cutoffmod.exe " 
		svmp_exe_2 = "test_sequence_hg19.t.scale "
		#svmp_exe_2 = "test_sequence_hg19.txt "
		svmp_exe_3 = "train_model_hg19.model " 
		svmp_exe_4 = "sequence_hg19.result"
		svmp_exe = svmp_exe_1+svmp_exe_2+svmp_exe_3+svmp_exe_4
		p1 = popen(svmp_exe)		
		#p1 = subprocess.check_output(["ipconfig","/all"], universal_newlines=True)






		form = NameForm(request.POST)
		#form = form + p1
		if form.is_valid():
			cd = form.cleaned_data
			#cd['test_variable']
			ex1 = cd['Sequence']
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
				i = os.path.getsize('sequence_hg19.result')
				time.sleep(3)
				j = os.path.getsize('sequence_hg19.result')
				if i==j and i != 0 and j != 0:
					break							
			

			file_read = open('sequence_hg19.result','r').read()



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
		


def form_function_2(request):
	
	
	if request.method == "POST":

		Anum=0
		Cnum=0
		Gnum=0
		Tnum=0
		ssize =0

		#return HttpResponse("success")
		#result = subprocess.check_output('ls -al | grep "user", shell=True)
		#p1 = subprocess.check_output("ifconfig",stdout=subprocess.PIPE)

		form2 = NameForm_2(request.POST)
		if form2.is_valid():
			cd2 = form2.cleaned_data
			#cd['test_variable']
			ex2 = cd2['Sequence_2']
		

		f = open('test_sequence_hg19.txt', 'w')

		nnn_1 = 'NNNNNNNNNNNN'
		nnn_2 = 'NNNNNNNNNNNN'

		nnn_1 = nnn_1 + ex2
		ex3 = nnn_1 + nnn_2

		
		# (human_hg19)
		residue_a = [0.0339020876279031, 0.123788876479506, 0.0261214885969252, 0.141659994018403, -0.0877227401220542,
            		 -0.197661507895266, 0.0219457356439961, 0.0253261978053977, 0.155774176530364, 0.121502461264815,
             		-0.0446054164377878, 0.0755844927266934, -0.0213822030028255, 0.241171784897495, -0.0663987515834963,
             		0.0652727925158541, 0.212215067123469, 0.09782174761623, 0.107733540927861, 0.0552399241311124,
             		0.0693319616268975, 0.0853220720550266, 0.106459725343324, 0.0968678832267071, 0.0992998057216273]
		residue_c = [-0.266056010814566, -0.480117402037125, -0.110111097458962, -0.137440985969591, -0.0627218202684861,
             		0.232254069222025, 0.0230640007496732, -0.0259508324990214, -0.141721784823212, -0.305095412946933,
             		-0.273076245868164, -0.29722312605788, -0.109688455393834, -0.242630272857486, -0.133809641075751,
             		-0.0486032885246652, -0.227628184622934, -0.0731223590327968, -0.178746342364583, -0.121953040803263,
             		-0.106764908204301, -0.0721557233716481, -0.12788288639316, -0.12346608613399, -0.0734712692277474]
		residue_g = [0.256001074506024, 0.282301880866723, 0.276190279780631, 0.154151149535032, 0.0443119095526713,
             		0.0151309077818889, -0.159608368890426, -0.151203264055423, -0.01329913888232, 0.236890754731803,
             		0.23372033594794, 0.162244744234689, 0.166517746895458, 0.0477371014541588, 0.0824540845073825,
             		-0.0567306558213953, -0.0495965911366149, -0.0600167396034346, -0.00151865320143668, -0.0451898186563374,
             		-0.0638298089213101, -0.130428204474034, -0.111056058134691, -0.106079024302638, -0.152592741396241]
		residue_t = [-0.073288985095525, -0.0330463897378403, -0.244309853869626, -0.192761709693736, 0.0980769293257618,
             		-0.0849377106943723, 0.102038334838977, 0.137002508455823, -0.0163661968827132, -0.113576372335072,
             		0.038476460790372, 0.0191580173630881, -0.0505362508949716, -0.0904919978300694, 0.103990273226776,
             		0.0361937023231806, 0.0303929460131021, 0.0285862203954056, 0.0566495770447523, 0.10146590131151,
             		0.0913682265608114, 0.10339636862204, 0.114144930753532, 0.115647924258474, 0.109381608261575]


		def isTest_1(text):
    			global abc_1
    			if text[0] == 'A' or text[0] == 'a':
        			abc_1 = residue_a[i]
        			return abc_1
    			if text[0] == 'C' or text[0] == 'c':
        			abc_1 = residue_c[i]
        			return abc_1
    			if text[0] == 'G' or text[0] == 'g':
        			abc_1 = residue_g[i]
        			return abc_1
    			if text[0] == 'T' or text[0] == 't':
        			abc_1 = residue_t[i]
        			return abc_1
    			if text[0] == 'N' or text[0] == 'n':
        			abc_1 = -0.1
        			return abc_1
        			

        			
		def isTest_2(text):
			global abc_2
			if text[0] == 'A' or text[0] == 'a':
				abc_2 = 0.4
				return abc_2
			if text[0] == 'C' or text[0] == 'c':
				abc_2 = 0.6
				return abc_2
			if text[0] == 'G' or text[0] == 'g':
				abc_2 = 0.6
				return abc_2
			if text[0] == 'T' or text[0] == 't':
				abc_2 = 0.4
				return abc_2
			if text[0] == 'N' or text[0] == 'n':
				abc_2 = 0.4
				return abc_2



		residue_HHH = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,]

		def isTest_3(text):
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-2.08)
				residue_HHH[0] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-3.08)
				residue_HHH[1] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.33)
				residue_HHH[2] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.31)
				residue_HHH[3] += zzz

			if text[0] == 'A' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.82)
				residue_HHH[4] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-4.01)
				residue_HHH[5] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.48)
				residue_HHH[6] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.33)
				residue_HHH[7] += zzz

			if text[0] == 'A' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-2.95)
				residue_HHH[8] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-3.99)
				residue_HHH[9] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.26)
				residue_HHH[10] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-3.33)
				residue_HHH[11] += zzz
				
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.39)
				residue_HHH[12] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.93)
				residue_HHH[13] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.05)
				residue_HHH[14] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.31)
				residue_HHH[15] += zzz



			if text[0] == 'C' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-1.82)
				residue_HHH[16] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-2.82)
				residue_HHH[17] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.07)
				residue_HHH[18] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.05)
				residue_HHH[19] += zzz

			if text[0] == 'C' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.75)
				residue_HHH[20] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-3.94)
				residue_HHH[21] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.41)
				residue_HHH[22] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.26)
				residue_HHH[23] += zzz

			if text[0] == 'C' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-3.1)
				residue_HHH[24] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-4.14)
				residue_HHH[25] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.41)
				residue_HHH[26] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-3.48)
				residue_HHH[27] += zzz

			if text[0] == 'C' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.41)
				residue_HHH[28] += zzz
				#residue_HHH.insert(28, zzz)
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.95)
				residue_HHH[29] += zzz
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.07)
				residue_HHH[30] += zzz
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.33)
				residue_HHH[31] += zzz




			if text[0] == 'G' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-2.7)
				residue_HHH[32] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-3.7)
				residue_HHH[33] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.95)
				residue_HHH[34] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.93)
				residue_HHH[35] += zzz

			if text[0] == 'G' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-3.48)
				residue_HHH[36] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-4.67)
				residue_HHH[37] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-4.14)
				residue_HHH[38] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.99)
				residue_HHH[39] += zzz

			if text[0] == 'G' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-3.63)
				residue_HHH[40] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-4.67)
				residue_HHH[41] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.94)
				residue_HHH[42] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-4.01)
				residue_HHH[43] += zzz

			if text[0] == 'G' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-2.16)
				residue_HHH[44] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-3.7)
				residue_HHH[45] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.82)
				residue_HHH[46] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-3.08)
				residue_HHH[47] += zzz




			if text[0] == 'T' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-1.16)
				residue_HHH[48] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-2.16)
				residue_HHH[49] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-1.41)
				residue_HHH[50] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-1.39)
				residue_HHH[51] += zzz

			if text[0] == 'T' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.44)
				residue_HHH[52] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-3.63)
				residue_HHH[53] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.1)
				residue_HHH[54] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-2.95)
				residue_HHH[55] += zzz

			if text[0] == 'T' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-2.44)
				residue_HHH[56] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-3.48)
				residue_HHH[57] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-2.75)
				residue_HHH[58] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-2.82)
				residue_HHH[59] += zzz

			if text[0] == 'T' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.16)
				residue_HHH[60] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.7)
				residue_HHH[61] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-1.82)
				residue_HHH[62] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.08)
				residue_HHH[63] += zzz




		cg_ct = [1,1]
		residue_gg_tt = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
		
		def isTest_4(text):
			if text[0] == 'G' and text[1] == 'G':
				cg_ct[0] = cg_ct[0]+1
				residue_gg_tt[ff] += (0.04) * (cg_ct[0])
			elif text[0] == 'G' and text[1] != 'G':
				residue_gg_tt[ff] += (0.04) * 1
			elif text[0] == 'T' and text[1] == 'T':
				cg_ct[1] = cg_ct[1]+1
				residue_gg_tt[ff] += math.exp(cg_ct[1]) / (math.exp(cg_ct[1]) +1)
			elif text[0] == 'T' and text[1] != 'T':
				residue_gg_tt[ff] += math.exp(1) / (math.exp(1)+1)
			elif text[0] == 'N' or text[0] == 'M' or text[0] == 'R':
				asdfsdf =5
			else:
				residue_gg_tt[ff] += 0
		
		
		sequence_p = []
		for a in range(len(ex3)):
			chunk_3 = ex3[a:a+25]
			if len(chunk_3) < 25:
				break
			sequence_p.append(chunk_3)
		
		
		
		for jj in range(len(ex2)):
			f.write("1 ")
			print('\n-------1-------')

			for i in range(len(sequence_p[jj])):
				chunk_1 = sequence_p[jj][i:i + 1]
				if isTest_1(chunk_1):
					print(abc_1)
				f.write("%d:%f " % (i+1, abc_1))


			print('\n-------2------')

			for a in range(len(sequence_p[jj])):  
				chunk_2 = sequence_p[jj][a:a + 1]
				if isTest_2(chunk_2):
					print(abc_2)
				f.write("%d:%f " % (a+26, abc_2))

			print('\n-------3------')
		
			for a in range(len(sequence_p[jj]) - 2):
				chunk_3 = sequence_p[jj][a:a + 3]
				isTest_3(chunk_3)
				# print(abc_3)
			
			for aa in range(64):
				print(residue_HHH[aa])
				f.write("%d:%f " % (aa + 51, residue_HHH[aa]))


			print('\n-------4------')
		
			for ff in range(len(sequence_p[jj]) - 1):
				chunk_4 = sequence_p[jj][ff:ff + 2]
				isTest_4(chunk_4)
			
			for uu in range(24):
				print(residue_gg_tt[uu])
				f.write("%d:%f " % (uu + 115, residue_gg_tt[uu]))

			f.write("\n")
			cg_ct = [1, 1]
			residue_gg_tt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
			
			residue_HHH.clear()
			for hh in range(64):
				residue_HHH.append(0)


	
		#f.write('-1 2:1 6:1 17:1 24:1 38:1 42:1 50:1 64:1 71:1 73:1 74:1 76:1 82:1 83:1\n')
		#f.write('hhhh')
		f.close()
		

	
		
		svmc_exe = "svm-scale.exe -l 0 -u 1 -r train_model_hg19.range test_sequence_hg19.txt "+"> test_sequence_hg19.t.scale"
		popen(svmc_exe)
		time.sleep(5)


		svmp_exe_1 = "svm-predict_cutoffmod.exe " 
		svmp_exe_2 = "test_sequence_hg19.t.scale "
		#svmp_exe_2 = "test_sequence_hg19.txt "
		svmp_exe_3 = "train_model_hg19.model " 
		svmp_exe_4 = "sequence_hg19.result"
		svmp_exe = svmp_exe_1+svmp_exe_2+svmp_exe_3+svmp_exe_4
		p1 = popen(svmp_exe)		
		#p1 = subprocess.check_output(["ipconfig","/all"], universal_newlines=True)






		form = NameForm_2(request.POST)
		#form = form + p1
		if form.is_valid():
			cd = form.cleaned_data
			#cd['test_variable']
			ex1 = cd['Sequence_2']
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
				i = os.path.getsize('sequence_hg19.result')
				time.sleep(10)
				j = os.path.getsize('sequence_hg19.result')
				if i==j and i != 0 and j != 0:
					break							
			

			file_read = open('sequence_hg19.result','r').read()



			return HttpResponse(file_read)



	else:
		f = NameForm_2()
		return render(request, "home_site/human_long.html", {'form': f})
#	try:
#		f = NameForm()
#		return render(request, "home_site/index.html", {'form': f})
#
#	except:
#		return HttpResponseNotFound(u'<h1>not access</h1>')








def form_function_3(request):
	
	
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
			ex2 = cd2['Sequence']
		

		f = open('test_sequence_mm10.txt', 'w')


		
		# (human_hg19)
		residue_a = [0.0339020876279031, 0.123788876479506, 0.0261214885969252, 0.141659994018403, -0.0877227401220542,
            		 -0.197661507895266, 0.0219457356439961, 0.0253261978053977, 0.155774176530364, 0.121502461264815,
             		-0.0446054164377878, 0.0755844927266934, -0.0213822030028255, 0.241171784897495, -0.0663987515834963,
             		0.0652727925158541, 0.212215067123469, 0.09782174761623, 0.107733540927861, 0.0552399241311124,
             		0.0693319616268975, 0.0853220720550266, 0.106459725343324, 0.0968678832267071, 0.0992998057216273]
		residue_c = [-0.266056010814566, -0.480117402037125, -0.110111097458962, -0.137440985969591, -0.0627218202684861,
             		0.232254069222025, 0.0230640007496732, -0.0259508324990214, -0.141721784823212, -0.305095412946933,
             		-0.273076245868164, -0.29722312605788, -0.109688455393834, -0.242630272857486, -0.133809641075751,
             		-0.0486032885246652, -0.227628184622934, -0.0731223590327968, -0.178746342364583, -0.121953040803263,
             		-0.106764908204301, -0.0721557233716481, -0.12788288639316, -0.12346608613399, -0.0734712692277474]
		residue_g = [0.256001074506024, 0.282301880866723, 0.276190279780631, 0.154151149535032, 0.0443119095526713,
             		0.0151309077818889, -0.159608368890426, -0.151203264055423, -0.01329913888232, 0.236890754731803,
             		0.23372033594794, 0.162244744234689, 0.166517746895458, 0.0477371014541588, 0.0824540845073825,
             		-0.0567306558213953, -0.0495965911366149, -0.0600167396034346, -0.00151865320143668, -0.0451898186563374,
             		-0.0638298089213101, -0.130428204474034, -0.111056058134691, -0.106079024302638, -0.152592741396241]
		residue_t = [-0.073288985095525, -0.0330463897378403, -0.244309853869626, -0.192761709693736, 0.0980769293257618,
             		-0.0849377106943723, 0.102038334838977, 0.137002508455823, -0.0163661968827132, -0.113576372335072,
             		0.038476460790372, 0.0191580173630881, -0.0505362508949716, -0.0904919978300694, 0.103990273226776,
             		0.0361937023231806, 0.0303929460131021, 0.0285862203954056, 0.0566495770447523, 0.10146590131151,
             		0.0913682265608114, 0.10339636862204, 0.114144930753532, 0.115647924258474, 0.109381608261575]


		def isTest_1(text):
    			global abc_1
    			if text[0] == 'A' or text[0] == 'a':
        			abc_1 = residue_a[i]
        			return abc_1
    			if text[0] == 'C' or text[0] == 'c':
        			abc_1 = residue_c[i]
        			return abc_1
    			if text[0] == 'G' or text[0] == 'g':
        			abc_1 = residue_g[i]
        			return abc_1
    			if text[0] == 'T' or text[0] == 't':
        			abc_1 = residue_t[i]
        			return abc_1
    			if text[0] == 'N' or text[0] == 'n':
        			abc_1 = -0.1
        			return abc_1
        			

        			
		def isTest_2(text):
			global abc_2
			if text[0] == 'A' or text[0] == 'a':
				abc_2 = 0.4
				return abc_2
			if text[0] == 'C' or text[0] == 'c':
				abc_2 = 0.6
				return abc_2
			if text[0] == 'G' or text[0] == 'g':
				abc_2 = 0.6
				return abc_2
			if text[0] == 'T' or text[0] == 't':
				abc_2 = 0.4
				return abc_2
			if text[0] == 'N' or text[0] == 'n':
				abc_2 = 0.4
				return abc_2



		residue_HHH = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,]

		def isTest_3(text):
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-2.08)
				residue_HHH[0] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-3.08)
				residue_HHH[1] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.33)
				residue_HHH[2] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.31)
				residue_HHH[3] += zzz

			if text[0] == 'A' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.82)
				residue_HHH[4] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-4.01)
				residue_HHH[5] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.48)
				residue_HHH[6] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.33)
				residue_HHH[7] += zzz

			if text[0] == 'A' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-2.95)
				residue_HHH[8] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-3.99)
				residue_HHH[9] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.26)
				residue_HHH[10] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-3.33)
				residue_HHH[11] += zzz
				
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.39)
				residue_HHH[12] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.93)
				residue_HHH[13] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.05)
				residue_HHH[14] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.31)
				residue_HHH[15] += zzz



			if text[0] == 'C' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-1.82)
				residue_HHH[16] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-2.82)
				residue_HHH[17] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.07)
				residue_HHH[18] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.05)
				residue_HHH[19] += zzz

			if text[0] == 'C' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.75)
				residue_HHH[20] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-3.94)
				residue_HHH[21] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.41)
				residue_HHH[22] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.26)
				residue_HHH[23] += zzz

			if text[0] == 'C' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-3.1)
				residue_HHH[24] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-4.14)
				residue_HHH[25] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.41)
				residue_HHH[26] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-3.48)
				residue_HHH[27] += zzz

			if text[0] == 'C' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.41)
				residue_HHH[28] += zzz
				#residue_HHH.insert(28, zzz)
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.95)
				residue_HHH[29] += zzz
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.07)
				residue_HHH[30] += zzz
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.33)
				residue_HHH[31] += zzz




			if text[0] == 'G' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-2.7)
				residue_HHH[32] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-3.7)
				residue_HHH[33] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.95)
				residue_HHH[34] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.93)
				residue_HHH[35] += zzz

			if text[0] == 'G' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-3.48)
				residue_HHH[36] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-4.67)
				residue_HHH[37] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-4.14)
				residue_HHH[38] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.99)
				residue_HHH[39] += zzz

			if text[0] == 'G' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-3.63)
				residue_HHH[40] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-4.67)
				residue_HHH[41] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.94)
				residue_HHH[42] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-4.01)
				residue_HHH[43] += zzz

			if text[0] == 'G' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-2.16)
				residue_HHH[44] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-3.7)
				residue_HHH[45] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.82)
				residue_HHH[46] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-3.08)
				residue_HHH[47] += zzz




			if text[0] == 'T' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-1.16)
				residue_HHH[48] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-2.16)
				residue_HHH[49] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-1.41)
				residue_HHH[50] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-1.39)
				residue_HHH[51] += zzz

			if text[0] == 'T' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.44)
				residue_HHH[52] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-3.63)
				residue_HHH[53] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.1)
				residue_HHH[54] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-2.95)
				residue_HHH[55] += zzz

			if text[0] == 'T' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-2.44)
				residue_HHH[56] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-3.48)
				residue_HHH[57] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-2.75)
				residue_HHH[58] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-2.82)
				residue_HHH[59] += zzz

			if text[0] == 'T' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.16)
				residue_HHH[60] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.7)
				residue_HHH[61] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-1.82)
				residue_HHH[62] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.08)
				residue_HHH[63] += zzz




		cg_ct = [1,1]
		residue_gg_tt = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
		
		def isTest_4(text):
			if text[0] == 'G' and text[1] == 'G':
				cg_ct[0] = cg_ct[0]+1
				residue_gg_tt[ff] += (0.04) * (cg_ct[0])
			elif text[0] == 'G' and text[1] != 'G':
				residue_gg_tt[ff] += (0.04) * 1
			elif text[0] == 'T' and text[1] == 'T':
				cg_ct[1] = cg_ct[1]+1
				residue_gg_tt[ff] += math.exp(cg_ct[1]) / (math.exp(cg_ct[1]) +1)
			elif text[0] == 'T' and text[1] != 'T':
				residue_gg_tt[ff] += math.exp(1) / (math.exp(1)+1)
			elif text[0] == 'N' or text[0] == 'M' or text[0] == 'R':
				asdfsdf =5
			else:
				residue_gg_tt[ff] += 0









		f.write("1 ")
		print('\n-------1-------')

		for i in range(len(ex2)):
			chunk_1 = ex2[i:i + 1]
			if isTest_1(chunk_1):
				print(abc_1)
			f.write("%d:%f " % (i+1, abc_1))


		print('\n-------2------')

		for a in range(len(ex2)):  
			chunk_2 = ex2[a:a + 1]
			if isTest_2(chunk_2):
				print(abc_2)
			f.write("%d:%f " % (a+26, abc_2))

		print('\n-------3------')
		
		for a in range(len(ex2) - 2):
			chunk_3 = ex2[a:a + 3]
			isTest_3(chunk_3)
			# print(abc_3)
			
		for aa in range(64):
			print(residue_HHH[aa])
			f.write("%d:%f " % (aa + 51, residue_HHH[aa]))


		print('\n-------4------')
		
		for ff in range(len(ex2) - 1):
			chunk_4 = ex2[ff:ff + 2]
			isTest_4(chunk_4)
			
		for uu in range(24):
			print(residue_gg_tt[uu])
			f.write("%d:%f " % (uu + 115, residue_gg_tt[uu]))

		f.write("\n")



	
		#f.write('-1 2:1 6:1 17:1 24:1 38:1 42:1 50:1 64:1 71:1 73:1 74:1 76:1 82:1 83:1\n')
		#f.write('hhhh')
		f.close()
		

	
		
		svmc_exe = "svm-scale.exe -l 0 -u 1 -r train_model_mm10.range test_sequence_mm10.txt "+"> test_sequence_mm10.t.scale"
		popen(svmc_exe)
		time.sleep(5)


		svmp_exe_1 = "svm-predict_cutoffmod.exe " 
		svmp_exe_2 = "test_sequence_mm10.t.scale "
		#svmp_exe_2 = "test_sequence_mm10.txt "
		svmp_exe_3 = "train_model_mm10.model " 
		svmp_exe_4 = "sequence_mm10.result"
		svmp_exe = svmp_exe_1+svmp_exe_2+svmp_exe_3+svmp_exe_4
		p1 = popen(svmp_exe)		
		#p1 = subprocess.check_output(["ipconfig","/all"], universal_newlines=True)






		form = NameForm(request.POST)
		#form = form + p1
		if form.is_valid():
			cd = form.cleaned_data
			#cd['test_variable']
			ex1 = cd['Sequence']
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
				i = os.path.getsize('sequence_mm10.result')
				time.sleep(3)
				j = os.path.getsize('sequence_mm10.result')
				if i==j and i != 0 and j != 0:
					break							
			

			file_read = open('sequence_mm10.result','r').read()



			return HttpResponse(file_read)



	else:
		f = NameForm()
		return render(request, "home_site/mouse_25bp.html", {'form': f})
#	try:
#		f = NameForm()
#		return render(request, "home_site/index.html", {'form': f})
#
#	except:
#		return HttpResponseNotFound(u'<h1>not access</h1>')
		


def form_function_4(request):
	
	
	if request.method == "POST":

		Anum=0
		Cnum=0
		Gnum=0
		Tnum=0
		ssize =0

		#return HttpResponse("success")
		#result = subprocess.check_output('ls -al | grep "user", shell=True)
		#p1 = subprocess.check_output("ifconfig",stdout=subprocess.PIPE)

		form2 = NameForm_2(request.POST)
		if form2.is_valid():
			cd2 = form2.cleaned_data
			#cd['test_variable']
			ex2 = cd2['Sequence_2']
		

		f = open('test_sequence_mm10.txt', 'w')

		nnn_1 = 'NNNNNNNNNNNN'
		nnn_2 = 'NNNNNNNNNNNN'

		nnn_1 = nnn_1 + ex2
		ex3 = nnn_1 + nnn_2

		
		# (human_hg19)
		residue_a = [0.0339020876279031, 0.123788876479506, 0.0261214885969252, 0.141659994018403, -0.0877227401220542,
            		 -0.197661507895266, 0.0219457356439961, 0.0253261978053977, 0.155774176530364, 0.121502461264815,
             		-0.0446054164377878, 0.0755844927266934, -0.0213822030028255, 0.241171784897495, -0.0663987515834963,
             		0.0652727925158541, 0.212215067123469, 0.09782174761623, 0.107733540927861, 0.0552399241311124,
             		0.0693319616268975, 0.0853220720550266, 0.106459725343324, 0.0968678832267071, 0.0992998057216273]
		residue_c = [-0.266056010814566, -0.480117402037125, -0.110111097458962, -0.137440985969591, -0.0627218202684861,
             		0.232254069222025, 0.0230640007496732, -0.0259508324990214, -0.141721784823212, -0.305095412946933,
             		-0.273076245868164, -0.29722312605788, -0.109688455393834, -0.242630272857486, -0.133809641075751,
             		-0.0486032885246652, -0.227628184622934, -0.0731223590327968, -0.178746342364583, -0.121953040803263,
             		-0.106764908204301, -0.0721557233716481, -0.12788288639316, -0.12346608613399, -0.0734712692277474]
		residue_g = [0.256001074506024, 0.282301880866723, 0.276190279780631, 0.154151149535032, 0.0443119095526713,
             		0.0151309077818889, -0.159608368890426, -0.151203264055423, -0.01329913888232, 0.236890754731803,
             		0.23372033594794, 0.162244744234689, 0.166517746895458, 0.0477371014541588, 0.0824540845073825,
             		-0.0567306558213953, -0.0495965911366149, -0.0600167396034346, -0.00151865320143668, -0.0451898186563374,
             		-0.0638298089213101, -0.130428204474034, -0.111056058134691, -0.106079024302638, -0.152592741396241]
		residue_t = [-0.073288985095525, -0.0330463897378403, -0.244309853869626, -0.192761709693736, 0.0980769293257618,
             		-0.0849377106943723, 0.102038334838977, 0.137002508455823, -0.0163661968827132, -0.113576372335072,
             		0.038476460790372, 0.0191580173630881, -0.0505362508949716, -0.0904919978300694, 0.103990273226776,
             		0.0361937023231806, 0.0303929460131021, 0.0285862203954056, 0.0566495770447523, 0.10146590131151,
             		0.0913682265608114, 0.10339636862204, 0.114144930753532, 0.115647924258474, 0.109381608261575]


		def isTest_1(text):
    			global abc_1
    			if text[0] == 'A' or text[0] == 'a':
        			abc_1 = residue_a[i]
        			return abc_1
    			if text[0] == 'C' or text[0] == 'c':
        			abc_1 = residue_c[i]
        			return abc_1
    			if text[0] == 'G' or text[0] == 'g':
        			abc_1 = residue_g[i]
        			return abc_1
    			if text[0] == 'T' or text[0] == 't':
        			abc_1 = residue_t[i]
        			return abc_1
    			if text[0] == 'N' or text[0] == 'n':
        			abc_1 = -0.1
        			return abc_1
        			

        			
		def isTest_2(text):
			global abc_2
			if text[0] == 'A' or text[0] == 'a':
				abc_2 = 0.4
				return abc_2
			if text[0] == 'C' or text[0] == 'c':
				abc_2 = 0.6
				return abc_2
			if text[0] == 'G' or text[0] == 'g':
				abc_2 = 0.6
				return abc_2
			if text[0] == 'T' or text[0] == 't':
				abc_2 = 0.4
				return abc_2
			if text[0] == 'N' or text[0] == 'n':
				abc_2 = 0.4
				return abc_2



		residue_HHH = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,]

		def isTest_3(text):
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-2.08)
				residue_HHH[0] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-3.08)
				residue_HHH[1] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.33)
				residue_HHH[2] += zzz
			if text[0] == 'A' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.31)
				residue_HHH[3] += zzz

			if text[0] == 'A' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.82)
				residue_HHH[4] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-4.01)
				residue_HHH[5] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.48)
				residue_HHH[6] += zzz
			if text[0] == 'A' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.33)
				residue_HHH[7] += zzz

			if text[0] == 'A' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-2.95)
				residue_HHH[8] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-3.99)
				residue_HHH[9] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.26)
				residue_HHH[10] += zzz
			if text[0] == 'A' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-3.33)
				residue_HHH[11] += zzz
				
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.39)
				residue_HHH[12] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.93)
				residue_HHH[13] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.05)
				residue_HHH[14] += zzz
			if text[0] == 'A' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.31)
				residue_HHH[15] += zzz



			if text[0] == 'C' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-1.82)
				residue_HHH[16] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-2.82)
				residue_HHH[17] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.07)
				residue_HHH[18] += zzz
			if text[0] == 'C' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.05)
				residue_HHH[19] += zzz

			if text[0] == 'C' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.75)
				residue_HHH[20] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-3.94)
				residue_HHH[21] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.41)
				residue_HHH[22] += zzz
			if text[0] == 'C' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.26)
				residue_HHH[23] += zzz

			if text[0] == 'C' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-3.1)
				residue_HHH[24] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-4.14)
				residue_HHH[25] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.41)
				residue_HHH[26] += zzz
			if text[0] == 'C' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-3.48)
				residue_HHH[27] += zzz

			if text[0] == 'C' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.41)
				residue_HHH[28] += zzz
				#residue_HHH.insert(28, zzz)
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.95)
				residue_HHH[29] += zzz
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.07)
				residue_HHH[30] += zzz
			if text[0] == 'C' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.33)
				residue_HHH[31] += zzz




			if text[0] == 'G' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-2.7)
				residue_HHH[32] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-3.7)
				residue_HHH[33] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-2.95)
				residue_HHH[34] += zzz
			if text[0] == 'G' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-2.93)
				residue_HHH[35] += zzz

			if text[0] == 'G' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-3.48)
				residue_HHH[36] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-4.67)
				residue_HHH[37] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-4.14)
				residue_HHH[38] += zzz
			if text[0] == 'G' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-3.99)
				residue_HHH[39] += zzz

			if text[0] == 'G' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-3.63)
				residue_HHH[40] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-4.67)
				residue_HHH[41] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-3.94)
				residue_HHH[42] += zzz
			if text[0] == 'G' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-4.01)
				residue_HHH[43] += zzz

			if text[0] == 'G' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-2.16)
				residue_HHH[44] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-3.7)
				residue_HHH[45] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-2.82)
				residue_HHH[46] += zzz
			if text[0] == 'G' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-3.08)
				residue_HHH[47] += zzz




			if text[0] == 'T' and text[1] == 'A' and text[2] == 'A':
				zzz = math.exp(-1.16)
				residue_HHH[48] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'C':
				zzz = math.exp(-2.16)
				residue_HHH[49] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'G':
				zzz = math.exp(-1.41)
				residue_HHH[50] += zzz
			if text[0] == 'T' and text[1] == 'A' and text[2] == 'T':
				zzz = math.exp(-1.39)
				residue_HHH[51] += zzz

			if text[0] == 'T' and text[1] == 'C' and text[2] == 'A':
				zzz = math.exp(-2.44)
				residue_HHH[52] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'C':
				zzz = math.exp(-3.63)
				residue_HHH[53] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'G':
				zzz = math.exp(-3.1)
				residue_HHH[54] += zzz
			if text[0] == 'T' and text[1] == 'C' and text[2] == 'T':
				zzz = math.exp(-2.95)
				residue_HHH[55] += zzz

			if text[0] == 'T' and text[1] == 'G' and text[2] == 'A':
				zzz = math.exp(-2.44)
				residue_HHH[56] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'C':
				zzz = math.exp(-3.48)
				residue_HHH[57] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'G':
				zzz = math.exp(-2.75)
				residue_HHH[58] += zzz
			if text[0] == 'T' and text[1] == 'G' and text[2] == 'T':
				zzz = math.exp(-2.82)
				residue_HHH[59] += zzz

			if text[0] == 'T' and text[1] == 'T' and text[2] == 'A':
				zzz = math.exp(-1.16)
				residue_HHH[60] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'C':
				zzz = math.exp(-2.7)
				residue_HHH[61] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'G':
				zzz = math.exp(-1.82)
				residue_HHH[62] += zzz
			if text[0] == 'T' and text[1] == 'T' and text[2] == 'T':
				zzz = math.exp(-2.08)
				residue_HHH[63] += zzz




		cg_ct = [1,1]
		residue_gg_tt = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
		
		def isTest_4(text):
			if text[0] == 'G' and text[1] == 'G':
				cg_ct[0] = cg_ct[0]+1
				residue_gg_tt[ff] += (0.04) * (cg_ct[0])
			elif text[0] == 'G' and text[1] != 'G':
				residue_gg_tt[ff] += (0.04) * 1
			elif text[0] == 'T' and text[1] == 'T':
				cg_ct[1] = cg_ct[1]+1
				residue_gg_tt[ff] += math.exp(cg_ct[1]) / (math.exp(cg_ct[1]) +1)
			elif text[0] == 'T' and text[1] != 'T':
				residue_gg_tt[ff] += math.exp(1) / (math.exp(1)+1)
			elif text[0] == 'N' or text[0] == 'M' or text[0] == 'R':
				asdfsdf =5
			else:
				residue_gg_tt[ff] += 0
		
		
		sequence_p = []
		for a in range(len(ex3)):
			chunk_3 = ex3[a:a+25]
			if len(chunk_3) < 25:
				break
			sequence_p.append(chunk_3)
		
		
		
		for jj in range(len(ex2)):
			f.write("1 ")
			print('\n-------1-------')

			for i in range(len(sequence_p[jj])):
				chunk_1 = sequence_p[jj][i:i + 1]
				if isTest_1(chunk_1):
					print(abc_1)
				f.write("%d:%f " % (i+1, abc_1))


			print('\n-------2------')

			for a in range(len(sequence_p[jj])):  
				chunk_2 = sequence_p[jj][a:a + 1]
				if isTest_2(chunk_2):
					print(abc_2)
				f.write("%d:%f " % (a+26, abc_2))

			print('\n-------3------')
		
			for a in range(len(sequence_p[jj]) - 2):
				chunk_3 = sequence_p[jj][a:a + 3]
				isTest_3(chunk_3)
				# print(abc_3)
			
			for aa in range(64):
				print(residue_HHH[aa])
				f.write("%d:%f " % (aa + 51, residue_HHH[aa]))


			print('\n-------4------')
		
			for ff in range(len(sequence_p[jj]) - 1):
				chunk_4 = sequence_p[jj][ff:ff + 2]
				isTest_4(chunk_4)
			
			for uu in range(24):
				print(residue_gg_tt[uu])
				f.write("%d:%f " % (uu + 115, residue_gg_tt[uu]))

			f.write("\n")
			cg_ct = [1, 1]
			residue_gg_tt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
			
			residue_HHH.clear()
			for hh in range(64):
				residue_HHH.append(0)


	
		#f.write('-1 2:1 6:1 17:1 24:1 38:1 42:1 50:1 64:1 71:1 73:1 74:1 76:1 82:1 83:1\n')
		#f.write('hhhh')
		f.close()
		

	
		
		svmc_exe = "svm-scale.exe -l 0 -u 1 -r train_model_mm10.range test_sequence_mm10.txt "+"> test_sequence_mm10.t.scale"
		popen(svmc_exe)
		time.sleep(5)


		svmp_exe_1 = "svm-predict_cutoffmod.exe " 
		svmp_exe_2 = "test_sequence_mm10.t.scale "
		#svmp_exe_2 = "test_sequence_mm10.txt "
		svmp_exe_3 = "train_model_mm10.model " 
		svmp_exe_4 = "sequence_mm10.result"
		svmp_exe = svmp_exe_1+svmp_exe_2+svmp_exe_3+svmp_exe_4
		p1 = popen(svmp_exe)		
		#p1 = subprocess.check_output(["ipconfig","/all"], universal_newlines=True)






		form = NameForm_2(request.POST)
		#form = form + p1
		if form.is_valid():
			cd = form.cleaned_data
			#cd['test_variable']
			ex1 = cd['Sequence_2']
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
				i = os.path.getsize('sequence_mm10.result')
				time.sleep(3)
				j = os.path.getsize('sequence_mm10.result')
				if i==j and i != 0 and j != 0:
					break							
			

			file_read = open('sequence_mm10.result','r').read()



			return HttpResponse(file_read)



	else:
		f = NameForm_2()
		return render(request, "home_site/mouse_long.html", {'form': f})
#	try:
#		f = NameForm()
#		return render(request, "home_site/index.html", {'form': f})
#
#	except:
#		return HttpResponseNotFound(u'<h1>not access</h1>')









def doc_home(request):
    return render(request, 'home_site/doc.html')
    
    
def contact_home(request):
    return render(request, 'home_site/contact.html')


#def file_home(request):
#   return render(request, 'home_site/Supplementary Table 1.xlsx')

def file_home(request, scripts_id):
    scripts = get_object_or_404(Scripts, id=scripts_id)
    title = scripts.title.encode('euc-kr')
    response = HttpResponse(content_type='plain/text')
    response['Content-Disposition'] = 'attachment; filename=' + title
    response.write(scripts.contents.encode('euc-kr'))
    return response
