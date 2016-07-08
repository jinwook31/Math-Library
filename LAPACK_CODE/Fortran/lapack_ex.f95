program solve
	
	implicit none
	integer, parameter :: n =3
	real(kind=8), dimension(n) :: x,b
	real(kind=8), dimension(n,n) :: a
	integer :: i, info, lda, ldb, nrhs
	integer, dimension(n) :: ipiv

	a = reshape((/3.0,2.0,-1.0,2.0,-2.0,0.5,-1.0,4.0,-1.0/),(/n,n/))
	b = (/1.0, -2.0, 0.0/)
	x = b

	nrhs = 1
	lda = n
	ldb = n

	call dgesv(n, nrhs, a, lda, ipiv, x, ldb, info)

	print *, "result : "

	do i=1,n
		print '("X",i1,":",f16.6)',i,x(i)
	end do

end program solve
