# Oracle - SubQuery(서브쿼리)

## 1. SubQuery
- 하나의 쿼리 문장 내에 포함된 또 하나의 쿼리 문장
- ( )로 묶어서 사용된다.
- 비교조건의 오른쪽에 선언된다.
- 일반적으로 ORDER BY 절은 서브쿼리 안에 사용하지 않는다.
- 서브쿼리의 결과가 단일행, 다중행으로 나뉜다.
  - 단일행 연산자( >, >=, <, <=, ==, != )
  - 다중행 연산자( IN, NOT IN, ANY, ALL ,,,)
- 주쿼리와 서브쿼리로 구현되는 하나의 구문에서 먼저 서브쿼리가 실행이 되고 결과를 통해서 주 쿼리 연산이 실행이 된다.
- SELECT, WHERE, FROM, GROUP BY, ORDER BY, UPDATE, DELETE, INSERT INTO, HAVING 등등 에서 사용된다.
- 서브쿼리를 사용하는 위치에 따라 스칼라 서브쿼리, 인라인 뷰 서브쿼리, 중첩 서브쿼리로 나뉜다.

<br/>

## 2. Scalar SubQuery(스칼라 서브쿼리)
- SELECT절 서브쿼리
- 서브쿼리의 결과는 반드시 단일 행이나 단일 값으로 리턴되어야 한다.
  - 서브쿼리 실행을 끝낸 값 하나를 주 쿼리에서 SELECT하기 때문이다.
- 서브 쿼리가 0개의 행을 리턴하면 스칼라 서브쿼리의 값은 NULL이다.
- 서브 쿼리가 2개 이상의 행을 리턴하면 오류가 리턴된다.

<br/>

### 예시01 - Scalar SubQuery
```oracle
-- 사원번호, 이름, 부서번호, 해당 사원이 속한 부서의 평균 급여를 출력하자.

SELECT EMPNO, ENAME, DEPTNO, SAL,
    ROUND((SELECT AVG(SAL)
    FROM C##SCOTT.EMP
    WHERE DEPTNO = E.DEPTNO)) AS M_SAL
FROM C##SCOTT.EMP E;
```
출력결과
```oracle
     EMPNO ENAME          DEPTNO        SAL      M_SAL
---------- ---------- ---------- ---------- ----------
      7499 ALLEN              30       1600       1567
      7521 WARD               30       1250       1567
      7654 MARTIN             30       1250       1567
      7698 BLAKE              30       2850       1567
      7844 TURNER             30       1500       1567
      7900 JAMES              30        950       1567
      7369 SMITH              20        800       2175
      7566 JONES              20       2975       2175
      7788 SCOTT              20       3000       2175
      7876 ADAMS              20       1100       2175
      7902 FORD               20       3000       2175
      7782 CLARK              10       2450       2917
      7839 KING               10       5000       2917
      7934 MILLER             10       1300       2917
```
- ROUND ~ AS M_SAL까지가 서브쿼리이다.
- 이때, `DEPTNO = E.DEPTNO`와 같이 주 쿼리 테이블의 컬럼을 역참조할 때는 별칭을 사용한다.

<br/>

### ※ 상호 연관(CORRELATIED) 서브쿼리
- 상의 질의, 즉, 주 쿼리에 있는 테이블의 열을 참조하는 것을 말한다.
- 메인 쿼리의 하나의 ROW에서 서브쿼리가 한번씩 실행된다.
- 테이블에서 행을 먼저 읽어서 각 행의 값을 관련된 데이터와 비교한다.
- 주 쿼리에서 각 서브쿼리의 해에 대해 다른 결과를 리턴할 때 사용한다.
- 각 행의 값에 따라 응답이 달라지는 다중 질의의 값을 리턴받을 때 사용한다.
- 서브쿼리에서 메인쿼리의 컬럼명을 사용할 수 있지만 메인에서는 서브쿼리의 컬럼명을 사용할 수 없다.

