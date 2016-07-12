program test

      double precision a(5), b(5)
      integer i

      do i= 1,5
         a(i)= i
      enddo


      call dcopy(5, a, 1, b, 1) 

      do i= 1,5
         write(*,*) b(i)
      enddo

end program
