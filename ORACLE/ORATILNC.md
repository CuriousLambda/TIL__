# Oracle - NULL, DECODE, CASE-WHEN


## 1. NULL관련 함수
- NULLIF(EXPR01, EXPR02)
  - EXPR01 == EXPR02이면 NULL을 반환, 아니면 본래 컬럼 값을 반환
- NVL(컬럼, 변환값)
  - 해당 컬럼의 값 중 NULL값을 변환값으로 반환
- NVL2(컬럼, NULL이 아닌 경우의 반환값01, NULL인경우의 반환값02)
  - 컬럼의 값이 NULL이 아닌 경우 반환값01을 반환하고, NULL인 경우 반환값02를 반환한다.
- COALESCE(EXPR01, EXPR02, EXPR03)
  - 인자가 정해져 있지 않다.
  - 원하는대로 인자를 넣을 수 있다.
  - 입력받은 값 중에서 null이 아닌 첫 번째 표현식을 반환

### 예시01 - NULLIF
```oracle
-- EMP 테이블의 사원이름 , 업무, 업무가 'CLERK‘ 인 경우 NULL로 나오도록 출력해보자.

SELECT  ENAME, JOB, NULLIF(JOB,'CLERK') AS RESULT 
FROM  C##SCOTT.EMP;
```
출력결과
```oracle
ENAME	JOB	RESULT
SMITH	CLERK	
ALLEN	SALESMAN	SALESMAN
WARD	SALESMAN	SALESMAN
JONES	MANAGER	MANAGER
MARTIN	SALESMAN	SALESMAN
BLAKE	MANAGER	MANAGER
CLARK	MANAGER	MANAGER
SCOTT	ANALYST	ANALYST
KING	PRESIDENT	PRESIDENT
TURNER	SALESMAN	SALESMAN
ADAMS	CLERK	
JAMES	CLERK	
FORD	ANALYST	ANALYST
MILLER	CLERK	
```
- JOB이 CLERK인 사원들의 NULLIF결과가 null로 나온것을 확인할 수 있다.

<br/>

### 예시02 - NVL2
```oracle
 --EMP 테이블의 사원이름, 매니저 번호, 매니저번호가 null이면 ‘대표’ 로 표시하고, 매니저번호가 있으면 MGR'프로'로 조회해보자.

 SELECT ENAME, MGR, NVL2(MGR, MGR||'프로','대표') 
 FROM C##SCOTT.EMP;
 ```
 출력결과
 ```oracle
 ENAME	MGR	NVL2(MGR,MGR||'프로','대표')
SMITH	7902	7902프로
ALLEN	7698	7698프로
WARD	7698	7698프로
JONES	7839	7839프로
MARTIN	7698	7698프로
BLAKE	7839	7839프로
CLARK	7839	7839프로
SCOTT	7566	7566프로
KING		대표
TURNER	7698	7698프로
ADAMS	7788	7788프로
JAMES	7698	7698프로
FORD	7566	7566프로
MILLER	7782	7782프로
```
- NVL2(MGR, MGR||'프로', '대표')에서, 연결 연산자 `||`를 사용하여 컬럼 값 뒤에 '프로'라는 문자열을 붙여주었다.

<br/>

### 예시03 - COALESCE
```oracle
-- EMP테이블에서 이름, 보너스,봉급과,
-- 보너스가 null 아닌 경우 보너스를, 보너스가 null인 경우엔 봉급을,
-- 모두 null인 경우엔 50으로 리턴하는 SQL문을 작성해보자.

SELECT ENAME, COMM, SAL, COALESCE(COMM, SAL, 50) RESULT 
FROM C##SCOTT.EMP;
```
출력결과
```oracle
ENAME	COMM	SAL	RESULT
SMITH		800	800
ALLEN	300	1600	300
WARD	200	1250	200
JONES	30	2975	30
MARTIN	300	1250	300
BLAKE		2850	2850
CLARK		2450	2450
SCOTT		3000	3000
KING	3500	5000	3500
TURNER	0	1500	0
ADAMS		1100	1100
JAMES		950	950
FORD		3000	3000
MILLER		1300	1300
```
- COALESCE는 작성한 표현식들 중, NULL이 아닌 가장 첫번째 값을 반환한다.
- 만약 COMM(보너스)이 NULL이 아니라면, COMM이 가장 첫번째 표현식이므로, COMM이 조회된다.
- COMM이 NULL이라면, 다음 표현식인 SAL로 넘어가서, SAL이 NULL이 아니라면 이떄는 SAL이 조회된다.
- COMM과 SAL이 모두 NULL이라면 가장 마지막 표현식인 50이 반환될 것이다.