<br/>

- 따라서 `DEPTNO = E.DEPTNO`에서 현재 행의 부서번호와 동일한 부서번호를 찾아서 그 부서의 평균 급여 값을 리턴한다고 생각할 수 있다.

<br/>

## 3. Inline View SubQuery(인라인 뷰 서브쿼리)
- From 절 서브쿼리
- 서브쿼리의 결과는 반드시 하나의 테이블로 리턴되어야 한다.
    - 서브쿼리 실행을 끝낸 테이블 하나가 주 쿼리의 FROM 에서 테이블이 되기 때문이다.
- 서브쿼리의 결과가 마치 실행 시에 동적으로 생성된 테이블인 것처럼 사용 가능하다.

<br/>

### 예시02 - Inline View SubQuery
```oracle
-- 소속된 부서번호의 평균급여보다 많은 월급을 받는 사원의 이름, 급여, 부서번호, 입사일, 직업을 출력해보자.

SELECT E.ENAME, E.SAL, E.DEPTNO, E.HIREDATE, D.AVGSAL
FROM C##SCOTT.EMP E, (SELECT DEPTNO, ROUND(AVG(SAL),0) AVGSAL FROM C##SCOTT.EMP E GROUP BY DEPTNO) D
WHERE E.DEPTNO = D.DEPTNO AND E.SAL > D.AVGSAL;
```
출력결과
```oracle
ENAME             SAL     DEPTNO HIREDATE     AVGSAL
---------- ---------- ---------- -------- ----------
ALLEN            1600         30 81/02/20       1567
JONES            2975         20 81/04/02       2175
BLAKE            2850         30 81/04/01       1567
SCOTT            3000         20 82/10/09       2175
KING             5000         10 81/11/17       2917
FORD             3000         20 81/10/03       2175
```
- SQL문이 길어서 초조할수 있지만 차근차근 살펴보자.
- `C##SCOTT.EMP E`
  - C##SCOTT에 있는 EMP테이블에 E라는 별칭을 지어줬다.
- `(SELECT DEPTNO, ROUND(AVG(SAL),0) AVGSAL FROM C##SCOTT.EMP E GROUP BY DEPTNO) D`
  - `DEPTNO`[부서번호], `ROUND(AVG(SAL),0)`[평균급여를 일의자리까지 나타낸 값]을 가져오자.
  - `ROUND(AVG(SAL),0) AVGSAL` : 단, `ROUND(AVG(SAL),0)`의 컬럼명은 AVGSAL로 정하자.
  - `FROM C##SCOTT.EMP E` : 이것들을 E라는 별칭을 가진 EMP테이블에서 가져오자.
  - `GROUP BY DEPTNO` : 부서번호로 그룹을 묶어서 가져오자. (집계해서 가져오자.)
  - 마지막 `D` : 가져와진 데이터 = 테이블의 별칭은 D라고 하자.
- `E.DEPTNO = D.DEPTNO` : 원래 테이블의 부서번호와 서브쿼리로 가져온 테이블의 부서번호가 일치하면 데이터를 조회하자.
- `AND` 그리고
- `E.SAL > D.AVGSAL` : 원래 테이블의 급여가 서브쿼리로 가져온 테이블의 평균 급여보다 많은지 비교해서 많다면 가져오자.
- 이런 로직으로 쿼리문이 실행됐고, 그 결과로 소속된 부서의 평균 급여보다 많은 급여를 받는 사원을 조회할 수 있다.

<br/>

## 4. Nested SubQuery(중첩 서브쿼리)
- WHERE절 서브쿼리
- 조건절의 일부로 사용된다.
- 메인쿼리 테이블의 특정 컬럼 값과 비교한 값을 반환하는 용도로 사용
  - 여러 개의 컬럼, 여러 개의 로우를 리턴할 수 있다.

<br/>

