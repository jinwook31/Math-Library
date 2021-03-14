# Math Library

### LAPACK
LAPACK(**L**inear **A**lgebra **Pac**kage)은 수치적 선형대수의 연산을 수행하는 함수를 제공하는 표준 수치 해석 SW 라이브러리이다.
LAPACK은 선형식, 선형 최소 제곱법을 제공하는 LINPACK과 고유값을 이용하는 EISPACK을 이용하여 개발되었고,
Cache-based architecture 형식의 BLAS(**B**asic **L**inear **A**lgebra **S**ubprograms) 인터페이스를 이용하여 개발되어서 빠른 처리 속도를 제공한다.

LAPACK은 driver routine을 갖고 low-level 컴퓨팅부터 보조 시스템을 구동하는 알고리즘, 전체 컴퓨팅 알고리즘까지 컴퓨터의 모든 부분에
다양하게 사용된다. SW개발 및 수치 해석에는 주로 LAPACK의 auxiliary routine을 사용한다.

LAPACK에서 더 확장된 것에는 ScaLAPACK, PLAPACK이 있다.

![structure](http://people.eecs.berkeley.edu/~demmel/cs267/lecture12/ScaLAPACK.gif)


### Levels of Routines

 * **driver routine**
	
	  선형식, 실수형 행렬의 고유치를 계산등 완전한 문제를 해결하는 알고리즘
	- Linear Equations
	- LLS Problems
	- LSE & GLM Problems
	- Standard Eigenvalue and Singular Value Problems
	- Generalized Eigenvalue and Singular Value Problems
 
 * **computational routine**
	
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

 * **auxiliary routine**
	
	  low-level 컴퓨팅에 주로 사용되는 것으로 행렬의 크기, matrix-norm 연산 등 subtask의 블록 알고리즘
	  block algorithm형식을 이용하면 다양한 컴퓨터에 적용 가능하다.
	

### Data Types and Precision

LAPACK은 실수와 복소수 data type을 이용할 수 있다. 몇가지 기능들을 제외하면 거의 모든 기능들이 두 타입 모두 제공된다.
또한, 단정도와 배정밀도 버젼도 각각 존재하는데 배정밀도 버젼은 자동적으로 수행된다. 복소수 행렬의 배정밀도 루틴은 Fortran의
COMPLEX*16의 데이터 타입으로 사용되어야 한다.


### Naming scheme
LAPACK의 subroutine은 Fortran때의 식별자 제한으로 짧고, 이해하기 어려운 형식을 갖고 있다.
LAPACK subroutine 식별자의 형식은 `pmmaaa`로 되어있고,

 * `p`는 어떤 종류의 상수가 사용되었는지 표시한다. S,D는 실수형을 의미하고 C,Z는 복소수를 의미한다.
   LAPACK95부터는 더 구체적인 data type을 위해 generic subroutine을 사용한다.

 * `mm`은 알고리즘의 결과로 반환될 행렬의 종류를 표시한다. 

 * `aaa`는 subroutine 안에 정의된 알고리즘에 대한 정의이다. 예를 들면, SV는 linear system을 해결하는 알고리즘, R은 rank-1 update 알고리즘이다.

즉, `SGEBRD`는 실수형 행렬의 Bidiagonal Reduction을 제공하는 단정도 알고리즘이고, `DGESV`는 일반적인 배정밀도 실수 행렬의 linear system을 해결하는 알고리즘이다.

 * LAPACK 함수 정리

 [http://www.mathkeisan.com/UsersGuide/e/lapack.html]


### BLAS
BLAS(**B**asic **L**inear **A**lgebra **S**ubprograms)은 벡터합, 스칼라곱, 행렬 곱등 기본적인 선형대수 문제를 해결하는 low-level routine의 집합이다.
BLAS는 주로 특수 부동소수점 하드웨어 같은 특정 장치(vector register, SIMD)에 최적화시켜 속도를 높이는데 사용된다. BLAS는 3단계로 되어있다.

##### Level 1
BLAS의 초기 루틴을 모두 갖고 있다. 즉, strided array(dot product, vector-norm)의 vector 연산을 다룬다. linear time을 소요한다.

![equation1](https://wikimedia.org/api/rest_v1/media/math/render/svg/1016203a2d42763e37d205e26e35a740a5fe53e5)


##### Level 2

이 레벨에서는 일반적인 벡터 행렬의 곱같은 matrix-vector operations을 다룬다. 시간은 quadratic time만큼 사용한다.

![equation2](https://wikimedia.org/api/rest_v1/media/math/render/svg/7658d5f7f6154333ccab6b64baa66163e5ef8d6f)

level1에서 matrix-vector연산을 컴파일러로 부터 숨겼던 것을 개선 하여 level2 개발로 인해 vector processor의 성능이 향상되었다.


##### Level 3
이 레벨에서는 matrix-matrix operation을 다룬다. 시간은 cubic time만큼 걸린다.

![equation3](https://wikimedia.org/api/rest_v1/media/math/render/svg/7f4f772e55eb95e54083f3bc4a177e171c4f7cdc)


또한, BLAS는 이식성이 좋기 때문에 LAPACK에서는 BLAS 인터페이스를 적용하였다. Level1은 LAPACK에서 성능보다는 편의를 위해 사용되었다. 
Level2는 많은 single vector processor들에서 좋은 성능을 보였지만, 그렇지 않은 processor에서는 메모리, 캐시 등에서 한계가 있었다.
Level3에서는 그 한계를 개선하였다. BLAS는 병렬처리도 가능하여 빠른 연산 속도와 Cache, Memory를 효율적으로사용할 수 있게 하였다.

BLAS와 LAPACK의 관계는 BLAS에서는 가장 기본적인 연산, low-level등을 담당하고, LAPACK은 BLAS에서 얻어진 값들을 갖고 처리하는 연산을 한다.
2개의 라이브러리는 독립적으로 컴파일 되며, LAPACK은 BLAS 위에 구현된 구조이다.

BLAS도 Fortran이였으므로 LAPACK과 비슷하지만 operation code가 1개 줄어든 `pmmaa` 방식을 따른다.

 * BLAS 함수 정리

 [http://www.netlib.org/lapack/lug/node145.html]


### ScaLAPACK

Scalable LAPACK으로 MIMD 병렬 컴퓨터를 위한 LAPACK의 subset이다. 현재는 message passing방식의 Single-Program-Multiple-Data형식으로 되어 있다.
ScaLAPACK은 LAPACK이 BLAS에 의존하듯 PBLAS(**P**arallel **BLAS**)에 의존한다. band와 packed matrix는 제공하지 않고, SVD, QR, D&C SVD등 몇몇 
고급 알고리즘들이 빠져 있다.

ScaLAPCK은 BLACS(Basic Linear Algebra Communication Subroutine)을 이용하여 행렬 데이터를 message passing방식으로 송수신하는 라이브러리도 사용한다.
BLACS는 다른 message passing 라이브러리(PVM, MPI 등)을 포함하여 여러 플랫폼 간에 통신이 가능하다.

 * 함수 정리

 [http://www.netlib.org/scalapack/explore-html/index.html]


### 다른 언어에서의 사용

 * C

	  C언어 에서 사용하기 위해서는 함수 호출 방법과 컴파일 방법에 대하여 고려를 해야한다.
	  Fortran77에서는 call by reference을 이용하기 때문에 C에서도 pointer를 이용하여 호출을 해야되고,
	  외부 라이브러리를 이용해야 하기 때문에 어디에 있는 어떤 라이브러리를 사용할 것인지 명시를 해야한다.
	  C언어 환경에서는 이런 것들을 해결한 clapack이라는 라이브러리를 사용하면 된다.

 * C++

	  LAPACK++, Armadillo, IT++

 * JAVA

	JLAPACK

 * OCaml

	Lacaml

 * 확장 라이브러리

	Intel Math Kernel Lib, IBM Engineering and Scientific Subroutine Lib, CUDA



### 언어별 속도 및 성능 비교

 * Fortran은 Column, C/C++은 Row 방식으로 메모리에  정렬이 된다. 그렇기 때문에  C/C++에서 BLAS, LAPACK 함수를 호출하면 뒤집어야한다.
   그 때문에 약간의 속도 차이가 생긴다.

 * 사용 언어보다 CPU, Memory 등의 영향을 제일 많이 받는다.



[참조]

[http://www.mitchr.me/SS/exampleCode/blas.html]

[https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms]

[https://en.wikipedia.org/wiki/LAPACK]

[http://www.netlib.org/lapack/lug/node1.html]

[https://www8.cs.umu.se/kurser/5DV050/VT08/utdelat/F7.pdf]

[http://people.eecs.berkeley.edu/~demmel/cs267/lecture12/lecture12.html]
