# Oracle - ROLLUP, CUBE

## 1. ROLLUP, CUBE
- ROLLUP과 CUBE는 그룹핑한 결과를 상호 참조열에 따라 상위 집계를 내는 함수이다.

<br/>

- ROLLUP
  - 정규 그룹화 행, 하위 총합을 포함해서 결과를 리턴
  - 데이터 보고서 작성, 집합에서 통계 및 요약정보를 추출하는데 사용
  - GROUP BY 절에 ()를 이용해서 지정된 열 목록을 따라 오른쪽에서 왼쪽 방향으로 하나씩 그룹을 만든다.
  - 그 다음 그룹함수를 생성한 그룹에 적용한다.
  - 총계를 산출하려면 N+1 개의 SELECT문을 UNION ALL로 지정한다.

- CUBE
  - 롤업(ROLLUP) 결과 + 교차 도표화 행을 포함하는 상위 집계 결과 집합을 리턴
  - GROUP BY 확장 기능이다.
  - 집계 함수를 사용하게 되면 결과집합에 추가 행이 만들어진다.
  - GROUP BY 절에 n개의 열이 있을 경우 상위집계 조합 수는 2의 n승 개이다.

<br/>

- ROLLUP은 하위 총합의 조합 중에 일부를 합을 내지만 CUBE는 모든 그룹의 합과 총계를 나타낸다.

<br/>

---------------

#### 사원테이블
```
EMPNO	ENAME	JOB	MGR	HIREDATE	SAL	COMM	DEPTNO
7369	SMITH	CLERK	7902	80/12/17	800		20
7499	ALLEN	SALESMAN	7698	81/02/20	1600	300	30
7521	WARD	SALESMAN	7698	81/02/22	1250	200	30
7566	JONES	MANAGER	7839	81/04/02	2975	30	20
7654	MARTIN	SALESMAN	7698	81/09/28	1250	300	30
7698	BLAKE	MANAGER	7839	81/04/01	2850		30
7782	CLARK	MANAGER	7839	81/06/01	2450		10
7788	SCOTT	ANALYST	7566	82/10/09	3000		20
7839	KING	PRESIDENT		81/11/17	5000	3500	10
7844	TURNER	SALESMAN	7698	81/09/08	1500	0	30
7876	ADAMS	CLERK	7788	83/01/12	1100		20
7900	JAMES	CLERK	7698	81/10/03	950		30
7902	FORD	ANALYST	7566	81/10/03	3000		20
7934	MILLER	CLERK	7782	82/01/23	1300		10
```

-------------------------------

<br/>

### 예시01
```oracle
-- 사원테이블에서 부서별, 직업별 급여의 합을 조회하되, ROLLUP으로 집계를 내보자.

SELECT DEPTNO, JOB, COUNT(*), SUM(SAL)
FROM C##SCOTT.EMP
GROUP BY ROLLUP(DEPTNO, JOB);
```
출력결과
```oracle
DEPTNO	JOB	COUNT(*)	SUM(SAL)
10	CLERK	1	1300
10	MANAGER	1	2450
10	PRESIDENT	1	5000
10		3	8750
20	CLERK	2	1900
20	ANALYST	2	6000
20	MANAGER	1	2975
20		5	10875
30	CLERK	1	950
30	MANAGER	1	2850
30	SALESMAN	4	5600
30		6	9400
		14	29025
```
- 각 부서별 총계가 각 부서 당 가장 마지막 행으로 추가된 모습을 확인할 수 있다. __(하위 집계)__
- 스크립트 실행으로 SQL을 실행시키면 보고서 형식으로 볼 수도 있다.
```oracle
    DEPTNO JOB         COUNT(*)   SUM(SAL)
---------- --------- ---------- ----------
        10 CLERK              1       1300
        10 MANAGER            1       2450
        10 PRESIDENT          1       5000
        10                    3       8750      -- 집계 행
        20 CLERK              2       1900
        20 ANALYST            2       6000
        20 MANAGER            1       2975
        20                    5      10875      -- 집계 행
        30 CLERK              1        950
        30 MANAGER            1       2850
        30 SALESMAN           4       5600
        30                    6       9400      -- 집계 행
                             14      29025      -- 전체집계 행
```
- 이후 예시부터는 한눈에 보기 쉬운 보고서 형식으로 결과를 보여주고자 한다.

<br/>

### 예시02
```oracle
-- 위의 예시에 MGR을 추가해서 조회해보자.

SELECT DEPTNO, JOB, MGR, SUM(SAL)
FROM C##SCOTT.EMP
GROUP BY ROLLUP(DEPTNO, JOB, MGR);
```
출력결과
```oracle
    DEPTNO JOB              MGR   SUM(SAL)
---------- --------- ---------- ----------
        10 CLERK           7782       1300
        10 CLERK                      1300      -- 10 / CLERK 집계 행
        10 MANAGER         7839       2450
        10 MANAGER                    2450      -- 10 / MANAGER 집계 행
        10 PRESIDENT                  5000
        10 PRESIDENT                  5000      -- 10 / PRESIDENT 집계 행
        10                            8750      -- 10 전체집계 행
        20 CLERK           7788       1100
        20 CLERK           7902        800
        20 CLERK                      1900      -- 20 / CLERK 집계 행
        20 ANALYST         7566       6000
        20 ANALYST                    6000      -- 20 / ANALYST 집계 행
        20 MANAGER         7839       2975
        20 MANAGER                    2975      -- 20 / MANAGER 집계 행
        20                           10875      -- 20 전체집계 행
        30 CLERK           7698        950
        30 CLERK                       950      -- 30 / CLERK 집계 행
        30 MANAGER         7839       2850
        30 MANAGER                    2850      -- 30 / MANAGER 집계 행
        30 SALESMAN        7698       5600
        30 SALESMAN                   5600      -- 30 / SALESMAN 집계 행
        30                            9400      -- 30 전체집계 행

    DEPTNO JOB              MGR   SUM(SAL)
---------- --------- ---------- ----------
                                     29025
```
- 이때는 부서번호(DEPTNO) 안에서도 직업(JOB)의 하위 총계를 집계한 것을 확인할 수 있다.
- 그 후 각 부서번호별 집계 행이 부서번호 당 가장 하위에 만들어진 것을 확인할 수 있다.

