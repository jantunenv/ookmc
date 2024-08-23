import numpy as np

def xrot(angle):
	M = np.asarray([
		[1,0,0],
		[0,np.cos(angle),-np.sin(angle)],
		[0,np.sin(angle),np.cos(angle)]
		])
	return(M)

def yrot(angle):
	M = np.asarray([
		[np.cos(angle),0,np.sin(angle)],
		[0,1,0],
		[-np.sin(angle),0,np.cos(angle)]
		])
	return(M)

def zrot(angle):
	M = np.asarray([
		[np.cos(angle),-np.sin(angle),0],
		[np.sin(angle),np.cos(angle),0],
		[0,0,1]
		])
	return(M)

def xref():
	M = np.asarray([[-1,0,0],[0,1,0],[0,0,1]])
	return(M)

def yref():
	M = np.asarray([[1,0,0],[0,-1,0],[0,0,1]])
	return(M)

def zref():
	M = np.asarray([[1,0,0],[0,1,0],[0,0,-1]])
	return(M)

def main():

	x = np.asarray([1,0,0])

	coords = []
	n = 20
	print(n)
	print("moi")
	for i in range(n):
		coords.append(xref().dot(xrot(np.pi).dot(yrot(np.pi*2/3).dot(zref().dot(zrot(np.pi/2.0).dot(x))))))
		x = coords[-1]
		print(x[0], x[1], x[2])


main()
