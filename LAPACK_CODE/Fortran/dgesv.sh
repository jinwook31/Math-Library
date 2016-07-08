rm *.o *.exe *.mod
gfortran -c dgesv.f95
gfortran *.o -L$HOME/libf77/$ARCH  -llapack -lblas
mv a.out dgesv.exe
./dgesv.exe
