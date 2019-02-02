""" NIM/Nama  : 13517019/Lydia Astrella Wiguna, 13517137/Vincent Budianto, 13517142/Saskia Imani
    Nama file : Transformer.py
    Topik     : Tugas Besar II IF2123 - Aljabar Geometri / Simulasi Transformasi Linier pada Bidang 2D dan 3D dengan Menggunakan OpenGL API
    Tanggal   : 19 November 2018
    Deskripsi : Program utama untuk transformasi 2D dan 3D """

from OpenGL.GL import*
from OpenGL.GLU import*
import pygame
from pygame.locals import*
from transformasi import*
import numpy as np
import msvcrt
import os
import random
import sys
import time

#Inisialisasi pygame
pygame.init()
pygame.event.set_blocked(pygame.MOUSEMOTION)
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
#Posisi Windows saat muncul
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,25)
#Waktu untuk animasi saat program berjalan
clock = pygame.time.Clock()

#Inisialisasi variabel mula-mula
vertices = []
default = []
flag = 0
x = 0

#Inisialisasi variabel mula-mula untuk kubus 3D
points = (
	(50., -50., -50.),
	(50., 50., -50.),
	(-50., 50., -50.),
	(-50., -50., -50.),
	(50., -50., 50.),
	(50., 50., 50.),
	(-50., -50., 50.),
	(-50., 50., 50.)
	)
edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7)
	)
surfaces = (
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6)
	)

#Inisialisasi variabel warna
colors = (
	(1,0.5,0.5),
	(0.5,1,0.5),
	(0.5,0.5,1),
	(0.5,1,0.5),
	(1,1,1),
	(0.5,1,1),
	(1,0.5,0.5),
	(0.5,1,0.5),
	(0.5,0.5,1),
	(1,0.5,0.5),
	(1,1,1),
	(0.5,1,1),
	)

#Algoritma Fungsi dan Prosedur
def shape2D(vertices):
#Prosedur untuk menampilkan garis sumbu x, garis sumbu y, dan bentuk 2D
	#Kamus
	global x
	
	#Algoritma
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glBegin(GL_LINES)
	glColor3fv((0,1,0))
	glVertex3fv((0,-50000,0))
	glVertex3fv((0,50000,0))
	glColor3fv((0,0,1))
	glVertex3fv((50000,0,0))
	glVertex3fv((-50000,0,0))
	glEnd()

	glBegin(GL_POLYGON)
	n = x
	for i in range(len(vertices)):
		glColor3fv(colors[n])
		glVertex2fv(vertices[i])
		n = (n + 1) % 12
	glEnd()
	pygame.display.flip()

def movement2D(default,vertices):
	#Kamus
	
	#Algoritma
	vin = np.array(default)
	vout = np.array(vertices)
	while (not(np.array_equal(vin,vout))):
		for i in range(len(vin)):
			for j in range(2):
				if (vout[i][j] - vin[i][j] > 1) or (vout[i][j] - vin[i][j] < -1):
					vin[i][j] += (vout[i][j] - vin[i][j]) / 70
				else:
					vin[i][j] += (vout[i][j] - vin[i][j])
		shape2D(vin)
		pygame.time.wait(1)


def input2D():
#prosedur untuk membaca titik 2D
	#Kamus
	global vertices
	global default
	   
	#Algoritma
	N = int(input(' Masukkan jumlah titik sudut : '))
	for i in range (N):
		vertices.append([0.0,0.0])
		inp = input(' (x%d,y%d) : '% (i+1,i+1))
		point = inp.split(',')
		vertices[i][0]=(float(point[0]))
		vertices[i][1]=(float(point[1]))
	default = np.array(vertices)
	vertices = np.array(vertices)

def display2D():
#Prosedur untuk menampilkan window pygame 2D dan gabungan prosedur bentuk 2D
	#Kamus
	global vertices
	global default
	global flag
	global function
	
	#Algoritma
	size=(500,500)
	pygame.display.set_mode(size, DOUBLEBUF|OPENGL)
	pygame.display.set_caption('Graph 2D')

	gluPerspective(45, (size[0]/size[1]), 0, 1250)

	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	glTranslatef(0.0,0.0,-1250)
	
	while (flag == 0):
		shape2D(vertices)
		vertices = dimensi2()

	movement2D(default,vertices)

	while (function != "exit"):
		temp = np.array(vertices)
		vertices = dimensi2()
		shape2D(vertices)
		movement2D(temp,vertices)

