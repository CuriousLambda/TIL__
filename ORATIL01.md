# Oracle 단순조회, 별칭, 컬럼명 만들기
- 오라클 접속 후, C##SCOTT이라는 다른 사용자 계정을 만들었다.
  - 따라서 이곳에서 다루는 모든 테이블 명 앞에는 <C##SCOTT.>이 붙을 것이다.
- 이 계정에서 오라클 조회 실습을 해보려고 한다.
- 오라클은 항상 맨 마지막 문구가 끝나면 세미콜론(;)을 작성해주어야 한다.
- 세미콜론이 있는 곳까지를 구문 끝이라고 생각하기 때문에 작성해주지 않는다면 다른 SQL조회문까지 한번에 읽어드리는 오류가 발생할 수 있다.

<br/>

> 테이블은 3가지 테이블을 사용했다.
> 1. EMP테이블 - 사원테이블, EMPNO(사원번호), ENAME(사원이름), JOB(역할/직업), MGR(매니저), HIREDATE(입사일), SAL(봉급), COMM(커미션), DEPTNO(부서번호) 를 컬럼으로 가지고 있다.
> 2. DEPT테이블 - 부서테이블, DEPTNO(부서번호), LOC(부서위치), DNAME(부서이름)을 컬럼으로 가지고 있다.
> 3. SALGRADE테이블 - 봉급등급테이블, LOSAL(최저봉급), HISAL(최고봉급), GRADE(등급)을 컬럼으로 가지고 있다.
> 4. BONUS테이블 - 보너스테이블, EANME(사원이름), JOB(역할/직업), SAL(봉급), COMM(커미션)으로 이루어져 있다.

<br/>

## 1. 단순조회(SELECT 컬럼 FROM 테이블명;)
<br/>

- 전체 데이터를 출력할 때는 __*__ 를 이용한다.


예시
```oracle
-- 사원테이블에서 전체 데이터를 출력하자.

SELECT * FROM C##SCOTT.EMP;
```
출력결과
```oracle
EMPNO	ENAME	JOB	        MGR	    HIREDATE	SAL	    COMM	DEPTNO
7369	SMITH	CLERK	    7902	80/12/17	800		20
7499	ALLEN	SALESMAN	7698	81/02/20	1600	300	    30
7521	WARD	SALESMAN	7698	81/02/22	1250	200	    30
7566	JONES	MANAGER	    7839	81/04/02	2975	30	    20
7654	MARTIN	SALESMAN	7698	81/09/28	1250	300	    30
7698	BLAKE	MANAGER	    7839	81/04/01	2850		    30
7782	CLARK	MANAGER	    7839	81/06/01	2450		    10
7788	SCOTT	ANALYST	    7566	82/10/09	3000		    20
7839	KING	PRESIDENT		    81/11/17	5000	3500	10
7844	TURNER	SALESMAN	7698	81/09/08	1500	0	    30
7876	ADAMS	CLERK	    7788	83/01/12	1100		    20
7900	JAMES	CLERK	    7698	81/10/03	950		30
7902	FORD	ANALYST	    7566	81/10/03	3000		    20
7934	MILLER	CLERK	    7782	82/01/23	1300		    10
```

<br/>

- 특정한 컬럼 데이터만 조회하고 싶다면 SELECT 뒤에 조회하고 싶은 컬럼명을 ,로 이어서 작성하면 된다.

예시02
```oracle
-- 사원테이블에서 사원의 이름과 월급을 출력하자.

SELECT ENAME, SAL
FROM C##SCOTT.EMP;
```

출력결과
```oracle
ENAME	SAL
SMITH	800
ALLEN	1600
WARD	1250
JONES	2975
MARTIN	1250
BLAKE	2850
CLARK	2450
SCOTT	3000
KING	5000
TURNER	1500
ADAMS	1100
JAMES	950
FORD	3000
MILLER	1300
```
<br/>

## 2. 별칭 만들기
- 별칭 : 컬럼별칭, 테이블의 별칭
- 컬럼명 별칭, 컬럼명 AS 별칭,
- 컬럼명 "별  칭", 컬럼명 AS "별  칭" __즉, 별칭 안에 공백 있으면 무조건 ""__ 필요

<br/>

예시03
```oracle
-- 사원테이블에서 사원의 번호를 사번이라고 출력하고 사원의 이름을 이름이라고 출력하자.

SELECT EMPNO 사번, ENAME 이름
FROM C##SCOTT.EMP;
```
```oracle
SELECT EMPNO AS 사번, ENAME AS 이름
FROM C##SCOTT.EMP;
```
출력결과
```oracle
사번	이름
7369	SMITH
7499	ALLEN
7521	WARD
7566	JONES
7654	MARTIN
7698	BLAKE
7782	CLARK
7788	SCOTT
7839	KING
7844	TURNER
7876	ADAMS
7900	JAMES
7902	FORD
7934	MILLER
```

