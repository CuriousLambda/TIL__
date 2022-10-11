# Oracle - Practice01
> 그동안의 내용에 대한 예제 풀이

<br/>

#### _실습에 사용한 EMPLOYEES 테이블_
![EMPLOYEE_TABLE01](https://user-images.githubusercontent.com/93986157/195105739-e07bb692-868d-4734-af40-42015abcf9cf.png)
![EMPLOYEE_TABLE02](https://user-images.githubusercontent.com/93986157/195105870-58ae5b65-9c01-4360-9587-16e4cefdd49f.png)
![EMPLOYEE_TABLE03](https://user-images.githubusercontent.com/93986157/195105972-a7241886-4ebf-4461-a501-93879952f94e.png)

<br/>

### 예제01
- [문제1] 사원테이블에서 부서가 90번인 사원들의 사원명,입사일,연봉,부서코드를 출력하시오.
  - 조건1) 제목은 사원명, 입 사 일,연 봉,부서코드로 하시오.
  - 조건2) 연봉 = 급여 * 12
  - 조건3) 연봉 뒤에 화폐단위 "원"을 붙이시오.
  - 조건4) 사원명은 first_name , last_name을 연결 하시오.
```oracle
SELECT FIRST_NAME ||' ' || LAST_NAME AS "사원명", HIRE_DATE AS "입 사 일",
SALARY*12||'원' AS "연 봉", DEPARTMENT_ID AS "부서코드"
FROM HR.EMPLOYEES
WHERE DEPARTMENT_ID = 90;
```
출력결과
```oracle
사원명	        입 사 일	연 봉	부서코드
Steven King	03/06/17	288000원	90
Neena Kochhar	05/09/21	204000원	90
Lex De Haan	01/01/13	204000원	90
```
- 컬럼명에 별칭을 줄 때 별칭에 띄어쓰기가 있다면 큰따옴표(" ")를 사용해야 한다.
- 두 컬럼을 연결할 때는 CONCAT 함수를 사용하거나 연결문자열(||)를 사용한다.
  - FIRST_NAME과 LAST_NAME 연결
- 또한 출력 시 값들에 특정 문자열을 추가하고 싶을 경우에도 연결문자열(||)를 사용할 수 있다.
  - 연봉 뒤에 화폐단위 "원" 추가

<br/>

### 예제02
- [문제2]  급여가 2500이하 이거나 3000이상이면서 90번 부서인 사원의 이름, 급여, 부서ID를 출력하시오.
  - 조건1) 제목은 사원명, 월 급, 부서코드로 하시오.
  - 조건2) 급여앞에 $를 붙이시오.
  - 조건3) 사원명은 first_name과 last_name을 연결해서 출력하시오.

```oracle
SELECT FIRST_NAME ||' ' || LAST_NAME AS "사원명", '$' || SALARY "월 급", DEPARTMENT_ID "부서코드"
FROM HR.EMPLOYEES
WHERE SALARY NOT BETWEEN 2500 AND 3000 AND DEPARTMENT_ID = 90;
```
출력결과
```oracle
사원명	        월 급	부서코드
Steven King	$24000	90
Neena Kochhar	$17000	90
Lex De Haan	$17000	90
```
- 1번과 거의 비슷하다.
- 하지만 조건문에서 '급여가 2500이하 이거나 3000이상이면서 90번 부서' 를 나타내기 위해 NOT BETWEEN을 사용했다.
- `SALARY NOT BETWEEN 2500 AND 3000`
  - 급여가 2500과 3000사이에 있지 않는 경우 = 급여가 2500이하 이거나 3000이상인 경우

<br/>