def dimensi2():
#Prosedur menu untuk bentuk 2D
	#Kamus
	global vertices
	global default
	global flag
	global function
	global func
	
	#Algoritma
	cek = 0
	while (cek == 0):
		print(" List Fungsi : ")
		print("  1. translate dx dy")
		print("  2. dilate k")
		print("  3. rotate deg x y")
		print("  4. reflect par")
		print("  5. shear par k")
		print("  6. stretch par k")
		print("  7. custom a b c d")
		print("  8. multiple n")
		print("  9. reset")
		print(" 10. camera")
		print(" 11. exit")
		function = input(" Masukan fungsi : ")
		func = function.split(' ')
		if (func[0]=="translate" and len(func)==3):
			vertices = translate2D(vertices,float(func[1]),float(func[2]))
		elif (func[0]=="dilate" and len(func)==2):
			vertices = dilate2D(vertices,float(func[1]))
		elif (func[0]=='rotate' and len(func)==4):
			vertices = rotate2D(vertices,float(func[1]),float(func[2]),float(func[3]))
		elif (func[0]=='reflect' and len(func)==2):
			vertices = reflect2D(vertices,func[1])
		elif (func[0]=='shear' and len(func)==3):
			vertices = shear2D(vertices,func[1],float(func[2]))
		elif (func[0]=='stretch' and len(func)==3):
			vertices = stretch2D(vertices,func[1],float(func[2]))
		elif (func[0]=='custom' and len(func)==5):
			vertices = custom2D(vertices,float(func[1]),float(func[2]),float(func[3]),float(func[4]))
		elif (func[0]=='multiple' and len(func)==2):
			vertices = multiple2D(vertices,int(func[1]))
		elif (func[0]=='reset' and len(func)==1):
			vertices = default
		elif (func[0]=='camera' and len(func)==1):
			os.system('cls')
			cam2()
		elif (func[0]=='exit' and len(func)==1):
			cek = 1
			os.system('cls')
			credit()
			exit()
		else :
			print(" Input fungsi salah. Silakan masukkan ulang fungsi.")
		flag = 1
		return vertices

def cam2():
#Prosedur untuk menggerakan kamera 2D
	#Kamus
	
	#Algoritma
	print(' HINT')
	print(' w,s : atas, bawah')
	print(' a,d : kiri, kanan')
	print(' i,o : zoom in, zoom out')
	print(' j,k : rotate cc, rotate c')
	print(' q   : kembali\n')
	cek = 0
	while (cek == 0):
		choice = msvcrt.getwch()
		if choice=='a':
			glTranslatef(10,0.0,0.0)
			shape2D(vertices)
		elif choice=='d':
			glTranslatef(-10,0.0,0)
			shape2D(vertices)
		elif choice=='s':
			glTranslatef(0.0,10,0)
			shape2D(vertices)
		elif choice=='w':
			glTranslatef(0.0,-10,0)
			shape2D(vertices)
		elif choice=='i':
			glTranslatef(0.0,0,10)
			shape2D(vertices)
		elif choice=='o':
			glTranslatef(0.0,0,-10)
			shape2D(vertices)
		elif choice=='j':
			glRotatef(1,0.0,0,1)
			shape2D(vertices)
		elif choice=='k':
			glRotatef(-1,0.0,0,1)
			shape2D(vertices)
		elif choice=='q':
			cek = 1
			os.system('cls')
			dimensi2()
		clock.tick(60)

def shape3D(points):
#Prosedur untuk menampilkan garis sumbu x, garis sumbu y, garis sumbu z, dan bentuk 3D
	#Kamus
	global x
	
	#Algoritma
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	glBegin(GL_LINES)
	glColor3fv((0,0,1))
	glVertex3fv((0,-50000,0))
	glVertex3fv((0,50000,0))
	glColor3fv((0,1,0))
	glVertex3fv((50000,0,0))
	glVertex3fv((-50000,0,0))
	glColor3fv((1,0,0))
	glVertex3fv((0,0,50000))
	glVertex3fv((0,0,-50000))
	glEnd()

	n = x
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv(colors[n])
			glVertex3fv(points[vertex])
			n = (n + 1) % 12
	glEnd()

	glBegin(GL_LINES)
	glColor3fv((1,1,1))
	for edge in edges:
		for vertex in edge:
			glVertex3fv(points[vertex])
	glEnd()

	pygame.display.flip()

