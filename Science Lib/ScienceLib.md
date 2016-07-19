#Science & Math Lib

###Java

 * Apache Commons

	자바 언어 관련 재사용 가능한 컴포넌트 개발을 위한 오픈소스 라이브러리로, Commons Proper라는 것에 Math, BSF, CSV 등
	수학 이외에도 여러 다양한 프로젝트들이 존재한다. 그중에서 가장 과학 및 수학에 관련된 Apache Math(3.6.1)를 보면
	org.apache.commons.math3 안에 총 76개의 package가 존재한다. 그 안에는 총 918개의 class가 존재한다.
	총 메소드 개수는 6534개 이다.
	
	Apache Math 내에는 벡터연산을 하는 선형 class와 log 같은 단순 연산등 비선형 관련된 문제들을 모두 해결할 수 있는 기능들이 있다. 

	[http://commons.apache.org/proper/commons-math/javadocs/api-3.6.1/index.html]

###C

 * GNU Scientific Library

	이 라이브러리는 C에서 가장 많이 쓰이는 수학, 과학 분석 라이브러리이다. 선형대수, Blas support, Eigensystem 등 넓게 지원하며
	Blas, ATLAS, LUSH등을 이용하여 구현하였다. 다른 라이브러리와 별개이기 때문에 컴파일 및 설치가 쉽고, 총 2082개의 함수로 되어있다.

	[https://www.gnu.org/software/gsl/manual/gsl-ref.pdf]


###C++

 * Armadillo

	사용하기 간편하고, streamlined base 연산 선형대수 라이브러리이다. int, floating point, complex, subset of Tigonometric,
	statistic Function을 제공한다. LAPACK과 ATLAS 라이브러리 기반으로 구현되었으며 Math Kernel Library, AMD Core Math Library와
	같이 사용되기도 한다.

	Armadillo는 uBLAS와도 관계가 있다. template metaprogramming 방식을 이용하여 구현되어서 Delayed evaluation과 optimisation을 제공한다.

	총 474개의 class가 있고, 함수들은 간단히 행렬 이름 1개만으로 호출하거나, 연산 할 값들을 이용하여 호출한다.

	[http://arma.sourceforge.net/docs.html]

	[http://arma.sourceforge.net/armadillo_joss_2016.pdf] 
