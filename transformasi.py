""" NIM/Nama  : 13517019/Lydia Astrella Wiguna, 13517137/Vincent Budianto, 13517142/Saskia Imani
    Nama file : transformasi.py
    Topik     : Tugas Besar II IF2123 - Aljabar Geometri / Simulasi Transformasi Linier pada Bidang 2D dan 3D dengan Menggunakan OpenGL API
    Tanggal   : 19 November 2018
    Deskripsi : Fungsi dan prosedur transformasi matriks 2D dan 3D """

import numpy as np
import math

#Kamus Global
global vertices
global default

def translate2D(vin,dx,dy):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: dx adalah perubahan koordinat X
#		: dy adalah perubahan koordinat Y
#Output : mengembalikan matriks baru yang berisi vin yang sudah ditranslasi
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	for i in range(len(vertices)):
		vertices[i][0] = vertices[i][0] + dx
		vertices[i][1] = vertices[i][1] + dy
	return vertices

def translate3D(vin,dx,dy,dz):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: dx adalah perubahan koordinat X
#		: dy adalah perubahan koordinat Y
#		: dz adalah perubahan koordinat Z
#Output : mengembalikan matriks baru yang berisi vin yang sudah ditranslasi
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	for i in range(len(vertices)):
		vertices[i][0] = vertices[i][0] + dx
		vertices[i][1] = vertices[i][1] + dy
		vertices[i][2] = vertices[i][2] + dz
	return vertices

def dilate2D(vin,k):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: k adalah faktor skala dilatasi
#Output : mengembalikan matriks baru yang berisi vin yang sudah didilatasi
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	for i in range(len(vertices)):
		vertices[i] = vertices[i] * k
	return vertices

def dilate3D(vin,k):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: k adalah faktor skala dilatasi
#Output : mengembalikan matriks baru yang berisi vin yang sudah didilatasi
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	for i in range(len(vertices)):
		vertices[i] = vertices[i] * k
	return vertices

def rotate2D(vin,deg,a,b):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: deg adalah sudut perputaran (derajat)
#		: a adalah titik pusat x
#		: b adalah titik pusat y
#Output : mengembalikan matriks baru yang berisi vin yang sudah dirotasi pada titik (a,b) dan deg derajat
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	for i in range(len(vin)):
		vertices[i][0] = (vin[i][0] - a) * math.cos(math.radians(deg)) - (vin[i][1] - b) * math.sin(math.radians(deg)) + a
		vertices[i][1] = (vin[i][0] - a) * math.sin(math.radians(deg)) + (vin[i][1] - b) * math.cos(math.radians(deg)) + b
	return vertices

def rotate3D(vin,deg,param):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: deg adalah sudut perputaran (derajat)
#		: param adalah sumbu parameter perputaran (x, y, atau z)
#Output : mengembalikan matriks baru yang berisi vin yang sudah dirotasi dengan paramater x, y, z dan deg derajat
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	if param=='x':
		for i in range(len(vin)):
			vertices[i][1] = vin[i][1] * math.cos(math.radians(deg)) - vin[i][2] * math.sin(math.radians(deg))
			vertices[i][2] = vin[i][1] * math.sin(math.radians(deg)) + vin[i][2] * math.cos(math.radians(deg))
	elif param=='y':
		for i in range(len(vin)):
			vertices[i][0] = vin[i][0] * math.cos(math.radians(deg)) + vin[i][2] * math.sin(math.radians(deg))
			vertices[i][2] = vin[i][2] * math.cos(math.radians(deg)) - vin[i][0] * math.sin(math.radians(deg))
	elif param=='z':
		for i in range(len(vin)):
			vertices[i][0] = vin[i][0] * math.cos(math.radians(deg)) - vin[i][1] * math.sin(math.radians(deg))
			vertices[i][1] = vin[i][0] * math.sin(math.radians(deg)) + vin[i][1] * math.cos(math.radians(deg))
	return vertices

def reflect2D(vin,param):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: param adalah sumbu parameter refleksi (x, y, y = x, y = -x, atau titik (a,b))
#Output : mengembalikan matriks baru yang merupakan vin yang sudah direkfleksi dengan paramater x, y, y = x, y = -x, atau titik (a,b)
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	par = param.split('(')
	par = param.split(')')
	par = param.split(',')
	if len(par)==2:
		a = float(par[0][1:])
		b = float(par[1][:len(par[1]) - 1])
		for i in range(len(vin)):
			vertices[i][0] = (2 * a) - vin[i][0]
			vertices[i][1] = (2 * b) - vin[i][1]
	else:
		if param=='x':
			for i in range(len(vin)):
				vertices[i][1] = -vin[i][1]
		elif param=='y':
			for i in range(len(vin)):
				vertices[i][0] = -vin[i][0]
		elif param=='y=x':
			for i in range(len(vin)):
				vertices[i][0] = vin[i][1]
				vertices[i][1] = vin[i][0]
		elif param=='y=-x':
			for i in range(len(vin)):
				vertices[i][0] = -vin[i][1]
				vertices[i][1] = -vin[i][0]
	return vertices