<br/>

## 2. CASE-WHEN, DECODE
- CASE WHEN
- 형식
```oracle
CASE WHEN 조건문01 THEN 반환값01
     WHEN 조건문02 THEN 반환값02
     ELSE 반환값03
     END;
```
- WHEN의 갯수는 제한되어 있지 않다.

- DECODE(EXPR, IF01, THEN01, IF02, THEN02,,,,)
  - EXPR이 IF01을 만족한다면, THEN01을 반환하고, EXPR이 IF02를 만족한다면 THEN02를 반환한다.
  - CASE WHEN문을 한줄로 작성한 것과 비슷하다.
  - 마지막에 IF를 작성하지 않고 반환값만 제시한다면, ELSE인 경우로 간주한다.

- WHEN은 조건문을 작성할 수 있으므로 비교적 더 자세하게 조건을 작성할 수 있다.
- DECODE는 IF에 있는 값들이 같은지/다른지 만 비교하여 반환값을 반환한다.
- WHEN은 PL/SQL에서도 사용 가능하지만 DECODE는 SQL에서만 사용 가능하다.

<br/>

### 예시04 - DECODE
```oracle
-- 급여가 1000보다 작으면 ‘A’, 1000이상 2500미만이면 ‘B’, 2500이상이면 ‘C’로 표시하고, 사원명, 봉급을 조회해보자.

SELECT  ENAME, SAL, DECODE(SIGN(SAL-1000), -1, 'A', DECODE(SIGN(SAL-2500), -1, 'B', 'C')) GRADE
FROM  C##SCOTT.EMP;
```
출력결과
```oracle
ENAME	SAL	GRADE
SMITH	800	A
ALLEN	1600	B
WARD	1250	B
JONES	2975	C
MARTIN	1250	B
BLAKE	2850	C
CLARK	2450	B
SCOTT	3000	C
KING	5000	C
TURNER	1500	B
ADAMS	1100	B
JAMES	950	A
FORD	3000	C
MILLER	1300	B
```
- SIGN은 값의 부호를 리턴하는 함수이다. 양수이면 1, 음수이면 -1, 0이면 0을 반환한다.
- 따라서 `SIGN(SAL-1000)` = -1 이라는 것은, 봉금이 1000보다 작다는 뜻이 된다.
- 위와 같은 논리로 SIGN을 이용해 봉급에 따라 'A', 'B', 'C'를 리턴할 수 있다.

<br/>

### 예시05 - CASE WHEN
```oracle
-- 급여가 1000보다 작으면 ‘A’, 1000이상 2500미만이면 ‘B’, 2500이상이면 ‘C’로 표시하고, 사원명, 봉급을 조회해보자.

SELECT ENAME, SAL, 
        CASE WHEN SAL < 1000 THEN 'A' 
             WHEN SAL>=1000 AND SAL<2500 THEN 'B'
             ELSE 'C' END  AS GRADE 
FROM C##SCOTT.EMP ORDER BY GRADE;
```
출력결과
```oracle
ENAME	SAL	GRADE
JAMES	950	A
SMITH	800	A
MARTIN	1250	B
WARD	1250	B
ALLEN	1600	B
MILLER	1300	B
ADAMS	1100	B
TURNER	1500	B
CLARK	2450	B
FORD	3000	C
KING	5000	C
SCOTT	3000	C
JONES	2975	C
BLAKE	2850	C
```
- 위의 DECODE와 같은 조건으로 출력한 것이다.
- DECODE의 경우 IF값에 조건문을 작성할 수 없었지만, CASE WHEN의 경우 작성 가능한 것을 볼 수 있다.
- 따라서 CASE WHEN의 경우 SAL < 1000, SAL > 1000 AND SAL < 2500과 같은 연산자를 사용한 조건문이 들어간 것을 확인할 수 있다.
- 같은 결과값이지만 CASE WHEN문에서는 ORDER BY를 사용하여 GRADE를 기준으로 정렬했다.