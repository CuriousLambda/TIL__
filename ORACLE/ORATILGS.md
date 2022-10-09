# Oracle - GROUPING, GROUPING SETS

## 1. GROUPING
- GROUPING 함수는 ROLLUP과 CUBE를 함께 사용한다.
- SELECT문 뒤에 선언되며 하나의 열을 인수로 갖는다.
  - GROUPING(컬럼명)
- 인수는 GROUP BY 절의 컬럼과 같아야 한다.
- 0 또는 1을 반환한다.
  - 0 : 해당 열을 그대로 사용하여 집계 값을 계산 했거나 해당 열에 나오는 null값이 저장된 것을 의미한다.
  - 1 : 0과 반대, 해당 열을 그대로 사용하지 않고 집계 값을 계산 했거나 null값이 그룹화의 결과로 ROLLUP이나 CUBE에 리턴값으로 구현된 것을 의미
- 즉, ROLLUP이나 CUBE의 결과로 집계된 행은 null로 표시되는데, 이 두 함수의 집계 결과로 null이 나왔을 때 1을 반환한다.
- __행에서 하위 총계를 형성한 그룹을 찾을 수 있다.__

<br/>

### _실습으로 사용한 EMP(사원) 테이블_
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


### 예시01
```oracle
-- 봉급 집계 결과를 ROLLUP, GROUPING을 사용하여 조회해보자.

SELECT DEPTNO, JOB, SUM(SAL), GROUPING(DEPTNO), GROUPING(JOB)
FROM C##SCOTT.EMP
GROUP BY ROLLUP(DEPTNO, JOB);
```
출력결과
```oracle
 DEPTNO JOB         SUM(SAL)     GROUPING(DEPTNO)        GROUPING(JOB)
---------- --------- ---------- -------------------- --------------------
        10 CLERK           1300                    0                    0
        10 MANAGER         2450                    0                    0
        10 PRESIDENT       5000                    0                    0
        10                 8750                    0                    1 -- ROLLUP(JOB) 집계 행
        20 CLERK           1900                    0                    0
        20 ANALYST         6000                    0                    0
        20 MANAGER         2975                    0                    0
        20                10875                    0                    1 -- ROLLUP(JOB) 집계 행
        30 CLERK            950                    0                    0
        30 MANAGER         2850                    0                    0
        30 SALESMAN        5600                    0                    0
        30                 9400                    0                    1 -- ROLLUP(JOB) 집계 행
                          29025                    1                    1 -- ROLLUP(DEPTNO, JOB) 집계 행
```
- ROLLUP에 의해 집계값이 계산된 행의 GROUPING결과가 1로 나타난 것을 확인할 수 있다.
- 또한 GROUPING 컬럼이 DEPTNO와 JOB이기 떄문에, GROUP BY에도 DEPTNO과 JOB을 이용했다.

<br/>

### 예시02
```oracle
-- 봉급 집계 결과를 CUBE, GROUPING을 사용하여 조회해보자.

SELECT DEPTNO, JOB, SUM(SAL), GROUPING(DEPTNO), GROUPING(JOB)
FROM C##SCOTT.EMP
GROUP BY CUBE(DEPTNO, JOB);
```
출력결과
```oracle
    DEPTNO JOB         SUM(SAL)     GROUPING(DEPTNO)            GROUPING(JOB)
---------- --------- ---------- --------------------- ------------------------
                          29025                     1                        1 -- CUBE(DEPTNO, JOB) 집계 행
           CLERK           4150                     1                        0 -- CUBE(DEPTNO) 집계 행
           ANALYST         6000                     1                        0 -- CUBE(DEPTNO) 집계 행
           MANAGER         8275                     1                        0 -- CUBE(DEPTNO) 집계 행
           SALESMAN        5600                     1                        0 -- CUBE(DEPTNO) 집계 행
           PRESIDENT       5000                     1                        0 -- CUBE(DEPTNO) 집계 행
        10                 8750                     0                        1 -- CUBE(JOB) 집계 행
        10 CLERK           1300                     0                        0
        10 MANAGER         2450                     0                        0
        10 PRESIDENT       5000                     0                        0
        20                10875                     0                        1 -- CUBE(JOB) 집계 행
        20 CLERK           1900                     0                        0
        20 ANALYST         6000                     0                        0
        20 MANAGER         2975                     0                        0
        30                 9400                     0                        1 -- CUBE(JOB) 집계 행
        30 CLERK            950                     0                        0
        30 MANAGER         2850                     0                        0
        30 SALESMAN        5600                     0                        0
```
- 마찬가지로 집계를 담당하는 부분은 1로 표시된 것을 확인할 수 있다.
- CUBE는 교차집계이기 때문에 ROLLUP보다 집계된 부분이 많다.

