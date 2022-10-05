# Oracle - GROUP BY, 문자열 관련 함수

## 1. GROUP BY
### 형식
```oracle
SELECT 컬럼명
FROM 테이블명
WHERE 조건문
GROUP BY 컬럼명
HAVING 조건문
ORDER BY 컬럼명/인덱스 번호;
```
- GROUP BY는 그룹함수, 즉, 집계함수이다.
- 오라클에서 GROUP BY를 이용하여 그룹별 건수나 합계를 얻을 수 있다.
- GROUP BY에 조건이 필요한 경우에는 HAVING을 써야한다.
  - WHERE절은 집계함수 이전에서 필터링 작업을 하고, HAVING절은 집계함수 이후에서 필터링 작업을 한다.
  - 즉, GROUP BY로 그룹이 형성되고 그룹함수가 계산되면, 그 이후 HAVING절 필터링이 발생한다.
- HAVING 함수를 사용해서 집계함수 결과로 그룹을 제한한다.

<br/>

### <참고> - SQL문 실행 순서
```oracle
FROM -> JOIN을 통해서 테이블을 생성
WHERE -> 하나의 ROW씩 읽어서 조건을 만족하는 결과를 추출한다.
GROUP BY -> 원하는 행들을 그룹핑한다.
HAVING -> 조건을 만족하는 그룹을 남긴다/리턴한다.
ORDER BY -> 조건에 따라 정렬한다.
SELECT -> 원하는 결과만 출력/PROJECTION한다.
```

<br/>

### 예시01
```oracle
-- 사원테이블에서 부서별 봉급의 가장큰값, 작은값, 중간값, 평균, 합계를 구해보자.

    SELECT DEPTNO, MAX(SAL), MIN(SAL), MEDIAN(SAL), ROUND(AVG(SAL),-1), SUM(SAL)
    FROM C##SCOTT.EMP
    GROUP BY DEPTNO;
```
출력결과
```oracle
DEPTNO	MAX(SAL)	MIN(SAL)	MEDIAN(SAL)	ROUND(AVG(SAL),-1)	SUM(SAL)
10	5000	        1300	        2450	    2920	                8750
20	3000	        800	        2987.5	    2310	                13875
30	2850	        950	        1375	    1570	                9400
```
- GRORP BY로 인해 부서번호(DEPTNO)로 묶인 것을 볼 수 있다.

<br/>

### 예시02
```oracle
-- 각 부서별로 봉급으로, 가장큰값, 작은값, 중앙값, 평균, 합계를 구해보자.
-- 단, 급여의 합이 많은 순으로 정렬을 하자.

    SELECT DEPTNO, MAX(SAL), MIN(SAL), MEDIAN(SAL), ROUND(AVG(SAL),-1), SUM(SAL)
    FROM C##SCOTT.EMP
    GROUP BY DEPTNO
    ORDER BY SUM(SAL) DESC;
```
출력결과
```oracle
DEPTNO	MAX(SAL)	MIN(SAL)	MEDIAN(SAL)	ROUND(AVG(SAL),-1)	SUM(SAL)
20	3000	        800	        2987.5	    2310	                13875
30	2850	        950	        1375	    1570	                9400
10	5000	        1300	        2450	    2920	                8750
```
> ROUND(컬럼명 , 숫자) : `소숫점 이하 숫자 자리`만큼 반올림해서 출력해주는 함수
>> EX) 만약 결과값이 1234.5678일때 ROUND( 컬럼명, 2) 였다면, 1234.57로 표시해준다.<br/>
위 예시의 경우 -1이기 때문에 일의 자리에서 반올림하여 십의자리까지 나타내 준 것이다.

<br/>

### 예시03
```oracle
-- 사원테이블에서 급여의 최대가 2900이상인 부서에 대해서 부서번호, 평균, 급여합계를 구하자.

    SELECT DEPTNO, ROUND(AVG(SAL),2), SUM(SAL)
    FROM C##SCOTT.EMP
    GROUP BY DEPTNO
    HAVING MAX(SAL) >= 2900;
```
출력결과
```oracle
DEPTNO	ROUND(AVG(SAL),2)	SUM(SAL)
20	2312.5	13875
10	2916.67	8750
```