def movement3D(default,vertices):
	#Kamus
	
	#Algoritma
	vin = np.array(default)
	vout = np.array(vertices)
	while (not(np.array_equal(vin,vout))):
		for i in range(len(vin)):
			for j in range(3):
				if (vout[i][j] - vin[i][j] > 1) or (vout[i][j] - vin[i][j] < -1):
					vin[i][j] += (vout[i][j] - vin[i][j]) / 70
				else:
					vin[i][j] += (vout[i][j] - vin[i][j])
		shape3D(vin)
		pygame.time.wait(1)

def display3D():
#Prosedur untuk menampilkan window pygame 3D dan gabungan prosedur bentuk 3D
	#Kamus
	global vertices
	global default
	global flag

	#Algoritma
	vertices = points
	default = points

	size=(500,500)
	pygame.display.set_mode(size, DOUBLEBUF|OPENGL)
	pygame.display.set_caption('Graph 3D')
	
	gluPerspective(45, (size[0]/size[1]), 0.1, 3000)

	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	glTranslatef(0.0,0.0,-1200)
	glRotatef(70,-1,0,0)
	glRotatef(-135,0,0,1)
	
	while (flag == 0):
		shape3D(vertices)
		vertices = dimensi3()

	movement3D(default,vertices)

	while (function != "exit"):
		temp = np.array(vertices)
		vertices = dimensi3()
		shape3D(vertices)
		movement3D(temp,vertices)

def dimensi3():
#Prosedur menu untuk bentuk 3D
	#Kamus
	global vertices
	global default
	global flag
	global function
	global func
	
	#Algoritma
	cek = 0
	while (cek == 0):
		print(" List Fungsi : ")
		print("  1. translate dx dy dz")
		print("  2. dilate k")
		print("  3. rotate deg par")
		print("  4. reflect par")
		print("  5. shear par k")
		print("  6. stretch par k")
		print("  7. custom a b c d e f g h i")
		print("  8. multiple n")
		print("  9. reset")
		print(" 10. camera")
		print(" 11. exit")
		function = input(" Masukan fungsi : ")
		func = function.split(' ')
		if (func[0]=="translate" and len(func)==4):
			vertices = translate3D(vertices,float(func[1]),float(func[2]),float(func[3]))
		elif (func[0]=="dilate" and len(func)==2):
			vertices = dilate3D(vertices,float(func[1]))
		elif (func[0]=='rotate' and len(func)==3):
			vertices = rotate3D(vertices,float(func[1]),func[2])
		elif (func[0]=='reflect' and len(func)==2):
			vertices = reflect3D(vertices,func[1])
		elif (func[0]=='shear' and len(func)==3):
			vertices = shear3D(vertices,func[1],float(func[2]))
		elif (func[0]=='stretch' and len(func)==3):
			vertices = stretch3D(vertices,func[1],float(func[2]))
		elif (func[0]=='custom' and len(func)==10):
			vertices = custom3D(vertices,float(func[1]),float(func[2]),float(func[3]),float(func[4]),float(func[5]),float(func[6]),float(func[7]),float(func[8]),float(func[9]))
		elif (func[0]=='multiple' and len(func)==2):
			vertices = multiple3D(vertices,int(func[1]))
		elif (func[0]=='reset' and len(func)==1):
			vertices = default
		elif (func[0]=='camera' and len(func)==1):
			os.system('cls')
			cam3()
		elif (func[0]=='exit' and len(func)==1):
			cek = 1
			os.system('cls')
			credit()
			exit()
		else:
			print("Input fungsi salah. Silakan masukkan ulang fungsi.")
		flag = 1
		return vertices

