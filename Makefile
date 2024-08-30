ff=gfortran
flags=-O3
debug=-g

bin/ookmc : src/ookmc.f03
	${ff} src/ookmc.f03 ${flags} -o bin/ookmc