<br/>

## 2. GROUPING SETS
- GROUP BY 뒤에 선언되는 함수, 여러개를 그룹화 할 수 있다.
- 각 그룹 조건에 대해 별도로 GROUP BY한 결과를 UNION ALL한 결과와 동일하다.

<br/>

### 예제03 - GROUPING SETS
```oracle
-- GROUPING SETS를 사용하여 부서번호+직업 별, 부서번호+매니저별 봉급의 집계를 조회해보자.

SELECT DEPTNO, JOB, MGR, SUM(SAL) 
FROM C##SCOTT.EMP 
GROUP BY GROUPING SETS((DEPTNO, JOB), (DEPTNO, MGR));
```
출력결과
```oracle
    DEPTNO JOB              MGR   SUM(SAL)
---------- --------- ---------- ----------
        20                 7839       2975
        10                 7839       2450
        30                 7698       6550
        20                 7566       6000
        10                 7782       1300
        20                 7902        800
        10                            5000
        30                 7839       2850
        20                 7788       1100 -- 여기까지는 (DEPTNO, MGR)로 집계
        20 CLERK                      1900
        30 SALESMAN                   5600
        20 MANAGER                    2975
        30 CLERK                       950
        10 PRESIDENT                  5000
        30 MANAGER                    2850
        10 CLERK                      1300
        10 MANAGER                    2450
        20 ANALYST                    6000 -- 여기까지는 (DEPTNO, JOB)로 집계
```

<br/>

- 그렇다면 UNION ALL은 어떨까?
### 예제04 - UNION ALL
```oracle
-- UNION ALL을 사용하여 부서번호+직업 별, 부서번호+매니저별 봉급의 집계를 조회해보자.

SELECT DEPTNO, JOB, NULL AS MGR, SUM(SAL)
FROM C##SCOTT.EMP 
GROUP BY DEPTNO, JOB
UNION ALL 
SELECT DEPTNO, NULL AS JOB, MGR, SUM(SAL) 
FROM C##SCOTT.EMP 
GROUP BY DEPTNO, MGR; 
```
출력결과
```oracle
    DEPTNO JOB              MGR   SUM(SAL)
---------- --------- ---------- ----------
        20 CLERK                      1900
        30 SALESMAN                   5600
        20 MANAGER                    2975
        30 CLERK                       950
        10 PRESIDENT                  5000
        30 MANAGER                    2850
        10 CLERK                      1300
        10 MANAGER                    2450
        20 ANALYST                    6000 -- 여기까지 DEPTNO와 JOB을 그룹으로 집계하기 때문에 MGR이 NULL
        20                 7839       2975
        10                 7839       2450
        30                 7698       6550
        20                 7566       6000
        10                 7782       1300
        20                 7902        800
        10                            5000
        30                 7839       2850
        20                 7788       1100 -- 여기까지 DEPTNO와 MGR을 그룹으로 집계하기 때문에 JOB이 NULL
```
- 출력결과는 동일한 것을 확인할 수 있다.
- 다만, UNION ALL의 경우, __집계 시 NULL로 쓰이는 컬럼은 반드시 NULL이라고 명시__ 해주어야 SQL문이 정삭 작동된다.
- 또한 같은 결과지만 UNION ALL의 쿼리 문이 훨씬 길다.
- 따라서 GROUPING SETS를 활용함으로써 더 효율적으로 쿼리를 실행시킬 수 있다.