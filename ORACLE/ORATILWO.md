# Oracle - WHERE, WHERE절 연산자, ORDER BY
## 1. WHERE 절
형식
```oracle
SELECT 컬럼리스트
FROM 테이블리스트
WHERE 조건식;
```
- 열이름, 비교연산자, 조건연산자 등으로 리턴값이 TRUE인 데이터만 추출한다.
-  비교대상 : 상수, 열이름, 값목록 등
- 산술, 비교, 논리
  - LIKE, IN, NOT, BETWEEN, IS NULL, IS NOT NULL, ANY, ALL 등

<br/>

### 예시01
```oracle
-- 담당업무(JOB)가 MANAGER인 사원 정보를 출력해보자.

SELECT * FROM C##SCOTT.EMP WHERE JOB = 'MANAGER';
```
출력결과
```oracle
EMPNO	ENAME	JOB	    MGR	    HIREDATE	SAL	    COMM	DEPTNO
7566	JONES	MANAGER	7839	81/04/02	2975	30	    20
7698	BLAKE	MANAGER	7839	81/04/01	2850		    30
7782	CLARK	MANAGER	7839	81/06/01	2450		    10
```
- 쿼리문을 작성할 때는 대/소문자가 상관 없지만, 직접 값(VALUE)을 비교할 떄는 데이터의 값을 그대로 비교하기 때문에 대/소문자를 확실히 구분 해야한다.
- 데이터가 문자열 또는 날짜인 경우 `' '` 필요
- 숫자일 경우는 `' '` 필요 없음

<br/>

## 2. 논리연산자
1) WHERE 절은 여러 개의 조건을 지정할 때 사용한다.
2) AND는 모든 조건의 결과가 TRUE여야 선택된다.
3) OR는 한 조건의 결과라도 TRUE이면 선택된다.
4) NOT은 뒤따르는 조건의 결과가 FALSE이면 선택된다.
5) 우선순위는 NOT, AND, OR 순이다.
6) (  ) 는 모든 우선 순위 규칙보다 우선한다.  

<br/>  

- 논리 연산자는 두 조건의 결과를 결합하여 하나의 결과를 생성하거나 단일 조건의 결과를 부정하기도 한다.
- 조건의 전체가 참인 경우에만 행이 반환된다.

<br/>

### 예시02

```oracle
-Q21) 급여가 1300에서 1700사이에 해당하는 사원의 이름, 봉급을 출력하자.

SELECT ENAME, SAL FROM C##SCOTT.EMP WHERE SAL BETWEEN 1300 AND 1700;
```
```
SELECT ENAME, SAL FROM C##SCOTT.EMP WHERE SAL>= 1300 AND SAL <=1700;
```
출력결과
```oracle
ENAME	SAL
ALLEN	1600
TURNER	1500
MILLER	1300
```
- 대상컬럼 BETWEEN __작은값__ AND __큰값__  [EXPR >= A AND EXPR <=B]
  > 작은값 / 큰값 순서 바뀌면 안된다!<br/>
  > 만약 작은값과 큰값의 순서를 바꿔서 실행시킨다면 열이름만 출력되고 아무것도 출력되지 않는다.


<br/>

### 예시03 - _IN 연산자_
```oracle
-- 사원번호가 7902, 7788, 7566 인 사원의 이름과 사원번호, 입사일을 출력하자.

SELECT ENAME, EMPNO, TO_CHAR(HIREDATE, 'YYYY"년"-MM"월"-DD"일" DAY')
FROM C##SCOTT.EMP WHERE EMPNO IN(7902,7788,7566);
```
출력결과
```oracle
ENAME	EMPNO	TO_CHAR(HIREDATE,'YYYY"년"-MM"월"-DD"일"DAY')
JONES	7566	1981년-04월-02일 목요일
SCOTT	7788	1982년-10월-09일 토요일
FORD	7902	1981년-10월-03일 토요일
```
- IN 연산자
  - 여러값 중에 일치하는 값 : EXPR IN(3,4,5)
  - 여러 목록 값 중에 하나와 일치하는 값을 리턴
  - 즉, 목록 중 하나라도 일치하는 값이 있으면 그 값을 리턴한다.
  - IN = ANY 연산자와 같다.
  - NOT IN !=ALL과 같다.

<br/>

### 예시04 - _LIKE 연산자_
```oracle
-- 사원의 이름이 s로 시작하는 사원의 이름과 봉급을 출력하자.

SELECT ENAME, SAL FROM C##SCOTT.EMP
WHERE ENAME LIKE 'S%';
```
출력결과
```oracle
ENAME	SAL
SMITH	800
SCOTT	3000
```
- LIKE 연산자
  - 문자의 패턴이 같은 값
  - 특정 패턴에 속하는 문자열을 추출하는 키워드
  - % : 임의의 길이 문자열(공백가능)
  - _ : 한글자
  - ESCAPE : 검색할 문자에 %, _ 문자 대응

<br/>

