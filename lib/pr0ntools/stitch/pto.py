'''
pr0ntools
Copyright 2011 John McMaster <JohnDMcMaster@gmail.com>
Licensed under the terms of the LGPL V3 or later, see COPYING for details

.pto format?
http://photocreations.ca/panotools/stitch.txt
'''

'''
# Hugin project file
# generated by Autopano

# Panorama settings:
p w8000 h1200 f2 v250 n"PSD_mask"

# input images:
#-imgfile 2816 2112 "Z:\home\mcmaster\buffer\IC\motorola_mcu_vince\top_metal\5X\0.1\x00000_y00000.jpg"
o f0 y+0.000000 r+0.000000 p+0.000000 u20 d0.000000 e0.000000 v70.000000 a0.000000 b0.000000 c0.000000
'''

import shutil
from pr0ntools.temp_file import ManagedTempFile
from pr0ntools.execute import Execute
import os

class Image:
	'''
	#-hugin  cropFactor=6.05334
	i w2816 h2112 f0 Eb1 Eev0 Er1 Ra0 Rb0 Rc0 Rd0 Re0 Va1 Vb0 Vc0 Vd0 Vx0 Vy0 a0 b-0.01 c0 d0 e-964.732609921273 g0 p0 r90 t0 v18.6619860596508 y12  Vm5 u10 n"data/c0_r0.jpg"
	
	to script creation
	"i w h f Eb Eev Er Ra Rb Rc Rd Re Va Vb Vc Vd Vx Vy a b c d e g p r t v y Vm u n".split()
	'''
	
	# Width, int
	w = None
	# Height, int
	h = None
	# Field of view? int
	f = None
	# ?, int
	Eb = None
	# ?, int
	Eev = None
	# ?, int
	Er = None
	# ?, int
	Ra = None
	# ?, int
	Rb = None
	# ?, int
	Rc = None
	# ?, int
	Rd = None
	# ?, int
	Re = None
	# ?, int
	Va = None
	# ?, int
	Vb = None
	# ?, int
	Vc = None
	# ?, int
	Vd = None
	# ?, int
	Vx = None
	# ?, int
	Vy = None
	# ?, int
	a = None
	# ?, signed with decimal
	b = None
	# ?, int
	a = None
	# ?, int
	c = None
	# ?, int
	d = None
	# ?, signed with decimal
	e = None
	# ?, int
	g = None
	# ?, int
	p = None
	# ?, int
	r = None
	# ?, int
	t = None
	# ?, signed with decimal
	v = None
	# ?, int
	y = None
	# ?, int
	Vm = None
	# ?, int
	u = None
	# Image file name
	n = None
	
	# Entire line
	text = None

	def __init__(self):
		pass
		
	@staticmethod
	def from_line(pto_project, line):
		ret = Image()
		ret.text = line
		ret.reparse()
		return ret

	def reparse(self):
		for token in self.text.split(' '):
			t = token[0]
			r = token[1:]
			if t == 'i':
				# Ignore line identifier
				pass
			elif t == "w":
				self.w = int(r)
			elif t == "h":
				self.h = int(r)
			elif t == "f":
				self.f = int(r)
			elif t == "Eb":
				self.Eb = int(r)
			elif t == "Eev":
				self.Eev = int(r)
			elif t == "Er":
				self.Er = int(r)
			elif t == "Ra":
				self.Ra = int(r)
			elif t == "Rb":
				self.Rb = int(r)
			elif t == "Rc":
				self.Rc = int(r)
			elif t == "Rd":
				self.Rd = int(r)
			elif t == "Re":
				self.Re = int(r)
			elif t == "Va":
				self.Va = int(r)
			elif t == "Vb":
				self.Vb = int(r)
			elif t == "Vc":
				self.Vc = int(r)
			elif t == "Vd":
				self.Vd = int(r)
			elif t == "Vx":
				self.Vx = int(r)
			elif t == "Vy":
				self.Vy = int(r)
			elif t == "a":
				self.a = int(r)
			elif t == "b":
				self.b = int(r)
			elif t == "c":
				self.c = int(r)
			elif t == "d":
				self.d = int(r)
			elif t == "e":
				self.e = int(r)
			elif t == "g":
				self.g = int(r)
			elif t == "p":
				self.p = int(r)
			elif t == "r":
				self.r = int(r)
			elif t == "t":
				self.t = int(r)
			elif t == "v":
				self.v = int(r)
			elif t == "y":
				self.y = int(r)
			elif t == "Vm":
				self.Vm = int(r)
			elif t == "u":
				self.u = int(r)
			elif t == "n":
				self.n = int(r)
			else:
				raise Exception('Unrecognized: %s' % part)

	def __repr__(self, pto_project, line):
		self.text = "i "
		
		# w2816 h2112
		if self.w:
			self.text += 'w%d' % self.w
		if self.h:
			self.text += 'h%d' % self.w
		
		# f0
		if self.f:
			self.text += 'f%d' % self.w
		
		# Eb1 Eev0 Er1 
		if self.Eb:
			self.text += 'Eb%d' % self.w
		if self.Eev:
			self.text += 'Eev%d' % self.w
		if self.Er:
			self.text += 'Er%d' % self.w

		# Ra0 Rb0 Rc0 Rd0 Re0
		if self.Ra:
			self.text += 'Ra%d' % self.w
		if self.Rb:
			self.text += 'Rb%d' % self.w
		if self.Rc:
			self.text += 'Rc%d' % self.w
		if self.Rd:
			self.text += 'Rd%d' % self.w
		if self.Re:
			self.text += 'Re%d' % self.w
		
		# Va1 Vb0 Vc0 Vd0 Vx0 Vy0
		if self.Va:
			self.text += 'Va%d' % self.w
		if self.Vb:
			self.text += 'Vb%d' % self.w
		if self.Vc:
			self.text += 'Vc%d' % self.w
		if self.Vd:
			self.text += 'Vd%d' % self.w
		if self.Vx:
			self.text += 'Vx%d' % self.w
		if self.Vy:
			self.text += 'Vy%d' % self.w

		# a0 b-0.01 c0 d0 e-964.732609921273 
		if self.a:
			self.text += 'a%d' % self.w
		if self.b:
			self.text += 'b%f' % self.w
		if self.c:
			self.text += 'c%d' % self.w
		if self.d:
			self.text += 'd%d' % self.w
		if self.e:
			self.text += 'e%f' % self.w

		# g0 p0 r90 t0 v18.6619860596508
		if self.g:
			self.text += 'g%d' % self.w
		if self.p:
			self.text += 'p%d' % self.w
		if self.r:
			self.text += 'r%d' % self.w
		if self.t:
			self.text += 't%d' % self.w
		if self.v:
			self.text += 'v%f' % self.w
		
		# y12
		if self.x:
			self.text += 'x%d' % self.w
		if self.y:
			self.text += 'y%d' % self.w
		
		# Vm5
		if self.Vm:
			self.text += 'Vm%d' % self.w
		# u10
		if self.u:
			self.text += 'u%d' % self.w
		# n"data/c0_r0.jpg"
		if self.n:
			self.text += 'n%s' % self.n