### 예제03
- [문제3] Employees테이블의 업무ID가 중복되지 않게 표시하는 질의를 작성하시오.
```oracle
SELECT DISTINCT JOB_ID
FROM HR.EMPLOYEES;
```
출력결과
```oracle
JOB_ID
AC_ACCOUNT
AC_MGR
AD_ASST
AD_PRES
AD_VP
FI_ACCOUNT
FI_MGR
HR_REP
IT_PROG
MK_MAN
MK_REP
PR_REP
PU_CLERK
PU_MAN
SA_MAN
SA_REP
SH_CLERK
ST_CLERK
ST_MAN
```
- 중복을 제거한 조회를 할 떄는 DISTINCT함수를 사용했었다.

<br/>

### 예제04
- [문제4] 업무ID에 MAN이 포함되어있는 사원들의 이름,업무ID,부서ID를 출력하시오.
```oracle
SELECT LAST_NAME, JOB_ID, DEPARTMENT_ID
FROM HR.EMPLOYEES
WHERE JOB_ID LIKE '%MAN%';
```
출력결과
```oracle
LAST_NAME	JOB_ID	DEPARTMENT_ID
Raphaely	PU_MAN	30
Weiss	        ST_MAN	50
Fripp	        ST_MAN	50
Kaufling	ST_MAN	50
Vollman	        ST_MAN	50
Mourgos	        ST_MAN	50
Russell	        SA_MAN	80
Partners	SA_MAN	80
Errazuriz	SA_MAN	80
Cambrault	SA_MAN	80
Zlotkey	        SA_MAN	80
Hartstein	MK_MAN	20
```
- JOB_ID LIKE '%MAN' : 직업이 MAN으로 끝나는 것을 나타냄
- JOB_ID LIKE 'MAN%' : 직업이 MAN으로 시작되는 것을 나타냄
- JOB_ID LIKE '%MAN%' : 직업에 MAN이 포함되어있는 것을 나타냄

<br/>

### 예제05
- [문제5] 사원테이블에서 업무ID가 IT_PROG,ST_MAN,SA_REP인 사원을 표시하시오.
  - 조건1) 사원명, 업무ID, 부서ID만 표시.
  - 조건2) or 연산자, in 연산자 둘다 사용하시오.
```oracle
SELECT LAST_NAME AS "사원명", JOB_ID AS "업무ID", DEPARTMENT_ID AS "부서ID"
FROM HR.EMPLOYEES
WHERE JOB_ID IN ('IT_PROG','ST_MAN') OR JOB_ID = 'SA_REP';
```
출력결과
```oracle
사원명	    업무ID	부서ID
Hunold	    IT_PROG	60
Ernst	    IT_PROG	60
Austin	    IT_PROG	60
Pataballa	IT_PROG	60
Lorentz	    IT_PROG	60
Weiss	    ST_MAN	50
Fripp	    ST_MAN	50
Kaufling	ST_MAN	50
Vollman	    ST_MAN	50
Mourgos	    ST_MAN	50
Tucker	    SA_REP	80
Bernstein	SA_REP	80
Hall	    SA_REP	80
Olsen	    SA_REP	80
Cambrault	SA_REP	80
Tuvault	    SA_REP	80
King	    SA_REP	80
Sully	    SA_REP	80
McEwen	    SA_REP	80
Smith	    SA_REP	80
Doran	    SA_REP	80
Sewall	    SA_REP	80
Vishney	    SA_REP	80
Greene	    SA_REP	80
Marvins	    SA_REP	80
Lee	    SA_REP	80
Ande	    SA_REP	80
Banda	    SA_REP	80
Ozer	    SA_REP	80
Bloom	    SA_REP	80
Fox	    SA_REP	80
Smith	    SA_REP	80
Bates	    SA_REP	80
Kumar	    SA_REP	80
Abel	    SA_REP	80
Hutton	    SA_REP	80
Taylor	    SA_REP	80
Livingston	SA_REP	80
Grant	    SA_REP	
Johnson	    SA_REP	80
```
- IN 연산자는 OR와 동일하게 연산된다. 괄호 안의 것들 중 만족하는 것이 하나라도 있다면 출력해준다.
- 따라서, `JOB_ID = 'IT_PROG' OR JOB_ID = 'ST_MAN' OR JOB_ID = 'SA_REP'` 이런식으로 작성해도 무방하다.

