#LAPACK Lib
LAPACK(**L**inear **A**lgebra **Pac**kage)은 수치적 선형대수의 연산을 수행하는 함수를 제공하는 표준 수치 해석 SW 라이브러리이다.
LAPACK은 선형식, 선형 최소 제곱법을 제공하는 LINPACK과 고유값을 이용하는 EISPACK을 이용하여 개발되었고,
Cache-based architecture 형식의 BLAS 인터페이스를 이용하여 개발되어서 빠른 처리 속도를 제공한다.

LAPACK에서 더 확장된 것에는 ScaLAPACK, PLAPACK이 있다. BSD style license를 가지고, 일부를 제외하고는 무료 SW 이다.

###Naming scheme
LAPACK의 subroutine은 Fortran때의 식별자 제한으로 짧고, 이해하기 어려운 형식을 갖고 있다.

LAPACK subroutine 식별자의 형식은 `pmmaaa`로 되어있고,

*`p`는 

*`mm`

*`aaa`

[참조][https://en.wikipedia.org/wiki/LAPACK]