class ControlPointImage:
	image = None
	x = None
	y = None
	# Index		
	n = None
	
class ControlPoint:
	# c n0 N1 x1444.778035 y233.742619 X1225.863118 Y967.737131 t0
	# Both of type ControlPointImage
	# Coordinates are increasing from upper left of image
	lower_image = None
	upper_image = None
	# What is t?
	t = None
	# Original text
	text = None

	def __init__(self):
		pass

	@staticmethod
	def from_line(pto_project, line):
		ret = ControlPoint()
		ret.text = line
		ret.reparse()
		return ret
	
	def reparse(self):
		for token in self.text.split(' '):
			t = token[0]
			r = token[1:]
			if t == 'c':
				# Ignore line identifier
				pass
			elif t == "n":
				self.lower_image.n = int(r)
			elif t == "N":
				self.upper_image.n = int(r)
			elif t == "x":
				self.lower_image.x = int(r)
			elif t == "X":
				self.upper_image.x = int(r)
			elif t == "y":
				self.lower_image.y = int(r)
			elif t == "Y":
				self.upper_image.y = int(r)
			elif t == "t":
				self.t = int(r)
			else:
				raise Exception('Unrecognized: %s' % part)

	def __repr__(self):
		self.text = 'c'
		self.text += ' n%d N%d' % (self.lower_image.image.get_index(), self.lower_image.image.get_index())
		self.text += ' x%f y%f' % (self.lower_image.x, self.lower_image.y)
		self.text += ' X%f Y%f' % (self.upper_image.x, self.upper_image.y)
		self.text += ' t0'
		return self.text

class VariableLine:
	text = None
	# Need to know image index to write these
	image = None
	d = None
	e = None
	p = None
	r = None
	x = None
	y = None
	
	def __init__(self):
		pass
	
	@staticmethod
	def from_line(pto_project, line):
		ret = VariableLine()
		ret.text = line
		return ret

	def __repr__(self):
		# v d1 e1 p1 r1 y1
		if d is None and e is None and p is None and r is None and x is None and y is None:
			return ''
			
		self.text = 'v '
		if self.d:	
			self.text += ' d%d' % (self.image.get_index())
		if self.e:	
			self.text += ' e%d' % (self.image.get_index())
		if self.p:	
			self.text += ' p%d' % (self.image.get_index())
		if self.r:	
			self.text += ' r%d' % (self.image.get_index())
		if self.x:	
			self.text += ' x%d' % (self.image.get_index())
		if self.y:	
			self.text += ' y%d' % (self.image.get_index())
		return self.text


