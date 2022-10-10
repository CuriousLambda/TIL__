# Oracle - 분석함수, PARTITION BY

## 분석함수
- MAX, MIN, COUNT, LAG, LEAD, RANK, RATIO_TO_REPORT, ROW_NUMBER, SUM, AVG 등
- ARGS : 0 ~ 3개 까지만 줄 수 있다.
- 테이블에서 몇줄에서 몇줄가지 그룹핑 해서 정렬한 다음 분석함수로 리턴할 건지를 결정하는 함수
  - 테이블 -> 선택 행 -> 그룹핑 -> 정렬 -> 집계 리턴
```oracle
[형식] 

SELECT 컬럼명, 컬럼명,,,,,
    분석함수 (ARGS[아규먼트]) OVER (
                                      [PARTITION BY] 쿼리 결과를 그룹으로 묶는다.
                                      [ORDER BY] 각 그룹의 정렬 _행의 겁색 순서_ 옵션_ ASC/DESC/NULL/FIRST/LAST
                                                 EX) DESC NULL FIRST | ASC NULL LAST
                                      [WINDOWING 절] ROWS | RANGE [BETWEEN AND]
                                  )
FROM 테이블명;
```
<br/>

#### 실습을 위한 EMP(사원) 테이블
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

### 예시01 - MAX
```oracle
-- 사원번호, 사원명, 직업, 봉급, 최대봉급을 조회하되,
-- 각 사원의 직업별 봉급이 어떤 카테고리에 속해 있는지 확인할 수 있도록 조회해보자.

SELECT EMPNO, ENAME, JOB, SAL,
MAX(SAL) OVER(PARTITION BY JOB)
FROM C##SCOTT.EMP
WHERE JOB IN ('MANAGER', 'SALESMAN')
ORDER BY JOB;
```
출력결과
```oracle
     EMPNO ENAME      JOB              SAL            MAX(SAL)OVER(PARTITIONBYJOB)
---------- ---------- --------- ---------- ---------------------------------------
      7782 CLARK      MANAGER         2450                                    2975
      7698 BLAKE      MANAGER         2850                                    2975
      7566 JONES      MANAGER         2975                                    2975
      7844 TURNER     SALESMAN        1500                                    1600
      7521 WARD       SALESMAN        1250                                    1600
      7499 ALLEN      SALESMAN        1600                                    1600
      7654 MARTIN     SALESMAN        1250                                    1600
```
- 이렇게 PARTITION BY를 사용하면 직업별 봉급 최댓값을 각 직업 행에 출력해준다.

<br/>

### 예시02 - ROW_NUMBER
```oracle
-- 사원번호, 사원명, 직업, 봉급을 출력하되,
-- 직업별 봉급이 낮은 순서대로 순위를 확인할 수 있도록 조회해보자.

SELECT EMPNO, ENAME, JOB, SAL,
ROW_NUMBER() OVER(PARTITION BY JOB ORDER BY SAL) "행번호"
FROM C##SCOTT.EMP
WHERE JOB IN ('MANAGER', 'SALESMAN')
ORDER BY JOB;
```
출력결과
```oracle
     EMPNO ENAME      JOB              SAL        행번호
---------- ---------- --------- ---------- ----------
      7782 CLARK      MANAGER         2450          1
      7698 BLAKE      MANAGER         2850          2
      7566 JONES      MANAGER         2975          3
      7521 WARD       SALESMAN        1250          1
      7654 MARTIN     SALESMAN        1250          2
      7844 TURNER     SALESMAN        1500          3
      7499 ALLEN      SALESMAN        1600          4
```
- SQL문 두번째 줄에서, `PRATITION BY JOB ORDER BY SAL` 로 인해서
- 각 직업별 봉급이 낮은 순서대로 행번호를 붙인다.

<br/>

### 예시03 - RANK
```oracle
-- 사원번호, 사원의 이름, 부서번호, 봉급, 부서별로 급여가 많은 사원부터 순위를 출력하자.

SELECT EMPNO, ENAME, DEPTNO, SAL,
RANK() OVER (PARTITION BY DEPTNO ORDER BY SAL DESC) "순  위"
FROM C##SCOTT.EMP;
```
출력결과
```oracle
     EMPNO ENAME          DEPTNO        SAL       순  위
---------- ---------- ---------- ---------- ----------
      7839 KING               10       5000          1
      7782 CLARK              10       2450          2
      7934 MILLER             10       1300          3
      7788 SCOTT              20       3000          1 -- 부서번호 20 내에서 봉급이 같음
      7902 FORD               20       3000          1 -- 부서번호 20 내에서 봉급이 같음
      7566 JONES              20       2975          3 -- 다음 순위는 1등이 2명이므로, 3등으로 책정됨
      7876 ADAMS              20       1100          4
      7369 SMITH              20        800          5
      7698 BLAKE              30       2850          1
      7499 ALLEN              30       1600          2
      7844 TURNER             30       1500          3
      7654 MARTIN             30       1250          4
      7521 WARD               30       1250          4
      7900 JAMES              30        950          6
```
- DESC 옵션을 주어, 파티션 내에서 봉급을 내림차순으로 정렬했다.
- `RANK`의 경우 동일 봉급일 때, 같은 순위를 부여하고, 그 다음 순위는 *__순위 + N__* 의 순위가 부여된다.
  - 즉, 부서번호 10인 사원들 중, 봉급이 7000으로 동일한 5명이 있다면 다섯명은 모두 동일 순위(EX. 3)를 부여받고
  - 다음 순위는 3 + 5인 8번이 된다.

<br/>

- 또 다른 순위 분석함수인 DENSE_RANK와 비교해보자.
### 예시04 - DENSE_RANK
```oracle
-- 사원번호, 사원의 이름, 부서번호, 봉급, 부서별로 급여가 많은 사원부터 순위를 출력하자.

SELECT EMPNO, ENAME, DEPTNO, SAL,
DENSE_RANK() OVER (PARTITION BY DEPTNO ORDER BY SAL DESC) "순  위"
FROM C##SCOTT.EMP;
```
출력결과
```oracle
     EMPNO ENAME          DEPTNO        SAL       순  위
---------- ---------- ---------- ---------- ----------
      7839 KING               10       5000          1
      7782 CLARK              10       2450          2
      7934 MILLER             10       1300          3
      7788 SCOTT              20       3000          1 -- 부서번호 20 내에서 봉급이 같음
      7902 FORD               20       3000          1 -- 부서번호 20 내에서 봉급이 같음
      7566 JONES              20       2975          2 -- 다음 순위는 무조건 한단계 다음 순위인 2번으로 책정됨
      7876 ADAMS              20       1100          3
      7369 SMITH              20        800          4
      7698 BLAKE              30       2850          1
      7499 ALLEN              30       1600          2
      7844 TURNER             30       1500          3
      7654 MARTIN             30       1250          4
      7521 WARD               30       1250          4
      7900 JAMES              30        950          5
```
- 예시03과 같이, DESC옵션을 주어 파티션 내에서 봉급을 내림차순으로 정렬했다.
- `DENSE-RANK`의 경우 동일 봉급일 때, 동일 순위를 부여하고 그 다음 순위는 *__순위 + 1__* 의 순위가 부여된다.
  - 즉, 부서번호 10인 사원들 중, 봉급이 7000으로 동일한 5명이 있다면 다섯명은 모두 동일 순위(EX. 3)를 부여받고
  - 다음 순위는 3 + 1인 4번이 된다.