### 예제06
- [문제6] 다음의 조건을 만족하는 사원의 레코드를 검색하시오.
  - 조건1) 이름과 성을 연결하시오.
  - 조건2) 구해진 이름의 길이를 구하시오.
  - 조건3) 성이 n으로 끝나는 사원.

```oracle
SELECT EMPLOYEE_ID, CONCAT(FIRST_NAME, LAST_NAME) "NAME", LENGTH(FIRST_NAME || LAST_NAME) AS "LENGTH"
FROM HR.EMPLOYEES
WHERE LAST_NAME LIKE '%n';
```
출력결과
```oracel
EMPLOYEE_ID	NAME	        LENGTH
102	        LexDe Haan	        10
105	        DavidAustin	        11
110	        JohnChen	        8
112	        Jose ManuelUrman	16
123	        ShantaVollman	    13
130	        MozheAtkinson	    13
132	        TJOlson	            7
133	        JasonMallin	    11
151	        DavidBernstein	14
153	        ChristopherOlsen	16
158	        AllanMcEwen	    11
160	        LouiseDoran	    11
175	        AlyssaHutton	    12
177	        JackLivingston	    14
179	        CharlesJohnson	    14
182	        MarthaSullivan	    14
194	        SamuelMcCain	    12
200	        JenniferWhalen	    14
201	        MichaelHartstein	16
```
- 앞서 보았듯이, 두 컬럼을 합칠 때는 CONCAT이나 연결문자열(||)을 사용할 수 있다.
- LENGTH안에 연결문자열로 연결된 두 컬럼을 넣어 합쳐진 컬럼의 길이를 구했다.

<br/>

### 예제07
- [문제7] 2007년 이후에 고용된 사원을 찾으시오.
```oracle
SELECT LAST_NAME, TO_CHAR(HIRE_DATE,'DD-MON-YYYY')
FROM HR.EMPLOYEES
WHERE EXTRACT(YEAR FROM HIRE_DATE) >= 2007;
```
출력결과
```oracle
LAST_NAME	TO_CHAR(HIRE_DATE,'DD-MON-YYYY')
Ernst	    21-5월 -2007
Lorentz 	07-2월 -2007
Popp	    07-12월-2007
Colmenares	10-8월 -2007
Mourgos	    16-11월-2007
Landry	    14-1월 -2007
Markle	    08-3월 -2008
Olson	    10-4월 -2007
Gee	1   2-12월-2007
Philtanker	06-2월 -2008
Cambrault	15-10월-2007
Zlotkey	    29-1월 -2008
Tuvault	    23-11월-2007
Greene	    19-3월 -2007
Marvins	    24-1월 -2008
Lee	    23-2월 -2008
Ande	    24-3월 -2008
Banda	    21-4월 -2008
Smith	    23-2월 -2007
Bates	    24-3월 -2007
Kumar	    21-4월 -2008
Grant	    24-5월 -2007
Johnson	    04-1월 -2008
Sullivan	21-6월 -2007
Geoni	    03-2월 -2008
Cabrio	    07-2월 -2007
Perkins	    19-12월-2007
Jones	    17-3월 -2007
OConnell	21-6월 -2007
Grant	    13-1월 -2008
```
- HIRE_DATE를 TO_CHAR를 통해 원하는 형태('DD-MON-YYYY')의 문자열로 바꾸어주고
- EXTRACT를 사용해서 HIRE_DATE에서 연도를 추출했다.

<br/>

### 예제08
- [문제8] 급여가 10000미만이면 초급, 20000미만이면 중급 그 외면 고급을 출력하시오.
  - 조건1) 컬럼명은 사원번호, 사원명, 구 분 으로 하시오.
  - 조건2) 구분(오름차순)으로 정렬하고, 같으면 사원명(오름차순)으로 정렬하시오.
  - 조건3) 부서번호가 20 또는 90인 사원들만 조회하시오.
