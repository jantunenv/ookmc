import numpy as np
import sys
import io

class Object:
	name = None
	lattice_type = None
	lattice_constant = None
	offset = None
	def __init__(self):
		pass

	def init_with_strings(self, name, lattice_type, lattice_constant, offset_x, offset_y, offset_z):
		self.name = name
		self.lattice_type = lattice_type
		self.lattice_constant = string_to_float(lattice_constant)
		self.offset = np.asarray([string_to_float(offset_x), string_to_float(offset_y), string_to_float(offset_z)])

def read_lattices(fname):
	with open(fname, 'r') as f:
		lines = f.readlines()

	lattices = {}

	i = 0
	while(True):
		if(i>=len(lines)):
			break
		line = lines[i]
		check_comment = line.split("#")
		if(len(check_comment)>1):
			content = check_comment[0]
			comment = check_comment[1]
		else:
			content = check_comment[0]
		if(content):
			n = int(content)
			name = lines[i+1].split()[0]
			file_like_handler = io.StringIO("".join(lines[i+2:i+2+n]))
			lattices[name] = np.loadtxt(file_like_handler)
			i = i + 2 + n
		else:
			i = i+1
	return(lattices)

def read_objects(fname):
		with open(fname, 'r') as f:
				lines = f.readlines()

		objects = []

		i = 0
		while(True):
				if(i>=len(lines)):
						break
				line = lines[i]
				check_comment = line.split("#")
				if(len(check_comment)>1):
						content = check_comment[0]
						comment = check_comment[1]
				else:
						content = check_comment[0]
				if(content):
					if(bool(content[1])):
						object = Object()
						content = content.split()
						object.init_with_strings(content[0], content[2], content[3], content[4], content[5], content[6])
						objects.append(object)
				i = i+1

		return(objects)

def string_to_float(string):
	if("/" in string):
		a,b = string.split("/")
		c = float(a)/float(b)
	else:
		c = float(string)

	return(c)

def main():
	lattice_file ="crystal_structures.dat"
	objects_file ="objects.dat"

	lattices = read_lattices(lattice_file)
	objects = read_objects(objects_file)


	sites = []

	for object in objects:
		coords = (lattices[object.lattice_type] + object.offset)*object.lattice_constant
		if(coords.ndim == 1):
			sites.append("{} {} {} {}".format(object.name, coords[0], coords[1], coords[2]))
		else:
			for line in coords:
								sites.append("{} {} {} {}".format(object.name, line[0], line[1], line[2]))

	print(len(sites))
	print("Lattice=\"{0} 0.0 0.0 0.0 {0} 0.0 0.0 0.0 {0}\"".format(np.max([obj.lattice_constant for obj in objects])))
	for site in sites:
		print(site)

main()
