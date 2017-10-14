#!/usr/bin/env python
#coding: utf-8

import PIL, sys, binascii
from PIL import Image

def encode(pic, message):
	lsb(pic, message)


def lsb(pic, msg):
	im        = Image.open(pic) 	# �ppna bilden
	load      = im.load() 		# Ladda bilden
	fmsg	= fixmsg(msg)
	pix       = im.getdata() 		# H�mta bildens pixlar
	lsb       = msg2bin(fmsg) 		# Konvertera meddelandet till bin�r form

	counter,red,green,blue = 0,0,0,0

	for i in range(0,get_pixels(fmsg)):
		#bin = pix[i][0],pix[i][1],pix[i][2]

		r = list(hexToBin(rgb2hex(pix[i][0])))
		g = list(hexToBin(rgb2hex(pix[i][1])))
		b = list(hexToBin(rgb2hex(pix[i][2])))
		#print "(%s,%s,%s)" % (r,g,b)

		lr = len(r)-1
		lg = len(g)-1
		lb = len(b)-1

		xr = r[lr]
		xg = g[lg]
		xb = b[lb]


		if xr != lsb[counter]:
			r[lr] = lsb[counter]
			red = int(''.join(r),2)
			load[i,0] = (red, pix[i][1], pix[i][2])
			#print r
			print("[PASS]Counter is %d" % (counter))
			counter += 1
		else:
			#print r
			print("Counter is %d" % (counter))
			counter += 1

		if xg != lsb[counter]:
			g[lg] = lsb[counter]
			green = int(''.join(g),2)
			load[i,0] = (pix[i][0], green, pix[i][2])
			#print g
			print("[PASS]Counter is %d" % (counter))
			counter += 1
		else:
			#print g
			print("Counter is %d" % (counter))
			counter += 1

		if xb != lsb[counter]:
			b[lb] = lsb[counter]
			blue = int(''.join(b),2)
			load[i,0] = (pix[i][0], pix[i][1], blue)
			#print b
			print("[PASS]Counter is %d" % (counter))
			counter += 1
		else:
			#print b
			print("Counter is %d" % (counter))
			counter += 1

		if counter == len(fmsg)*8:
			break

	im.save("out.png")

def decode(pic):
	im     = Image.open(pic)
	pix    = im.getdata()
	binary = ""
	length = ""
	for i in range(0,3):

		r = list(hexToBin(rgb2hex(pix[i][0])))
		g = list(hexToBin(rgb2hex(pix[i][1])))
		b = list(hexToBin(rgb2hex(pix[i][2])))

		lr = len(r)-1
		lg = len(g)-1
		lb = len(b)-1

		xr = r[lr]
		xg = g[lg]
		xb = b[lb]

		length += xr
		length += xg
		length += xb

#messagelength = int(length[:8],2)
	#tes = (messagelength*8)/3

	for n in range(0,88):

		r = list(hexToBin(rgb2hex(pix[n][0])))
		g = list(hexToBin(rgb2hex(pix[n][1])))
		b = list(hexToBin(rgb2hex(pix[n][2])))
		#print "(%s,%s,%s)" % (r,g,b)
		lr = len(r)-1
		lg = len(g)-1
		lb = len(b)-1

		xr = r[lr]
		xg = g[lg]
		xb = b[lb]

		binary += xr
		binary += xg
		binary += xb

	text = int(binary, 2)
	print("Binary is: %s" % binary)
	return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))


def msg2bin(fmsg):
	text = ""
	for x in fmsg:
		text += bin(ord(x))[2:].rjust(8, '0')
	return text

def ToInt(x):
	x = "".join(x)
	return x

# Konvertera fr�n Hexadecimal till bin�r
def hexToBin(var):
	binary = bin(int(var, 16))[2:]
	return binary

def rgb2hex(x):
	return hex(x)

# RGB to Hex
def rgbToHex(x,y,z):
	rgb   = (x, y, z)
	r,g,b = rgb
	var = hex(r)[2:] + hex(g)[2:] + hex(b)[2:]
	return var

def get_pixels(fmsg):
	pix = int((len(fmsg) * 8)/3)
	print('Pixels needed:' + str(pix))
	return pix

def fixmsg(msg):
	le = len(msg)
	while (le % 3 != 0):
		msg += ' '
		le = len(msg)
		print('Fixing message: ' + str(msg))
		print('Message Length:' + str(le))
	return (msg)



'''
if sys.argv[1] == '-e':
	message = sys.argv[2] # Ditt meddelande
	pic = Image.open(sys.argv[3]) # Bilden du vill anv�nda
	encode(pic, message)
	#pic.save(sys.argv[4]) # Var din nya bild ska heta

elif sys.argv[1] == '-d':
	pic = Image.open(sys.argv[2])
	message = decode(pic)
	print message
'''


lsb("in.png", "CCTF{St3gaNgr4phy_tH3_N4iv3_w4y}")


print(decode("out.png"))

'''
{[011][000][010]}|{[110][001][001]}|{[100][011][000]}
[01100001][01100010][01100011][01100111]1000

l�s in 8 bitar �t g�ngen


'''