def reflect3D(vin,param):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: param adalah sumbu parameter refleksi (x, y, z, xy, xz, yz, atau titik(a,b,c))
#Output : mengembalikan matriks baru yang merupakan vin yang sudah direkfleksi dengan paramater x, y, z, xy, xz, atau yz
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	par = param.split('(')
	par = param.split(')')
	par = param.split(',')
	if len(par)==3:
		a = float(par[0][1:])
		b = float(par[1][:len(par[1])])
		c = float(par[2][:len(par[2]) - 1])
		for i in range(len(vin)):
			vertices[i][0] = (2 * a) - vin[i][0]
			vertices[i][1] = (2 * b) - vin[i][1]
			vertices[i][2] = (2 * c) - vin[i][2]
	else:
		if param=='x':
			for i in range(len(vin)):
				vertices[i][1] = -vin[i][1]
				vertices[i][2] = -vin[i][2]
		elif param=='y':
			for i in range(len(vin)):
				vertices[i][0] = -vin[i][0]
				vertices[i][2] = -vin[i][2]
		elif param=='z':
			for i in range(len(vin)):
				vertices[i][0] = -vin[i][0]
				vertices[i][1] = -vin[i][1]
		elif param=='xy':
			for i in range(len(vin)):
				vertices[i][2] = -vin[i][2]
		elif param=='xz':
			for i in range(len(vin)):
				vertices[i][1] = -vin[i][1]
		elif param=='yz':
			for i in range(len(vin)):
				vertices[i][0] = -vin[i][0]
	return vertices
	
def shear2D(vin,param,k):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: param adalah sumbu parameter shear (x atau y)
#		: k adalah faktor gusuran
#Output : mengembalikan matriks baru yang telah digusur terhadap sumbu <param> dengan faktor gusuran <k>
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	if param=='x':
		for i in range(len(vin)):
			vertices[i][0] = vin[i][0] + (k * vin[i][1])
	elif param=='y':
		for i in range(len(vin)):
			vertices[i][1] = vin[i][1] + (k * vin[i][0])
	return vertices

def shear3D(vin,param,k):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: param adalah sumbu parameter shear (xy, xz, atau yz)
#		: k adalah faktor gusuran
#Output : mengembalikan matriks baru yang telah digusur terhadap sumbu <param> dengan faktor gusuran <k>
	vertices = np.array(vin)
	if param=='xy':
		for i in range(len(vin)):
			vertices[i][0] = vin[i][0] + (k * vin[i][2])
			vertices[i][1] = vin[i][1] + (k * vin[i][2])
	elif param=='xz':
		for i in range(len(vin)):
			vertices[i][0] = vin[i][0] + (k * vin[i][1])
			vertices[i][2] = vin[i][2] + (k * vin[i][1])
	elif param=='yz':
		for i in range(len(vin)):
			vertices[i][1] = vin[i][1] + (k * vin[i][0])
			vertices[i][2] = vin[i][2] + (k * vin[i][0])
	return vertices

def stretch2D(vin,param,k):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: param adalah sumbu parameter stretch (x atau y)
#		: k adalah faktor regangan
#Output : mengembalikan matriks baru yang telah diregangkan terhadap sumbu <param> dengan faktor regangan <k>
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	if param=='x':
		for i in range(len(vin)):
			vertices[i][0] = vin[i][0] * k
	elif param=='y':
		for i in range(len(vin)):
			vertices[i][1] = vin[i][1] * k
	return vertices

def stretch3D(vin,param,k):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: param adalah sumbu parameter stretch (x, y, atau z)
#		: k adalah faktor regangan
#Output : mengembalikan matriks baru yang telah diregangkan terhadap sumbu <param> dengan faktor regangan <k>
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	if param=='x':
		for i in range(len(vin)):
			vertices[i][0] = vin[i][0] * k
	elif param=='y':
		for i in range(len(vin)):
			vertices[i][1] = vin[i][1] * k
	elif param=='z':
		for i in range(len(vin)):
			vertices[i][2] = vin[i][2] * k
	return vertices

