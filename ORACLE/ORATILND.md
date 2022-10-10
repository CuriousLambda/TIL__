# Oracle - 숫자함수, 날짜함수

## 1. 숫자함수
- ROUND(숫자, 정수) : 반올림
- TRUNC(숫자, 정수) : 버림
- MOD(숫자, 숫자) : 나머지
- ABS(숫자) : 절대값
- FLOOR(숫자)
  - 해당 수보다 작거나 같은 정수 중 가장 큰 정수값을[최대정수값] 리턴
  - 숫자가 양수일 경우는 TRUNC와 비슷하지만 숫자가 음수일 경우 정확한 의미는 위의 의미이다.
- CEIL(숫자)
  - 해당 수보다 크거나 같은 정수 중 가장 작은 정수값을[최소정수값] 리턴
  - CEIL도 마찬가지로 숫자가 양수일 경우 올림과 비슷하지만 숫자가 음수일 경우 정확한 의미는 위의 의미이다.
- SIGN(숫자) : 숫자가 음수, 양수, 0인지를 출력해주는 함수
- POWER(숫자1, 숫자2) : 숫자1의 숫자2승

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

  
### 예시01
```oracle
-- ROUND를 확인해보자.

SELECT ROUND(4567.678) 결과1, ROUND(4567.678,0) 결과2,
ROUND(4567.678,2) 결과3, ROUND(4567.678,-2) 결과4
FROM DUAL;
```
출력결과
```oracle
결과1	결과2	결과3	결과4
4568	4568	4567.68	4600
```

<br/>

### 예시02
```oracle
-- TRUNC를 확인해보자.

SELECT TRUNC(4567.678) 결과1, TRUNC(4567.678,0) 결과2,
TRUNC(4567.678,2) 결과3, TRUNC(4567.678,-2) 결과4
FROM DUAL;
```
출력결과
```oracle
결과1	결과2	결과3	결과4
4567	4567	4567.67	4500
```

<br/>

### 예시03
```oracle
-- 사원 테이블에서 급여를 30으로 나눈 나머지를 출력하자. 이름과 급여, 결과를 출력해보자.

SELECT E.ENAME, SAL, MOD(SAL,30) 결과
FROM C##SCOTT.EMP E;
```
출력결과
``` oracle
ENAME	SAL	결과
SMITH	800	20
ALLEN	1600	10
WARD	1250	20
JONES	2975	5
MARTIN	1250	20
BLAKE	2850	0
CLARK	2450	20
SCOTT	3000	0
KING	5000	20
TURNER	1500	0
ADAMS	1100	20
JAMES	950	20
FORD	3000	0
MILLER	1300	10
```

<br/>

## 2. 날짜함수
- 날짜 형식은 산술 연산이 가능하다.
- extract(YEAR / MONTH / DAY... FROM 날짜 = datetime) : 날짜에서 특정 값 추출
- MONTHS_BETWEEN(날짜1, 날짜2) : 날짜1-날짜2 된 개월 수 -- 숫자리턴
- ADD_MONTHS(날짜, 숫자) : 날짜 + 숫자 한 월
- NEXT_DAY(기준일자, '찾을요일') : 기준일자보다 이후 날짜로 지정한 요일에 해당하는 날짜
- LAST_DAY : 해당월의 마지막 날짜
- TO_DATE('문자열','MM-DD-YYYY'= 날짜포맷) : 문자를 날짜포맷으로 변환해서 타입을 날짜로 리턴

<br/>

### 예시04 - EXTRACT
```oracle
-- 오늘 날짜 중 년도만 조회하고 싶다.

SELECT EXTRACT(YEAR FROM SYSDATE) FROM DUAL;
```
출력결과
```oracle
EXTRACT(YEARFROMSYSDATE)
2022
```
<br/>

### 예시05 - MONTH_BETWEEN
```oracle
SELECT MONTHS_BETWEEN(TO_DATE('02-02-1995','MM-DD-YYYY'), TO_DATE('01-01-1995', 'MM-DD-YYYY')) RES
FROM DUAL;
```
출력결과
```oracle
RES
1.03225806451612903225806451612903225806
```
<br/>

### 예시06 - ADD_MONTH
```oracle
-- 사원테이블에서 10번, 30번 부서의 사원들의 입사일로부터 5개월이 지난 후 날자를 계산해서 출력해보자.
-- 출력예시 : ENAME, HIREDATE, A_MONTH로 출력

SELECT ENAME, HIREDATE, ADD_MONTHS(HIREDATE, 5) A_MONTH
FROM C##SCOTT.EMP
WHERE DEPTNO = 10 OR DEPTNO = 30
ORDER BY 2 DESC;
```
출력결과
```oracle
ENAME	HIREDATE	A_MONTH
MILLER	82/01/23	82/06/23
KING	81/11/17	82/04/17
JAMES	81/10/03	82/03/03
MARTIN	81/09/28	82/02/28
TURNER	81/09/08	82/02/08
CLARK	81/06/01	81/11/01
BLAKE	81/04/01	81/09/01
WARD	81/02/22	81/07/22
ALLEN	81/02/20	81/07/20
```
<br/>