### 예시05 - NULL, NVL
```oracle
-- 커미션이 측정되지 않은 사원을 출력해보자.

SELECT * FROM C##SCOTT.EMP
WHERE COMM IS NULL;
```
출력결과
```oracle
EMPNO	ENAME	JOB	    MGR	    HIREDATE	SAL	    COMM	DEPTNO
7369	SMITH	CLERK	7902	80/12/17	800		(null)  20
7698	BLAKE	MANAGER	7839	81/04/01	2850	(null)	30
7782	CLARK	MANAGER	7839	81/06/01	2450	(null)	10
7788	SCOTT	ANALYST	7566	82/10/09	3000	(null)	20
7876	ADAMS	CLERK	7788	83/01/12	1100	(null)	20
7900	JAMES	CLERK	7698	81/10/03	950		(null)  30
7902	FORD	ANALYST	7566	81/10/03	3000	(null)	20
7934	MILLER	CLERK	7782	82/01/23	1300	(null)	10
```
<br/>


```oracle
-- 커미션이 측정된 사원을 출력해보자.

SELECT * FROM C##SCOTT.EMP
WHERE COMM IS NOT NULL;
```
출력결과
```oracle
EMPNO	ENAME	JOB	        MGR	    HIREDATE	SAL	    COMM	DEPTNO
7499	ALLEN	SALESMAN	7698	81/02/20	1600	300	    30
7521	WARD	SALESMAN	7698	81/02/22	1250	200	    30
7566	JONES	MANAGER	    7839	81/04/02	2975	30	    20
7654	MARTIN	SALESMAN	7698	81/09/28	1250	300	    30
7839	KING	PRESIDENT		    81/11/17	5000	3500	10
7844	TURNER	SALESMAN	7698	81/09/08	1500	0	    30
```
- COMM의 값이 0인것도 NULL(아예 측정되지 않은 것)은 아니므로 커미션이 측정된 것이다.
- NULL은 특이하게 `!= NULL` 은 되지 않는다.

<br/>

- 그럼 NULL값이 있으면 데이터를 다루기 불편한데 어떻게 할 수 있을까?

<br/>

### 예시05-1
```oracle
SELECT EMPNO, ENAME,COMM, NVL(COMM, 0) 치환결과
FROM C##SCOTT.EMP;
```
출력결과
```oracle
EMPNO	ENAME	COMM	치환결과
7369	SMITH		    0
7499	ALLEN	300	    300
7521	WARD	200	    200
7566	JONES	30	    30
7654	MARTIN	300	    300
7698	BLAKE		    0
7782	CLARK		    0
7788	SCOTT		    0
7839	KING	3500	3500
7844	TURNER	0	    0
7876	ADAMS		    0
7900	JAMES		    0
7902	FORD		    0
7934	MILLER		    0
```
- `NVL(치환할 열 또는 데이터, 치환할 값)`을 해주면 NULL값을 치환할 수 있다.

<br/>

## 3. ORDER BY (데이터 정렬)
형식
```oracle
SELECT 컬럼리스트
FROM 테이블리스트
ORDER BY ASC|DESC 컬럼명;
```
- ORDER BY 는 SELECT 문장의 마지막에 명시한다.
- 컬럼명 대신 컬럼 순서, 별칭도 가능
- 기본 디폴트는 오름차순
    - ASC : 오름차순 ( A->Z, ㄱ->ㅎ, 1-10)
    - DESC : 내림차순 ( Z->A, ㅎ->ㄱ, 10-1)
- NULL값은 오름차순할 때 가장 마지막에, 즉, 내림차순에선 가장 위에 정렬된다.

<br/>

### 예시06
```oracle
-- 사원테이블에서 입사일 순으로 정렬해서 사원번호, 급여, 입사일자, 부서번호를 출력하자.

SELECT EMPNO, SAL, HIREDATE, DEPTNO
FROM C##SCOTT.EMP
ORDER BY HIREDATE;
```
출력결과
```oracle
EMPNO	SAL	    HIREDATE	DEPTNO
7369	800	    80/12/17	20
7499	1600	81/02/20	30
7521	1250	81/02/22	30
7698	2850	81/04/01	30
7566	2975	81/04/02	20
7782	2450	81/06/01	10
7844	1500	81/09/08	30
7654	1250	81/09/28	30
7900	950	    81/10/03	30
7902	3000	81/10/03	20
7839	5000	81/11/17	10
7934	1300	82/01/23	10
7788	3000	82/10/09	20
7876	1100	83/01/12	20
```
<br/>

### 예시 06-1
```oracle
SELECT EMPNO, SAL, HIREDATE, DEPTNO
FROM C##SCOTT.EMP
ORDER BY 3 DESC;
```
출력결과
```oracle
EMPNO	SAL	HIREDATE	DEPTNO
7876	1100	83/01/12	20
7788	3000	82/10/09	20
7934	1300	82/01/23	10
7839	5000	81/11/17	10
7902	3000	81/10/03	20
7900	950	    81/10/03	30
7654	1250	81/09/28	30
7844	1500	81/09/08	30
7782	2450	81/06/01	10
7566	2975	81/04/02	20
7698	2850	81/04/01	30
7521	1250	81/02/22	30
7499	1600	81/02/20	30
7369	800 	80/12/17	20
```
- 이번에는 내림차순으로 정렬했다.
- HIREDATE가 우리가 나열한 인덱스 중 3번째이다.
- `ORDER BY`뒤에 컬럼명이 아닌 인덱스 번호를 작성해 줄 수도 있다.