<br/>

### 예시04
```oracle
-- 사원테이블에서 부서인원이 4명보다 많은 부서의 부서번호, 인원수, 급여의 합을 조회하자.

    SELECT DEPTNO, COUNT(*), SUM(SAL)
    FROM C##SCOTT.EMP
    GROUP BY DEPTNO
    HAVING COUNT(*)>4;
```
출력결과
```oracle
DEPTNO	COUNT(*)	SUM(SAL)
30	6	9400
20	6	13875
```

<br/>

## 2. 문자열 관련 함수
- LOWER(char) : 문자열을 소문자로 
- UPPER(char) : 문자열을 대문자로 
- INITCAP(char) : 주어진 문자열의 첫 번째 문자를 대문자로 나머지 문자는 소문자로 변환.
- CONCAT(char1, char2) : CONCAT 함수는 Concatenation의 약자로 두 문자를 결합
- SUBSTR(s, m ,[n])
  - 부분 문자열 추출함 . m 번째 자리부터 길이가 n개인 문자열을 반환
  - m이 음수일 경우에는 뒤에서 M번째 문자부터 반대 방향으로 n개의 문자를 반환
- INSTR(s1, s2 , m, n)
  - 문자열 검색, s1의 m번째부터 s2 문자열이 나타나는 n번째 위치 반환
  - 지정한 문자열이 발견되지 않으면 0 이 반환된다

- LENGTH(s) : 문자열의 길이를 리턴  
- CHR(n) : ASCII값이 n에 해당되는 문자를 리턴
- ASCII (s) : 해당 문자의 ASCII값 리턴
- LPAD(s1,n,[s2])
  - 왼쪽의 문자열을 s2를 끼어 놓는 역할,
  - n은 반환되는 문자열의 전체 길이를 나타내며, S1의 문자열이 n보다 클 경우 S1을 n개 문자열 만큼 반환.
- RPAD(s1,n,[s2]) : LPAD와반대로 오른쪽에 문자열을 끼어 놓는 역할
- LTRIM (s ,c) : 문자열 왼쪽 c문자열 제거
- RTRIM (s,c) : 문자열 오른쪽 c문자열 제거
- TRIM
  - 특정 문자 제거
  - 제거할 문자를 입력하지 않으면 기본적으로 공백이 제거 된다.
  - 리턴 값의 데이터타입은 VARCHAR2 이다.
- REPLACE(s,p,r) : s에서 from 문자열의 각 문자를 to문자열의 각 문자로 변환한다.
- TRANSLATE (s,from,to) : s에서 from 문자열의 각 문자를 to문자열의 각 문자로 리턴

<br/>

### 예시05
```oracle
-- EMP 테이블에서 이름의 첫글자가 'K'보고 크고 'Y'보다 작은 사원의 사원번호, 이름, 업무, 급여, 부서번호를 조회하자. 
-- 단, 이름순으로 정렬하자. 

   SELECT ENAME, EMPNO, JOB, SAL, DEPTNO
   FROM C##SCOTT.EMP
   WHERE ENAME BETWEEN 'K' AND 'Y'
   ORDER BY ENAME;
```
```oracle
   SELECT ENAME, EMPNO, JOB, SAL, DEPTNO
   FROM C##SCOTT.EMP
   WHERE SUBSTR(ENAME,1,1)> 'K' AND SUBSTR(ENAME,1,1) <'Y'
   ORDER BY ENAME;
```
출력결과
```
ENAME	EMPNO	JOB	SAL	DEPTNO
MARTIN	7654	SALESMAN	1250	30
MILLER	7934	CLERK	1300	10
SCOTT	7788	ANALYST	3000	20
SMITH	7369	CLERK	800	20
TURNER	7844	SALESMAN	1500	30
WARD	7521	SALESMAN	1250	30
```
- `BETWEEN 작은값 AND 큰값`에서 작은값과 큰값에는 문자가 들어갈 수도 있다.
- 마찬가지로, `__ > 'K' AND < __ 'Y'`와 같이 문자열과 부등호를 사용할 수도 있다.
- 이유는 문자의 코드값을 비교하기 떄문이다.