<br/>

예시04
```oracle
SELECT EMPNO "사 번", ENAME "이 름"
FROM C##SCOTT.EMP;
```
```oracle
SELECT EMPNO AS "사 번", ENAME AS "이 름"
FROM C##SCOTT.EMP;
```
출력결과
```oracle
사 번	이 름
7369	SMITH
7499	ALLEN
7521	WARD
7566	JONES
7654	MARTIN
7698	BLAKE
7782	CLARK
7788	SCOTT
7839	KING
7844	TURNER
7876	ADAMS
7900	JAMES
7902	FORD
7934	MILLER
```

예시05
- 테이블에 별칭을 주어 각 테이블에서 원하는 컬럼만 조회할 수도 있다.
- 이 예시에서는 EMP테이블의 별칭을 E로, DEPT테이블의 별칭을 D로 주었다.
```oracle
-- 사원테이블의 내용과 부서테이블의 내용 중 사원이름과 부서번호를 출력해보자.

SELECT ENAME, D.DEPTNO FROM C##SCOTT.EMP E, C##SCOTT.DEPT D;
```
출력결과
```oracle
ENAME	DEPTNO
SMITH	10
ALLEN	10
WARD	10
JONES	10
MARTIN	10
BLAKE	10
CLARK	10
SCOTT	10
KING	10
TURNER	10
ADAMS	10
JAMES	10
FORD	10
MILLER	10
SMITH	20
ALLEN	20
WARD	20
JONES	20
MARTIN	20
BLAKE	20
CLARK	20
SCOTT	20
KING	20
TURNER	20
ADAMS	20
JAMES	20
FORD	20
MILLER	20
SMITH	30
ALLEN	30
WARD	30
JONES	30
MARTIN	30
BLAKE	30
CLARK	30
SCOTT	30
KING	30
TURNER	30
ADAMS	30
JAMES	30
FORD	30
MILLER	30
SMITH	40
ALLEN	40
WARD	40
JONES	40
MARTIN	40
BLAKE	40
CLARK	40
SCOTT	40
KING	40
TURNER	40
ADAMS	40
JAMES	40
FORD	40
MILLER	40
```
<br/>

예시06
- 만약, 데이터가 NUMBER타입이라면, 연산도 가능하다.
```oracle
-- 사원의 테이블에서 사원 이름과 봉급을 출력하되, 봉급은 연봉으로 출력하자.
-- 즉, 연봉 = 봉급*12
-- 연봉의 컬럼명은 "연봉"으로 조회하자.

 SELECT ENAME, SAL*12 연봉
 FROM C##SCOTT.EMP;
 ```
 출력결과
 ```oracle
 ENAME	연봉
SMITH	9600
ALLEN	19200
WARD	15000
JONES	35700
MARTIN	15000
BLAKE	34200
CLARK	29400
SCOTT	36000
KING	60000
TURNER	18000
ADAMS	13200
JAMES	11400
FORD	36000
MILLER	15600
```
<br/>

## 3. 연결문자열(" | | ")
- 연결문자열 " | | "을 사용하여 출력 데이터의 형식을 만들 수 있다.
- 예를 들어, 봉급 데이터 뒤에 $와 같은 문자열을 추가해서 조회되게 할 수 있다.
- 또한 컬럼끼리 연결하기 위해서도 연결 문자열을 사용할 수 있다.
<br/>

예시07
```oracle
-- 사원의 테이블에서 사원 이름과 봉급을 출력하되, "00의 봉급은 00이다"
 -- || (연결문자열)

 SELECT ENAME ||'의 봉급은' || SAL ||'이다'
 FROM C##SCOTT.EMP;
 ```
 출력결과
 ```oracle
 ENAME||'의봉급은'||SAL||'이다'
SMITH의 봉급은800이다
ALLEN의 봉급은1600이다
WARD의 봉급은1250이다
JONES의 봉급은2975이다
MARTIN의 봉급은1250이다
BLAKE의 봉급은2850이다
CLARK의 봉급은2450이다
SCOTT의 봉급은3000이다
KING의 봉급은5000이다
TURNER의 봉급은1500이다
ADAMS의 봉급은1100이다
JAMES의 봉급은950이다
FORD의 봉급은3000이다
MILLER의 봉급은1300이다
홍길동의 봉급은300이다
정길동의 봉급은3000이다
```
