program test

      double precision a(5), b(5)
      integer i
	real :: T1,T2

	call CPU_TIME(T1);
      do i= 1,5
         a(i)= i
      enddo


      call dcopy(5, a, 1, b, 1) 
	CALL cpu_time(T2)

	Print '("CPU Time :",f6.3,"Sec")',T2-T1
      do i= 1,5
         write(*,*) b(i)
      enddo

end program