<br/>

### 예시06
```oracle
-- EMP 테이블에서 10번 부서의 사원들의 담당 업무에서 좌측에 'A'를 삭제하고 급여에서 좌측의 1을 삭제하여 출력하자. 

  SELECT JOB, LTRIM(JOB, 'A'), SAL, LTRIM(SAL, 1)
  FROM C##SCOTT.EMP
  WHERE DEPTNO = 10;
```
출력결과
```oracle
JOB	LTRIM(JOB,'A')	SAL	LTRIM(SAL,1)
MANAGER	MANAGER	2450	2450
PRESIDENT	PRESIDENT	5000	5000
CLERK	CLERK	1300	300
```
<br/>

### 예시07 - LTRIM 비교
```oracle
SELECT LTRIM('ABC12345', 'XABC')
FROM DUAL;
```
출력결과
```oracle
LTRIM('ABC12345','XABC')
12345
```
- LTRIM은 문자열 하나하나를 비교하면서 있으면 지운다. 즉, OR과 같은 논리
- X는 없기때문에 pass, A는 왼쪽에 위치했기 떄문에 지웠고, A가 지워졌기 때문에 이제 가장 왼쪽 문자는 B가 됐다.
- 따라서 B도 지워지고 같은 방법으로 C도 지워졌다.

### 예시 07-1
```oracle
SELECT LTRIM('ABC12345' , 'X12')
FROM DUAL;
```
출력결과
```oracle
LTRIM('ABC12345','X12')
ABC12345
``` 
- X는 없기 떄문에 pass, 마찬가지로 1과 2도 없기 떄문에 아무 문자열도 지우지 못했다.

### 예시 07-2
```oracle
SELECT LTRIM('ABC12345', '7788A')
FROM DUAL; --이건 왼쪽에 A 있으니까 A만지운다. 약간 AB이면, A먼저 지우고 B다음에 지우고 이런식
```
출력결과
```oracle
LTRIM('ABC12345','7788A')
BC12345
```
- 7788은 왼쪽 문자열에 존재하지 않는다.
- A는 가장 왼쪽에 위치한 문자열이기 때문에 A만 지워졌다.


<br/>

### 예시08 - REPLACE와 TRANSLATE비교
```oracle
-- REPACE함수를 사용하여 사원이름에 SC문자열을 *?로 변경해서 조회하자.

    SELECT ENAME, REPLACE(ENAME, 'SC', '*?')
    FROM C##SCOTT.EMP;
```
출력결과
```oracle
ENAME	REPLACE(ENAME,'SC','*?')
SMITH	SMITH
ALLEN	ALLEN
WARD	WARD
JONES	JONES
MARTIN	MARTIN
BLAKE	BLAKE
CLARK	CLARK
SCOTT	*?OTT
KING	KING
TURNER	TURNER
ADAMS	ADAMS
JAMES	JAMES
FORD	FORD
MILLER	MILLER
```
- 정확히 'SC', 즉, S와 C가 붙어있는 문자열만 대체됐다.
- 'S' AND 'C' 랑 느낌이 비슷하다.

<br/>

- 그럼 TRANSLATE의 경우는 어떨까?

```oracle
-- TRANSLATE함수를 사용하여 사원이름에 SC문자열을 *?로 변경해서 조회하자.

    SELECT ENAME, TRANSLATE(ENAME, 'SC', '*?')
    FROM C##SCOTT.EMP;
```
출력결과
```oracle
ENAME	TRANSLATE(ENAME,'SC','*?')
SMITH	*MITH
ALLEN	ALLEN
WARD	WARD
JONES	JONE*
MARTIN	MARTIN
BLAKE	BLAKE
CLARK	?LARK
SCOTT	*?OTT
KING	KING
TURNER	TURNER
ADAMS	ADAM*
JAMES	JAME*
FORD	FORD
MILLER	MILLER
```
- 'S'와 'C'가 있는 문자열은 한개씩이라도 대체됐다.
- 'S'만 있는 문자열은 '*'로 대체되었고, S와 C가 모두 있는 문자열은 '*?'로 대체된 것을 확인할 수 있다.