def custom2D(vin,a,b,c,d):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: a, b, c, dan d adalah matriks transformasi custom
#Output : mengembalikan matriks baru yang telah dikalikan dengan matriks transformasi [[a,b],[c,d]]
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	mcust = np.array([[a,b],[c,d]])
	return vertices.dot(mcust)

def custom3D(vin,a,b,c,d,e,f,g,h,i):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: a, b, c, d, e, f, g, h, dan i adalah matriks transformasi custom
#Output : mengembalikan matriks baru yang telah dikalikan dengan matriks transformasi [[a,b,c],[d,e,f],[g,h,i]]
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	mcust = np.array([[a,b,c],[d,e,f],[g,h,i]])
	return vertices.dot(mcust)

def multiple2D(vin,n):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: n adalah jumlah transformasi matriks yang akan dilakukan
#Output : melakukan transformasi linier sebanyak n kali berurutan. Setiap baris input 1..n dapat berupa translate, rotate, shear, dll tetapi bukan multiple, reset, exit
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	for i in range(n):
		correct = False
		while(not(correct)):
			print(" List Fungsi : ")
			print(" 1. translate dx dy")
			print(" 2. dilate k")
			print(" 3. rotate deg x y")
			print(" 4. reflect par")
			print(" 5. shear par k")
			print(" 6. stretch par k")
			print(" 7. custom a b c d")
			function = input(' Masukan fungsi %d : '% (i+1))
			func = function.split(' ')
			if (func[0] == "translate" and len(func)==3):
				vertices = translate2D(vertices,float(func[1]),float(func[2]))
				correct = True
			elif (func[0] == "dilate" and len(func)==2):
				vertices = dilate2D(vertices,float(func[1]))
				correct = True
			elif (func[0] == 'rotate' and len(func)==4):
				vertices = rotate2D(vertices,float(func[1]),float(func[2]),float(func[3]))
				correct = True
			elif (func[0] == 'reflect' and len(func)==2):
				vertices = reflect2D(vertices,func[1])
				correct = True
			elif (func[0] == 'shear' and len(func)==3):
				vertices = shear2D(vertices,func[1],float(func[2]))
				correct = True
			elif (func[0] == 'stretch' and len(func)==3):
				vertices = stretch2D(vertices,func[1],float(func[2]))
				correct = True
			elif (func[0] == 'custom' and len(func)==5):
				vertices = custom2D(vertices,float(func[1]),float(func[2]),float(func[3]),float(func[4]))
				correct = True
			else :
				print(" Input fungsi salah. Silakan masukkan ulang funsi.")
	return vertices

def multiple3D(vin,n):
#Input  : vin adalah list yang menampung titik (Matriks)
#		: n adalah jumlah transformasi matriks yang akan dilakukan
#Output : melakukan transformasi linier sebanyak n kali berurutan. Setiap baris input 1..n dapat berupa translate, rotate, shear, dll tetapi bukan multiple, reset, exit
	#Kamus
	
	#Algoritma
	vertices = np.array(vin)
	for i in range(n):
		correct = False
		while(not(correct)):
			print(" List Fungsi : ")
			print(" 1. translate dx dy dz")
			print(" 2. dilate k")
			print(" 3. rotate deg par")
			print(" 4. reflect par")
			print(" 5. shear par k")
			print(" 6. stretch par k")
			print(" 7. custom a b c d e f g h i")
			function = input(' Masukan fungsi %d: '% (i+1))
			func = function.split(' ')
			if (func[0] == "translate" and len(func)==4):
				vertices = translate3D(vertices,float(func[1]),float(func[2]),float(func[3]))
				correct = True
			elif (func[0] == "dilate" and len(func)==2):
				vertices = dilate3D(vertices,float(func[1]))
				correct = True
			elif (func[0] == 'rotate' and len(func)==3):
				vertices = rotate3D(vertices,float(func[1]),func[2])
				correct = True
			elif (func[0] == 'reflect' and len(func)==2):
				vertices = reflect3D(vertices,func[1])
				correct = True
			elif (func[0] == 'shear' and len(func)==3):
				vertices = shear3D(vertices,func[1],float(func[2]))
				correct = True
			elif (func[0] == 'stretch' and len(func)==3):
				vertices = stretch3D(vertices,func[1],float(func[2]))
				correct = True
			elif (func[0] == 'custom' and len(func)==10):
				vertices = custom3D(vertices,float(func[1]),float(func[2]),float(func[3]),float(func[4]),float(func[5]),float(func[6]),float(func[7]),float(func[8]),float(func[9]))
				correct = True
			else:
				print(" Input fungsi salah. Silakan masukkan ulang fungsi.")
	return vertices