def cam3():
#Prosedur untuk menggerakan kamera 3D
	#Kamus
	
	#Algoritma
	print(' HINT')
	print(' z,e : x positif, x negatif')
	print(' a,d : y negatif, y positif')
	print(' w,x : z positif, z negatif')
	print(' u,i : rotasi sumbu x')
	print(' j,k : rotasi sumbu y')
	print(' n,m : rotasi sumbu z')
	print(' q   : kembali\n')
	cek = 0
	while (cek == 0):
		choice = msvcrt.getwch()
		if choice=='e':
			glTranslatef(10,0.0,0.0)
			shape3D(vertices)
		elif choice=='z':
			glTranslatef(-10,0.0,0)
			shape3D(vertices)
		elif choice=='a':
			glTranslatef(0.0,10,0)
			shape3D(vertices)
		elif choice=='d':
			glTranslatef(0.0,-10,0)
			shape3D(vertices)
		elif choice=='x':
			glTranslatef(0.0,0,10)
			shape3D(vertices)
		elif choice=='w':
			glTranslatef(0.0,0,-10)
			shape3D(vertices)
		elif choice=='u':
			glRotatef(1,1,0.0,0.0)
			shape3D(vertices)
		elif choice=='i':
			glRotatef(-1,1,0.0,0.0)
			shape3D(vertices)
		elif choice=='j':
			glRotatef(1,0.0,1,0.0)
			shape3D(vertices)
		elif choice=='k':
			glRotatef(-1,0.0,1,0.0)
			shape3D(vertices)
		elif choice=='n':
			glRotatef(1,0.0,0.0,1.0)
			shape3D(vertices)
		elif choice=='m':
			glRotatef(-1,0.0,0.0,1.0)
			shape3D(vertices)
		elif choice=='q':
			cek = 1
			os.system('cls')
			dimensi3()
		clock.tick(60)
		
def mainmenu():
#prosedur menu utama
	#Kamus
	
	#Algoritma
	choice = 0
	os.system('cls')
	while (choice != 1) or (choice != 3) or (choice != 2):
		print(' ____________________________________________________________________________________________________ ')
		print('|  _______  _____             _   _   _____  _____   ____   _____   __  __             _____  _____  |')
		print('| |__   __||  __ \     /\    | \ | | / ____||  ___| / __ \ |  __ \ |  \/  |    /\     / ____||_   _| |')
		print('|    | |   | |__) |   /  \   |  \| || (___  | |__  | |  | || |__) || \  / |   /  \   | (___    | |   |')
		print('|    | |   |  _  /   / /\ \  | . ` | \___ \ |  __| | |  | ||  _  / | |\/| |  / /\ \   \___ \   | |   |')
		print('|    | |   | | \ \  / ____ \ | |\  | ____) || |    | |__| || | \ \ | |  | | / ____ \  ____) | _| |_  |')
		print('|    |_|   |_|  \_\/_/    \_\|_| \_||_____/ |_|     \____/ |_|  \_\|_|  |_|/_/    \_\|_____/ |_____| |')
		print('|                                                                                                    |')
		print('|           __  __         _______  _____   _____  _  __  _____                                      |')
		print('|          |  \/  |    /\ |__   __||  __ \ |_   _|| |/ / / ____|                Main Menu :          |')
		print('|          | \  / |   /  \   | |   | |__) |  | |  | ` / | (___                  1. 2 Dimensi         |')
		print('|          | |\/| |  / /\ \  | |   |  _  /   | |  |  <   \___ \                 2. 3 Dimensi         |')
		print('|          | |  | | / ____ \ | |   | | \ \  _| |_ | . \  ____) |                3. exit              |')
		print('|          |_|  |_|/_/    \_\|_|   |_|  \_\|_____||_|\_\|_____/                                      |')
		print('|____________________________________________________________________________________________________|')
		choice = msvcrt.getwch()
		if choice == '1':
			os.system('cls')
			input2D()
			display2D()
		elif choice == '2':
			os.system('cls')
			display3D()
		elif choice == '3':
			os.system('cls')
			credit()
			exit()
		else:
			mainmenu()

def credit():
#Prosedur untuk tampilan credit
	#Kamus
	
	#Algoritma
	print(' ____________________________________________________________________________________________________ ')
	print('|                                                                                                    |')
	print('|                                            TERIMA KASIH                                            |')
	print('|                                                                                                    |')
	print('|                                  13517019 - Lydia Astrella Wiguna                                  |')
	print('|                                     13517137 - Vincent Budianto                                    |')
	print('|                                       13517142 - Saskia Imani                                      |')
	print('|____________________________________________________________________________________________________|')
	time.sleep(1)

#Algoritma
x = random.randint(0,11)
mainmenu()
