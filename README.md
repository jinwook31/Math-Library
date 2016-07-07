#LAPACK Lib
LAPACK(**L**inear **A**lgebra **Pac**kage)은 수치적 선형대수의 연산을 수행하는 함수를 제공하는 표준 수치 해석 SW 라이브러리이다.
LAPACK은 선형식, 선형 최소 제곱법을 제공하는 LINPACK과 고유값을 이용하는 EISPACK을 이용하여 개발되었고,
Cache-based architecture 형식의 BLAS(**B**asic **L**inear **A**lgebra **S**ubprograms) 인터페이스를 이용하여 개발되어서 빠른 처리 속도를 제공한다.

LAPACK은 driver routine을 갖고 low-level 컴퓨팅부터 보조 시스템을 구동하는 알고리즘, 전체 컴퓨팅 알고리즘까지 컴퓨터의 모든 부분에
다양하게 사용된다. SW개발 및 수치 해석에는 주로 LAPACK의 auxiliary routine을 사용한다.

LAPACK에서 더 확장된 것에는 ScaLAPACK, PLAPACK이 있다.


###Levels of Routines

 * **driver**
 
 * **computational**

 * **auxiliary**



###Naming scheme
LAPACK의 subroutine은 Fortran때의 식별자 제한으로 짧고, 이해하기 어려운 형식을 갖고 있다.

LAPACK subroutine 식별자의 형식은 `pmmaaa`로 되어있고,

 * `p`는 어떤 종류의 상수가 사용되었는지 표시한다. S,D는 실수형을 의미하고, C,Z는 a=bi(a, b는 실수, i 허수)형태의 complec number를 의미한다.
   LAPACK95부터는 더 구체적인 data type을 위해 generic subroutine을 사용한다.

 * `mm`은 알고리즘의 결과로 반환될 행렬의 종류를 표시한다. 

 * `aaa`는 subroutine 안에 정의된 알고리즘에 대한 정의이다. 예를 들면, SV는 linear system을 해결하는 알고리즘, R은 rank-1 update 알고리즘이다.

즉, `SGEBRD`는 실수형 행렬의 Bidiagonal Reduction을 제공하는 단정도 알고리즘이고, `DGESV`는 일반적인 배정밀도 실수 행렬의 linear system을 해결하는 알고리즘이다.



###BLAS



###ScaLAPACK



[참조][https://en.wikipedia.org/wiki/LAPACK]
[참조][http://www.netlib.org/lapack/lug/node1.html]