### 예시07 - NEXT_DAY
```oracle
-- 사원테이블에서 10번 부서 사원들의 입사일로부터 돌아오는 금요일을 계산해서 리턴하자.

SELECT ENAME, HIREDATE, NEXT_DAY(HIREDATE, 6)
FROM C##SCOTT.EMP
WHERE DEPTNO = 10;
```
출력결과
```oracle
ENAME	HIREDATE	NEXT_DAY(HIREDATE,6)
CLARK	81/06/01	81/06/05
KING	81/11/17	81/11/20
MILLER	82/01/23	82/01/29
```
> 1 : 일요일 ~ 7 : 토요일

<br/>

## 3. 날짜함수 응용 - ROUND, TRUNC
- ROUND와 TRUNC를 날짜함수와 함께 사용하면 날짜를 가장 가까운 연도 또는 달로 반올림할 수 있다.
- ROUND
  - 일 : 정오를 넘으면 다음날 자정을 리턴 / 넘지 않으면 그날 자정을 리턴한다. 
  - 월 : 15일 이상이면 다음달 1을 출력 / 넘지 않으면  현재 달 1을 리턴
  - 년도 : 6월을 넘으면 다음해 1월1일 리턴 / 넘지 않으면 현재 1월 1일 리턴
- TRUNC
  - 일 : 그날 자정출력
  - 월 : 그 달 1을출력
  - 년도 : 금년 1월1일 리턴    

<br/>


### 예시08
```oracle
-- 현재 날짜에 ROUND와 TRUNC함수를 사용해보자.

SELECT   to_char(sysdate, 'YY/MM/DD HH24:MI:SS') normal, 
          to_char(trunc(sysdate), 'YY/MM/DD HH24:MI:SS') trunc, 
          to_char(round(sysdate), 'YY/MM/DD HH24:MI:SS') round 
          FROM  dual;
```
출력결과
```oracle
NORMAL	TRUNC	ROUND
22/10/06 21:34:39	22/10/06 00:00:00	22/10/07 00:00:00
```

## 4. 날짜함수 번외편
- RR/MM/DD(00~49 : 2000년대)
- DD/MON/RR(50~99:1900년대)
- TO_TIMESTAMP : CHAR, VARCHAR2 데이터 타입을 TIMESTAMP데이터 타입으로 리턴 
- TO_TIMESTAMP_TZ : CHAR, VARCHAR2 데이터 타입을 TIMESTAMP WITH TIME ZONE 데이터 타입으로 리턴 (Only Oracle)
- TO_DSINTERVAL : CHAR, VARCHAR2 데이터 타입을 INTERVAL DAY TO SECOND 데이터 타입으로 리턴
- TO_YMINTERVAL : CHAR, VARCHAR2 데이터 타입을 INTERVAL YEAR TO MONTH 데이터 타입으로 리턴


### 예시09
```oracle
SELECT TO_CHAR(TO_DATE('98','RR'),'YYYY') test1, 
TO_CHAR(TO_DATE('05','RR'),'YYYY') test2, 
TO_CHAR(TO_DATE('98','YY'),'YYYY') test3, 
TO_CHAR(TO_DATE('05','YY'),'YYYY') test4 
FROM  dual;
```
출력결과
```oracle
TEST1	TEST2	TEST3	TEST4
1998	2005	2098	2005
```
- RR은 반올림의 개념이 포함된 것으로, 연도의 경우 100년단위로 반올림된다.
  - 현재년도가 2020년이면 반올림한 2000년대가 기준년도가 된다.
  - 기준년도 전년도는 1900년이다.
  - 따라서 00~49까지는 20XX로 붙게되고, 50~99까지는 19XX로 붙게 된다.
- 첫번째 : 98, RR -> 1900년대 -> 1998
- 두번째 : 05, RR -> 2000년대 -> 2005
- 세번째 : 98, YY -> 2000년대 -> 2098
- 네번째 : 05, YY -> 2000년대 -> 2005

<br/>

### 예시10
```oracle
SELECT   TO_TIMESTAMP_TZ ('2004-8-20 1:30:00 -3:00', 'YYYY-MM-DD HH:MI:SS TZH:TZM')
FROM DAUL;
```
출력결과
```oracle
TO_TIMESTAMP_TZ('2004-8-201:30:00-3:00','YYYY-MM-DDHH:MI:SSTZH:TZM')
04/08/20 01:30:00.000000000 -03:00
```
<br/>

### 예시11
```oracle
SELECT TO_TIMESTAMP('2004-8-20 1:30:00', 'YYYY-MM-DD HH:MI:SS')
FROM DUAL;
```
출력결과
```oracle
TO_TIMESTAMP('2004-8-201:30:00','YYYY-MM-DDHH:MI:SS')
04/08/20 01:30:00.000000000
```

<br/>

### 예시12
```oracle
SELECT SYSDATE, SYSDATE + TO_YMINTERVAL('01-03') "15Months later" 
FROM  DAUL;
```
출력결과
```oracle
SYSDATE	15Months later
22/10/06	24/01/06
```
- 1년 3개월을 SYSDATE에 추가하는 코드
- 1년 3개월은 15개월이다.

<br/>

### 예시13
```oracle
SELECT  SYSDATE, SYSDATE + TO_DSINTERVAL('003 17:00:00') "3days 17hours later" 
FROM DUAL;
```
출력결과
```oracle
SYSDATE	3days 17hours later
22/10/06	22/10/10
```
- 3일 17시간 00분 00초를 SYSDATE에 추가하는 코드이다.