### 예시03 - Nested SubQuery
```oracle
-- 업무가 SALESMAN인 사원의 최소급여보다 급여를 많이 받는 사원의 이름, 급여, 직업을 출력하자.

SELECT ENAME, SAL, JOB
FROM C##SCOTT.EMP
WHERE SAL > ANY (SELECT SAL
            FROM C##SCOTT.EMP
            WHERE JOB = 'SALESMAN');
```
출력결과
```oracle
ENAME             SAL JOB     
---------- ---------- ---------
KING             5000 PRESIDENT
FORD             3000 ANALYST  
SCOTT            3000 ANALYST  
JONES            2975 MANAGER  
BLAKE            2850 MANAGER  
CLARK            2450 MANAGER  
ALLEN            1600 SALESMAN 
TURNER           1500 SALESMAN 
MILLER           1300 CLERK    
```
- 밑의 사원테이블을 보면, 직업이 SALESMAN인 사원의 최소 급여는 1250인 것을 확인할 수 있다.
- 최소 급여를 찾기 위해 서브쿼리절에서 직업이 SALESMAN인 사원들의 급여를 가져오라고 했다.
- 그런데, 직업이 SALESMAN인 사원들의 SAL는 총 4개이다.
- 따라서 이 경우 다중행 서브쿼리에 해당한다.

<br/>

### ※ 다중 행 (Multiple-Row) 서브쿼리
- 하나 이상의 행을 리턴 하는 서브쿼리를 다중 행 서브쿼리라고 한다.
- 복수 행 연산자(IN, ANY, ALL)를 사용한다. 
- IN : 목록에 있는 임의의 값과 동일하면 참,  OR연산
- ANY : 서브쿼리에서 리턴된 각각의 값과 비교하여 하나라도 참이면 참 __( =ANY는 IN과 동일)__ , OR연산
    - EX) __< ANY  = 최대값보다 적음__,  _>ANY  최소값보다 큼_
- ALL : 서브쿼리에서 리턴된 모든 값과 비교하여 모두 참이어야 참  AND연산
    - EX) < ALL = 최소값보다 적음   ,   >ALL  최대값 보다 큼
- NOT 연산자는 IN, ANY, ALL 연산자와 함께 사용될 수 있다.

<br/>

- 다중 행 연산자 ANY는 각각의 값과 비교하여 하나라도 참이면 참이다.
- 위 쿼리에서 ANY안에 들어있는 SAL은 (1250, 1250, 1500, 1600)이고,
- `> ANY`(1250, 1250, 1500, 1600) 은 1250보다만 크면 된다는 뜻이 되므로, _급여의 최솟값보다 큰_ 이라는 뜻이된다.

<br/>

<br/>

<br/>

<br/>

<br/>

#### _실습으로 사용한 EMP(사원) 테이블_
```oracle
EMPNO	ENAME	JOB	        MGR	HIREDATE	SAL	COMM	DEPTNO
7369	SMITH	CLERK	        7902	80/12/17	800		20
7499	ALLEN	SALESMAN	7698	81/02/20	1600	300	30
7521	WARD	SALESMAN	7698	81/02/22	1250	200	30
7566	JONES	MANAGER	        7839	81/04/02	2975	30	20
7654	MARTIN	SALESMAN	7698	81/09/28	1250	300	30
7698	BLAKE	MANAGER	        7839	81/04/01	2850		30
7782	CLARK	MANAGER	        7839	81/06/01	2450		10
7788	SCOTT	ANALYST	        7566	82/10/09	3000		20
7839	KING	PRESIDENT		81/11/17	5000	3500	10
7844	TURNER	SALESMAN	7698	81/09/08	1500	0	30
7876	ADAMS	CLERK	        7788	83/01/12	1100		20
7900	JAMES	CLERK	        7698	81/10/03	950		30
7902	FORD	ANALYST	        7566	81/10/03	3000		20
7934	MILLER	CLERK	        7782	82/01/23	1300		10
```