<br/>

### 예시03
```oracle
-- 사원테이블에서 부서별, 직업별 급여의 합 조회시 CUBE집계를 내보자

SELECT DEPTNO, JOB, COUNT(*), SUM(SAL)
FROM C##SCOTT.EMP
GROUP BY CUBE(DEPTNO, JOB);
```
출력결과
```oracle
   DEPTNO JOB         COUNT(*)   SUM(SAL)
---------- --------- ---------- ----------
                             14      29025
           CLERK              4       4150
           ANALYST            2       6000
           MANAGER            3       8275
           SALESMAN           4       5600
           PRESIDENT          1       5000
        10                    3       8750
        10 CLERK              1       1300
        10 MANAGER            1       2450
        10 PRESIDENT          1       5000
        20                    5      10875
        20 CLERK              2       1900
        20 ANALYST            2       6000
        20 MANAGER            1       2975
        30                    6       9400
        30 CLERK              1        950
        30 MANAGER            1       2850
        30 SALESMAN           4       5600
```
- 가장 먼저 ROLLUP과 구분되는 차이점은 __집계가 상위__ 에 조회된다는 것이다.
- ROLLUP의 같은 조회문의 경우, DEPTNO(부서번호)당 집계만 포함됐지만
- CUBE의 경우 __교차 집계__ 하기 때문에 구분되는 각 직업의 집계도 조회된 것을 확인할 수 있다.

<br/>

### 예시04
```oracle
SELECT DEPTNO, JOB, MGR, SUM(SAL)
FROM C##SCOTT.EMP
GROUP BY CUBE(DEPTNO, JOB, MGR);
```
출력결과
```oracle
    DEPTNO JOB              MGR   SUM(SAL)
---------- --------- ---------- ----------
                                      5000
                                     29025      -- 전체집계
                           7566       6000      -- MGR = 7566 집계
                           7698       6550      -- MGR = 7698 집계
                           7782       1300      -- MGR = 7782 집계
                           7788       1100      -- MGR = 7788 집계
                           7839       8275      -- MGR = 7839 집계
                           7902        800      -- MGR = 7902 집계
           CLERK                      4150      -- CELRK 집계
           CLERK           7698        950
           CLERK           7782       1300
           CLERK           7788       1100
           CLERK           7902        800
           ANALYST                    6000      -- ANALYST 집계
           ANALYST         7566       6000
           MANAGER                    8275      -- MANAGER 집계
           MANAGER         7839       8275
           SALESMAN                   5600      -- SALESMAN 집계
           SALESMAN        7698       5600
           PRESIDENT                  5000      -- PRESIDENT 집계
           PRESIDENT                  5000
        10                            5000      -- 10 /MGR = null 집계
        10                            8750      -- 10 집계
        10                 7782       1300      -- 10 / MGR = 7782 집계
        10                 7839       2450      -- 10 / MGR = 7839 집계
        10 CLERK                      1300      -- 10 / CLERK 집계
        10 CLERK           7782       1300
        10 MANAGER                    2450      -- 10 / MANAGER 집계
        10 MANAGER         7839       2450
        10 PRESIDENT                  5000      -- 10 / PRESIDENT 집계
        10 PRESIDENT                  5000
        20                           10875      -- 20 집계
        20                 7566       6000      -- 20 / MGR = 7566 집계
        20                 7788       1100      -- 20 / MGR = 7788 집계
        20                 7839       2975      -- 20 / MGR = 7839 집계
        20                 7902        800      -- 20 / MGR = 7902 집계
        20 CLERK                      1900      -- 20 / CLERK 집계
        20 CLERK           7788       1100
        20 CLERK           7902        800
        20 ANALYST                    6000      -- 20 / ANALYST 집계
        20 ANALYST         7566       6000
        20 MANAGER                    2975      -- 20 / MANAGER 집계
        20 MANAGER         7839       2975
        30                            9400      -- 30 집계
        30                 7698       6550      -- 30 / MGR = 7698 집계
        30                 7839       2850      -- 30 / MGR = 7839 집계
        30 CLERK                       950      -- 30 / CLERK 집계
        30 CLERK           7698        950
        30 MANAGER                    2850      -- 30 / MANAGER 집계
        30 MANAGER         7839       2850
        30 SALESMAN                   5600      -- 30 / SALESMAN 집계
        30 SALESMAN        7698       5600
```
- 교차 집계를 내기 때문에 확실히 ROLLUP에 비해 더 많은 집계 행이 생성된다.