'''
"autopano-sift-c" "--maxmatches" "0" "--maxdim" "10000" test.pto data/c0_r0.jpg data/c0_r1.jpg
	# Hugin project file generated by APSCpp

	p f2 w3000 h1500 v360  n"JPEG q90"
	m g1 i0

	# i: image file
	# w: width
	# h: height
	# f: field of view, default: 0
	# y: yaw: default 0
	# p: pitch: default 0
	# r: roll, default 90
	i w2816 h2112 f0 a0 b-0.01 c0 d0 e0 p0 r0 v180 y0  u10 n"data/c0_r0.jpg"
	i w2816 h2112 f0 a=0 b=0 c=0 d0 e0 p0 r0 v=0 y0  u10 n"data/c0_r1.jpg"

	v p1 r1 y1

	# automatically generated control points
	# c: control point
	# n0: lowercase n signifies lowercase coord letters
	# N0: uppercase N signifies uppercase coord letters
	# what is t?
	c n0 N1 x1444.778035 y233.742619 X1225.863118 Y967.737131 t0
	c n0 N1 x138.962214 y280.766699 X700.950061 Y337.168418 t0
	c n0 N1 x174.636854 y1506.062901 X409.952583 Y1520.077001 t0
	c n0 N1 x128.111790 y85.436614 X178.862171 Y82.166356 t0
	c n0 N1 x185.913687 y132.074929 X1316.285962 Y258.582828 t0
	c n0 N1 x575.842717 y186.222059 X807.577503 Y201.843139 t0
	c n0 N1 x106.501605 y234.781930 X415.561176 Y260.394812 t0
	c n0 N1 x106.501605 y234.781930 X415.561176 Y260.394812 t0
	c n0 N1 x282.454363 y861.246866 X524.759974 Y796.168031 t0
	c n0 N1 x263.741226 y1023.111056 X507.095358 Y958.025083 t0
	c n0 N1 x255.076623 y1046.452454 X521.642791 Y820.371911 t0
	c n0 N1 x21.128685 y1518.951592 X258.640812 Y1531.902643 t0
	c n0 N1 x154.281249 y1794.318825 X2276.028785 Y629.057778 t0
	c n0 N1 x184.953100 y1459.943702 X420.250084 Y1474.768162 t0
	c n0 N1 x184.953100 y1459.943702 X420.250084 Y1474.768162 t0
	c n0 N1 x176.023646 y1508.324113 X411.531954 Y1522.403846 t0
	c n0 N1 x120.663877 y774.190799 X1884.899395 Y804.325721 t0
	c n0 N1 x151.601649 y1534.284888 X386.385138 Y1549.239989 t0
	c n0 N1 x855.583962 y1992.647570 X1418.183265 Y51.846079 t0
	c n0 N1 x584.941773 y467.957317 X2294.246845 Y658.254045 t0
	c n0 N1 x1217.925413 y935.521381 X1477.978209 Y216.417092 t0
	c n0 N1 x389.932676 y626.473870 X628.094681 Y645.153382 t0
	c n0 N1 x1455.674496 y1538.841677 X1622.255876 Y476.350083 t0

	# :-)


Example file

	p f2 w3000 h1500 v360  n"JPEG q90"
	m g1 i0

	i w2816 h600 f0 a0 b-0.01 c0 d0 e0 p0 r0 v180 y0  u10 n"/tmp/0.6621735916207697.png"
	i w2816 h600 f0 a=0 b=0 c=0 d0 e0 p0 r0 v=0 y0  u10 n"/tmp/0.5022987786350409.png"

	v p1 r1 y1

	# numbers index into above images
	c n0 N1 x983.515978 y31.390674 X860.944595 Y132.080243 t0
	c n0 N1 x652.899413 y71.500283 X807.577503 Y201.843139 t0
	c n0 N1 x474.578071 y154.235865 X107.943696 Y223.202780 t0
	c n0 N1 x774.903103 y186.724081 X1830.890967 Y429.024407 t0
	c n0 N1 x1201.353730 y299.329003 X1269.005225 Y511.798210 t0
	c n0 N1 x1708.592510 y359.149116 X1873.061084 Y499.156064 t0
	c n0 N1 x192.653946 y158.115483 X80.809197 Y254.420106 t0


	# specify variables that should be optimized
	# Seems there is a lone v entry at the end
	# Hugin GUI groups the following by image: y, p, r
	# And these by lens: v, a, b, c, d, e
	# However, .pto specifies them for invidual by image
	v e0 
	v d1 e1 
	v d2 e2 
	v d3 e3 
	v 
'''
class PTOProject:
	# File name, if one exists
	file_name = None
	# Raw project text, None is not loaded
	text = None
	# If this is a temporary project, have it delete upon destruction
	temp_file = None
	
	# Those started with #hugin_
	option_lines = None
	# c N1 X1225.863118 Y967.737131 n0 t0 x1444.778035 y233.74261
	control_point_lines = None
	'''
	I bet lone v lines can be omitted
	# Variable lines
	v
	v d1 e1 p1 r1 y1
	v d2 e2 p2 r2 y2
	v d3 e3 p3 r3 y3
	v
	'''
	variable_lines = None

	def __init__(self):
		pass
	
	def index_to_image(self, index):
		return None
	
	@staticmethod
	def from_file_name(file_name, is_temporary = False):
		ret = PTOProject()
		ret.file_name = file_name
		if is_temporary:
			ret.temp_file = ManagedTempFile.from_existing(file_name)
		return ret

	@staticmethod
	def from_temp_file(temp_file):
		ret = PTOProject()
		ret.file_name = temp_file.file_name
		ret.temp_file = temp_file
		return ret

	@staticmethod
	def from_text(text):
		ret = PTOProject()
		ret.text = text
		ret.reparse()
		return ret

	@staticmethod
	def from_blank():
		return PTOProject.from_text('')

	def reparse(self):
		if True:
			print 'WARNING: pto parsing disabled'
			return
		self.option_lines = dict()
		self.variable_lines = list()

		for line in self.text().split('\n'):
			t = line[0]
			if t == 'c':
				# Ignore line identifier
				pass
			elif t == "n":
				self.lower_image.n = int(r)
			elif t == "N":
				self.upper_image.n = int(r)
			
	def regen(self):
		self.text = ''
		self.text += '# Generated by pr0ntools'

	def __repr__(self):
		if self.text:
			return self.text
		self.text = open(self.file_name).read()
		self.reparse()
		return self.text

	def get_a_file_name(self, prefix = None, postfix = None):
		'''If doesn't have a real file, create a temp file'''
		if self.file_name:
			return self.file_name
		if postfix is None:
			postfix = ".pto"
		self.temp_file = ManagedTempFile.get(prefix, postfix)
		self.file_name = self.temp_file.file_name
		self.save()
		return self.file_name

	def set_file_name(self, file_name):
		self.file_name = file_name

	def merge_into(self, others):
		'''Merge project into this one'''
		print 'others: %d' % len(others)
		temp = self.merge(others)
		self.text = temp.__repr__()
		if self.file_name:
			self.save()	

	def merge(self, others):
		'''Return a project containing both control points'''
		'''
		Does not allow in place replace, we have to move things around
		
		[mcmaster@gespenst bin]$ pto_merge --help
		pto_merge: merges several project files
		pto_merge version 2010.4.0.854952d82c8f

		Usage:  pto_merge [options] input.pto input2.pto ...

		  Options:
			 -o, --output=file.pto  Output Hugin PTO file.
									Default: <filename>_merge.pto
			 -h, --help			 Shows this help
		'''
		if len(others) == 0:
			print 'WARNING: skipping merge due to no other files'
			raise Exception('die')
			return
		
		pto_temp_file = ManagedTempFile.get(None, ".pto")

		command = "pto_merge"
		args = list()
		
		args.append("--output=%s" % pto_temp_file)

		# Possible this is still empty
		if os.path.exists(self.file_name):
			args.append(self.get_a_file_name())
		for other in others:
			 args.append(other.get_a_file_name())
		
		print args

		(rc, output) = Execute.with_output(command, args)
		# go go go
		if not rc == 0:
			print 'rc: %d' % rc
			raise Exception('failed pto_merge')
		return PTOProject.from_temp_file(pto_temp_file)

	def save(self):
		f = open(self.file_name, 'w')
		f.write(self.text)

	def save_as(self, file_name, is_new_filename = False):
		if text:
			f = os.open(file_name)
			f.write(text)
		elif self.file_name:
			shutil.copyfile(self.file_name, file_name)
		# empty project?
		else:
			raise Exception("tried to save empty project")
		
		if is_new_filename:
			self.file_name = file_name

	# reload is a builtin...not sure if it would conflict
	def reopen(self):
		f = open(self.file_name, 'r')
		self.text = f.read()

