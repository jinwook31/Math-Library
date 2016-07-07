#LAPACK
LAPACK(**L**inear **A**lgebra **Pac**kage)은 수치적 선형대수의 연산을 수행하는 함수를 제공하는 표준 수치 해석 SW 라이브러리이다.
LAPACK은 선형식, 선형 최소 제곱법을 제공하는 LINPACK과 고유값을 이용하는 EISPACK을 이용하여 개발되었고,
Cache-based architecture 형식의 BLAS(**B**asic **L**inear **A**lgebra **S**ubprograms) 인터페이스를 이용하여 개발되어서 빠른 처리 속도를 제공한다.

LAPACK은 driver routine을 갖고 low-level 컴퓨팅부터 보조 시스템을 구동하는 알고리즘, 전체 컴퓨팅 알고리즘까지 컴퓨터의 모든 부분에
다양하게 사용된다. SW개발 및 수치 해석에는 주로 LAPACK의 auxiliary routine을 사용한다.

LAPACK에서 더 확장된 것에는 ScaLAPACK, PLAPACK이 있다.


###Levels of Routines

 * **driver**
	
	선형식, 실수형 행렬의 고유치를 계산등 완전한 문제를 해결하는 알고리즘
	- Linear Equations
	- LLS Problems
	- LSE & GLM Problems
	- Standard Eigenvalue and Singular Value Problems
	- Generalized Eigenvalue and Singular Value Problems
 
 * **computational**
	
	LU 인수 분해, 일반 실수형 행렬을 tridiagonal 행렬로 줄이는 연산 등의 명확한 작업을 할때 직접적으로 사용되는 알고리즘
	- Linear Equations
	- Orthogonal Factorization and Linear Least Squares Problem
	- Generalized Orthogonal Factorizations and Linear Least Squares Problems
	- Symmetric Eigenproblems
	- Nonsymmetric Eigenproblems
	- Singular Value Decomposition
	- Generalized Symmetric Definite Eigenproblems
	- Generalized Nonsymmetric Eigenproblems
	- Generalized (or Quotient) Singular Value Decomposition

 * **auxiliary**
	
	low-level 컴퓨팅에 주로 사용되는 것으로 행렬의 크기, matrix-norm 연산 등 subtask의 블록 알고리즘 
	

###Data Types and Percision

LAPACK은 실수와 복소수 data type을 이용할 수 있다. 몇가지 기능들을 제외하면 거의 모든 기능들이 두 타입 모두 제공된다.
또한, 단정도와 배정밀도 버젼도 각각 존재하는데 배정밀도 버젼은 자동적으로 수행된다. 복소수 행렬의 배정밀도 루틴은 Fortan의
COMPLEX*16의 데이터 타입으로 사용되어야 한다.


###Naming scheme
LAPACK의 subroutine은 Fortran때의 식별자 제한으로 짧고, 이해하기 어려운 형식을 갖고 있다.

LAPACK subroutine 식별자의 형식은 `pmmaaa`로 되어있고,

 * `p`는 어떤 종류의 상수가 사용되었는지 표시한다. S,D는 실수형을 의미하고, C,Z는 복소수를 의미한다.
   LAPACK95부터는 더 구체적인 data type을 위해 generic subroutine을 사용한다.

 * `mm`은 알고리즘의 결과로 반환될 행렬의 종류를 표시한다. 

 * `aaa`는 subroutine 안에 정의된 알고리즘에 대한 정의이다. 예를 들면, SV는 linear system을 해결하는 알고리즘, R은 rank-1 update 알고리즘이다.

즉, `SGEBRD`는 실수형 행렬의 Bidiagonal Reduction을 제공하는 단정도 알고리즘이고, `DGESV`는 일반적인 배정밀도 실수 행렬의 linear system을 해결하는 알고리즘이다.



###BLAS



###ScaLAPACK



###다른 언어에서의 사용

 * C

	C언어 에서 사용하기 위해서는 함수 호출 방법과 컴파일 방법에 대하여 고려를 해야한다.
	Fortan77에서는 call by reference을 이용하기 때문에 C에서도 pointer를 이용하여 호출을 해야되고,
	외부 라이브러리를 이용해야 하기 때문에 어디에 있는 어떤 라이브러리를 사용할 것인지 명시를 해야한다.

 * C++

	LAPACK++, Armadillo, IT++

 * OCaml

	Lacaml


[참조]
[https://en.wikipedia.org/wiki/LAPACK]
[http://www.netlib.org/lapack/lug/node1.html]
