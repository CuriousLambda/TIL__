# SubQuery 예제풀이

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

<br/>

### 예제01
1. 'SMITH'보다 월급을 많이 받는 사원들의 이름과 월급을 출력하라.
```
SELECT ENAME, SAL
FROM C##SCOTT.EMP
WHERE SAL >( SELECT SAL
              FROM C##SCOTT.EMP
              WHERE ENAME = 'SMITH');
```
출력결과
```oracle
ENAME             SAL
---------- ----------
ALLEN            1600
WARD             1250
JONES            2975
MARTIN           1250
BLAKE            2850
CLARK            2450
SCOTT            3000
KING             5000
TURNER           1500
ADAMS            1100
JAMES             950
FORD             3000
MILLER           1300
```
- 서브쿼리 절 풀이
  - `SELECT SAL` : 월급을 리턴
  - `FROM C##SCOTT.EMP` : (C##SCOTT계정의) 사원테이블에서
  - `WHERE ENAME = 'SMITH'` : 이름이 SMITH인
  - 사원테이블에서 이름이 SMITH인 사원의 월급을 리턴해라.
- SMITH의 월급을 S월급 이라고 해보자.
- 결국 주 쿼리의 WHERE절은 `WHERE SAL > S월급`이 되는 셈이다.
- 즉, SMITH의 월급보다 더 많은 월급을 받는 행들을 조회하게 된다.

<br/>

### 예제02
  2. 10번 부서의 사원들의 월급과 동일한 월급을 받는 사원들의 이름, 월급, 부서번호를 출력하라.
```oracle
SELECT ENAME, SAL, DEPTNO
FROM C##SCOTT.EMP
WHERE SAL IN (SELECT SAL
              FROM C##SCOTT.EMP
              WHERE DEPTNO = 10);
```
출력결과
```oracle
ENAME             SAL     DEPTNO
---------- ---------- ----------
CLARK            2450         10
KING             5000         10
MILLER           1300         10
```
- 서브쿼리 절 풀이
  - `SELECT SAL` : 월급을 리턴
  - `FROM C##SCOTT.EMP` : 사원테이블에서
  - `WHERE DEPTNO = 10` : 부서번호가 10인
  - 사원테이블에서 부서번호가 10인 사원들의 월급을 리턴해라.
- 이 경우 부서번호가 10인 사원들의 월급은 (2450, 5000, 1300) 세 개이다.
- 따라서 다중 행이 리턴되므로, 다중 행 연산자인 IN을 사용했다.
- IN이므로 OR연산으로, 월급이 2450, 5000, 1300 중 하나라도 일치하면 조회한다.
- 여기서는 2450, 5000, 1300과 일치하는 SAL이 자기 자신뿐이어서 이렇게 조회가 되었다.

<br/>

### 예제03
3. 'BLAKE'와 같은 부서에 있는 사원들의 이름과 고용일을 조회하되 'BLAKE'는 빼고 출력하라.
```oracle
SELECT ENAME, HIREDATE
FROM C##SCOTT.EMP
WHERE DEPTNO = (SELECT DEPTNO
                FROM C##SCOTT.EMP
                WHERE ENAME = 'BLAKE')
AND ENAME != 'BLAKE';
```
출력결과
```oracle
ENAME      HIREDATE
---------- --------
ALLEN      81/02/20
WARD       81/02/22
MARTIN     81/09/28
TURNER     81/09/08
JAMES      81/10/03
```
- 서브쿼리 절 풀이
  - `SELECT DEPTNO` : 부서번호를 리턴
  - `FROM C##SCOTT.EMP` : 사원테이블에서
  - `WHERE ENAME = 'BLAKE'` : 이름이 BLAKE인
  - 이름이 BLAKE인 사원의 부서번호를 리턴해라. ( = B부서번호라고 하자.)
- 그러면 주쿼리 WHERE절은 이렇게 된다.
  - `WHERE DEPTNO = B부서번호 AND ENAME != 'BLAKE'` : 부서번호가 BLAKE의 부서번호와 동일하고 블레이크는 제외된
- 따라서 블레이크와 동일한 부서에 있는 사람들이지만, 블레이크는 제외하고 조회된다.

<br/>

### 예제04
4. 평균급여보다 많은 급여를 받는 사원들의 사원번호, 이름, 월급을 출력하되, 월급이 높은 사람 순으로 출력하라.
```oracle
SELECT EMPNO, ENAME, SAL
FROM C##SCOTT.EMP
WHERE SAL > (SELECT AVG(SAL)
              FROM C##SCOTT.EMP)
ORDER BY SAL DESC;
```
출력결과
```oracle
     EMPNO ENAME             SAL
---------- ---------- ----------
      7839 KING             5000
      7902 FORD             3000
      7788 SCOTT            3000
      7566 JONES            2975
      7698 BLAKE            2850
      7782 CLARK            2450
```
- 서브쿼리 절 풀이
  - `SELECT AVG(SAL)` : 월급의 평균을 리턴
  - `FROM C##SCOTT.EMP` : 사원테이블에서
- 주쿼리 WHERE절은 다음과 같다.
  - `WHERE SAL > AVG(SAL)` : 월급의 평균보다 큰 월급을 리턴해라.
- `ORDER BY SAL DESC` : 월급으로 정렬하면서 내림차순 정렬해라.

<br/>

### 에제05
5. 이름에 'T'를 포함하고 있는 사원들과 같은 부서에서 근무하고 있는 사원의 사원번호와 이름을 출력하라.
```oracle
SELECT EMPNO, ENAME
FROM C##SCOTT.EMP
WHERE DEPTNO IN (SELECT DEPTNO
              FROM C##SCOTT.EMP
              WHERE ENAME LIKE '%T%');
```
출력결과
```oracle
     EMPNO ENAME    
---------- ----------
      7369 SMITH     
      7566 JONES     
      7788 SCOTT     
      7876 ADAMS     
      7902 FORD      
      7499 ALLEN     
      7521 WARD      
      7654 MARTIN    
      7698 BLAKE     
      7844 TURNER    
      7900 JAMES     
```
- 서브쿼리 절 풀이
  - `SELECT DEPTNO` : 부서번호를 리턴
  - `FROM C##SCOTT.EMP` : 사원테이블에서
  - `WHERE ENAME LIKE '%T%'` : 사원이름에 T가 포함된
  - 사원이름에 T가 포함된 사원의 부서번호를 리턴해라.
  - 마찬가지로 여러 행이 리턴되므로 다중행 서브쿼리이며, IN연산자를 사용했다.
- 주쿼리 WHERE절은 사원이름에 T가 포함된 사원들의 부서번호와 하나라도 일치하는 부서번호가 있다면 리턴한다.

<br/>

### 예제06
6. 자신의 급여가 평균급여보다 많고,이름에 S자가 들어가는 사원과 동일한 부서에서 근무하는 모든 사원의 사원번호,이름 및 급여를 출력하라.
```oracle
SELECT EMPNO, ENAME, SAL
FROM C##SCOTT.EMP
WHERE SAL > ( SELECT AVG(SAL)
              FROM C##SCOTT.EMP)
      AND
      DEPTNO IN (SELECT DEPTNO
      FROM C##SCOTT.EMP
      WHERE ENAME LIKE '%S%');
```
- 서브쿼리 절 풀이 - 1
  - `SELECT AVG(SAL)` : 월급의 평균을 리턴
  - `FROM C##SCOTT.EMP` : 사원테이블에서
- 서브쿼리 절 풀이 - 2
  - `SELECT DEPTNO` : 부서번호를 리턴
  - `FROM C##SCOTT.EMP` : 사원테이블에서
  - `WHERE ENAME LIKE '%S%'` : 사원이름에 S가 들어가는
- 주쿼리 WHERE절을 확인해보자.
  - `WHERE SAL > AVG(SAL) AND DEPTNO IN (사원이름에 S가 들어가는 사원들의 부서번호들)` 이런 뜻이 된다.
- 따라서 자신의 월급이 평균월급보다 많고,이름에 S자가 들어가는 사원과 동일한 부서에서 근무하는 모든 사원들을 조회할 수 있다.

<br/>

### 예시07
7. 30번 부서에 있는 사원들 중에서 가장 많은 월급을 받는 사원보다 많은 월급을 받는 사원들의 이름, 부서번호, 월급을 출력하라.<br/>
(단, ALL 또는 ANY 연산자를 사용할 것)
```oracle
해답 1)

SELECT ENAME, DEPTNO, SAL
FROM C##SCOTT.EMP
WHERE SAL >ALL (SELECT SAL
              FROM C##SCOTT.EMP
              WHERE DEPTNO = 30);
```
```oracle
해답 2)

SELECT ENAME, DEPTNO, SAL
FROM C##SCOTT.EMP
WHERE SAL > ANY (SELECT MAX(SAL)
              FROM C##SCOTT.EMP
              WHERE DEPTNO = 30);
```
출력결과
```oracle
ENAME          DEPTNO        SAL
---------- ---------- ----------
JONES              20       2975
SCOTT              20       3000
KING               10       5000
FORD               20       3000
```
- 서브쿼리 절 풀이 - ALL
  - `SELECT SAL` : 월급을 리턴
  - `FROM C##SCOTT.EMP` : 사원테이블에서
  - `WHERE DEPTNO = 30` : 부서번호가 30인
  - `ALL (SELECT SAL FROM C##SCOTT.EMP WHERE DEPTNO = 30)` : 부서번호가 30인 모든 월급들
- 주쿼리 WHERE절을 살펴보면
  - WHERE SAL > ALL(서브쿼리) : 부서번호가 30인 모든 월급들 보다 큰 SAL
  - 부서번호가 30인 모든 월급들을 통틀어서 그것보다도 SAL이 큰 경우를 말한다.
- 따라서 가장 많은 월급을 받는 사원보다 더 많은 월급을 받는 조건이 된다.
- 서브쿼리 절 풀이 ANY
  - `SELECT MAX(SAL)` : 최대 월급을 리턴
  - `FROM C##SCOTT.EMP` : 사원테이블에서
  - `WHERE DEPTNO = 30` : 부서번호가 30인
  - `ANY (SELECT MAX(SAL) FROM C##SCOTT.EMP WHERE DEPTNO = 30)` : 부서번호가 30인 월급들 중 최대 월급
- 주쿼리 WHERE절을 살펴보면
- WHERE SAL > ANY(서브쿼리) : 부서번호가 30인 최대 월급들 중 하나라도 일치하는 SAL
- 만약 두 사람 이상이 최대 월급을 받는다면 최대 월급으로 리턴되는 행은 두 개 이상이다.
- `WHERE SAL > ANY (SELECT MAX(SAL) FROM C##SCOTT.EMP WHERE DEPTNO = 30)` : 부서번호가 30인 최대 월급들보다 더 많은 월급
- 따라서 가장 많은 월급을 받는 사원보다 더 많은 월급을 받는 조건이 된다.