```oracle
SELECT EMPLOYEE_ID "사원번호", LAST_NAME "사원명",
DECODE(SIGN(SALARY-10000),-1,'초급', DECODE(SIGN(SALARY-20000),-1,'중급','고급')) "구분"
FROM HR.EMPLOYEES
WHERE DEPARTMENT_ID = 20 OR DEPARTMENT_ID = 90
ORDER BY 3, 2;
```
- 비슷한 다른 방법도 있다.
```oracle
SELECT EMPLOYEE_ID "사원번호", LAST_NAME "사원명",
CASE WHEN SALARY < 10000 THEN '초급' 
             WHEN SALARY>=10000 AND SALARY<20000 THEN '중급'
             ELSE '고급' END  AS "구분"
FROM HR.EMPLOYEES
WHERE DEPARTMENT_ID = 90 OR DEPARTMENT_ID = 20
ORDER BY 3, 2;
```
출력결과
```oracle
사원번호	사원명	    구분
100	King	    고급
102	De Haan	    중급
201	Hartstein	중급
101	Kochhar	    중급
202	Fay	    초급
```
- 이전에 DECODE와 CASE WHEN을 같이 다루었듯이 서로 비슷한 기능을 한다.
- DECODE는 첫번째 인자가 두번째 인자와 같은지 아닌지 비교만 가능했기에, SIGN함수를 통해 값을 비교할 수 있도록 바꿔주었다.
- CASE WHEN은 비교적 자유롭게 원하는 조건식을 작성할 수 있었다.
- 따라서 비교연산자를 사용해 조건식을 작성했다.

<br/>

### 예제09
- [문제9] 사원테이블에서 사원번호, 이름, 급여, 커미션, 연봉을 출력하시오.
  - 조건1) 연봉은 $ 표시거 앞쪽에 출력되도록 하시오.
  - 조건2) 연봉 = 급여 * 12 + (급여 * 12 * 커미션)
  - 조건3) 커미션을 받지 않는 사원도 포함해서 출력하시오.
  - 조건4) 사원번호가 130보다 크고 150이하인 사원들만 조회하시오.

```oracle
SELECT EMPLOYEE_ID "사원번호", LAST_NAME "사원이름", SALARY "급여", COMMISSION_PCT "커미션",
'$' || (SALARY * 12 + (SALARY *12 * NVL(COMMISSION_PCT,0))) "연봉"
FROM HR.EMPLOYEES
WHERE EMPLOYEE_ID > 130 AND EMPLOYEE_ID <= 150;
```
출력결과
```oracle
사원번호	사원이름	        급여	커미션	연봉
131	Marlow	        2500		$30000
132	Olson	        2100		$25200
133	Mallin	        3300		$39600
134	Rogers	        2900		$34800
135	Gee	        2400		$28800
136	Philtanker	2200		$26400
137	Ladwig	        3600		$43200
138	Stiles	        3200		$38400
139	Seo	        2700		$32400
140	Patel	        2500		$30000
141	Rajs	        3500		$42000
142	Davies	        3100		$37200
143	Matos	        2600		$31200
144	Vargas	        2500		$30000
145	Russell	        14000	0.4	$235200
146	Partners	13500	0.3	$210600
147	Errazuriz	12000	0.3	$187200
148	Cambrault	11000	0.3	$171600
149	Zlotkey	        10500	0.2	$151200
150	Tucker	        10000	0.3	$156000
```
- $를 붙이거나 연봉식을 설정해주는 것은 위의 예제에서 다루었기 때문에 어렵지 않았다.
- 하지만 <커미션을 받지 않는 사원 = 커미션이 null인 사원> 인데, 이 값을 계산하기 위해
  - NVL을 통해 COMMISION_PCT가 null인 사원의 경우 커미션을 0으로 바꾸어주었다.
  - 따라서 커미션이 null일지라도 값이 0으로 변환되어 연봉계산식이 차질없이 돌아간다.
<br/>

