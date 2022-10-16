# Oracle - 추가로 다뤄볼 함수들
## 몇가지 함수 소개
- CUME_DIST()
  - 누적된 분산정도를 출력(누적분포)
  - 그룹핑 -> 정렬 -> 그룹별 상대적인 위치(누적된 분산정도)
  - 상대적인 위치 : 구하고자 하는 값보다 작거나 같은 값을 가진 ROW수를 그룹의 전체 ROW수로 나눈것
  - 상대적인 위치는 0~1 사이의 값을 가진다.
> 누적분포 : 확률변수가 어떤 특정한 값보다 같거나 작을 확률, 모든 가능한 확률의 합은 1이다.

- NTILE(숫자)
  - 버킷 분할
  - 등분이 딱 나누어 떨어지지 않는다면 등분 후 나머지 행들을 1등분부터 차례로 배분한다.
    - 예 : 18행, 4등분의 경우, 총 4등분으로 나눈 후 나머지 2행을 1등분, 2등분에 1행씩 추가시킨다.

- RATIO_TO_REPORT
  - 해당 구간을 차지하는 비율
- LAG(컬럼명, 값을 가져올 행의 위치, 값이 없을 경우 기본값)
  - 그룹핑 내에서 상대적 로우를 참조한다.
  - 상대적으로 상위에 위치한 로우
  - 값을 가져올 행의 위치 = 몇번쨰 전 행의 값을 가져올 것인지 결정
  - __오름차순__ 의 경우 기중 로우의 __정렬 컬럼 값보다 작은 값__ 을 갖는 로우를 참조하기 위해 사용
  - _내림차순_ 의 경우 기준 로우의 _정렬 컬럼 값보다 큰 값_ 을 갖는 로우를 참조하기 위해 사용
  - 즉, 정렬했을 때 이전 행의 값을 리턴
- LEAD(컬럼명, 값을 가져올 행의 위치, 값이 없을 경우 기본값)
  - 그룹핑 내에서 상대적 로우를 참조한다.
  - 상대적으로 상위에 위치한 로우
  - 값을 가져올 행의 위치 = 몇번쨰 다음 행의 값을 가져올 것인지 결정
  - __오름차순__ 의 경우 기중 로우의 __정렬 컬럼 값보다 큰 값__ 을 갖는 로우를 참조하기 위해 사용
  - _내림차순_ 의 경우 기준 로우의 _정렬 컬럼 값보다 작은 값_ 을 갖는 로우를 참조하기 위해 사용
  - 즉, 정렬했을 때 다음 행의 값을 리턴

<br/>

### 예시05 - CUME_DIST()
```oracle
-- 20번 사원의 이름, 봉급, 누적분산을 출력해보자.

SELECT ENAME, SAL,
CUME_DIST() OVER (ORDER BY SAL) " 누적분산 "
FROM C##SCOTT.EMP
WHERE DEPTNO = 20;
```
출력결과
```oracle
ENAME             SAL    누적분산
---------- ---------- ----------
SMITH             800         .2
ADAMS            1100         .4
JONES            2975         .6
FORD             3000          1
SCOTT            3000          1
```
- 총 누적분산은 1로 수렴하므로
- 부서번호 20인 사원들의 봉급을 기준으로 한 누적분산이다.
- 즉, 봉급이 <800일 확률 = 0.2>, <봉급이 1100일 확률 = 0.2>,
- <봉급이 2975일 확률 = 0.2>, <봉급이 3000일 확률 = 0.4>인 것과 같다.

<br/>

### 예시06 - NTILE
```oracle
-- 사원의 봉급을 기준으로 4등분 하자.

SELECT ENAME, SAL,
NTILE(4) OVER (ORDER BY SAL) " 4등분 "
FROM C##SCOTT.EMP;
```
출력결과
```oracle
ENAME             SAL       4등분
---------- ---------- ----------
SMITH             800          1
JAMES             950          1
ADAMS            1100          1
WARD             1250          1
MARTIN           1250          2
MILLER           1300          2
TURNER           1500          2
ALLEN            1600          2
CLARK            2450          3
BLAKE            2850          3
JONES            2975          3
SCOTT            3000          4
FORD             3000          4
KING             5000          4
```
- NTILE의 경우, 등분을 할때 딱 떨어지지 않으면 앞 등분에 1행씩 추가한다.
- 이 경우에는 총 14행이 존재하는데, 4로 나누었을 때 2가 남는다
- 따라서 2행을 1, 2등분에 1행씩 추가로 부여한 것이다.

<br/>

### 예시07 - RATIO_TO_REPORT
```oracle
-- RATIO_TO_REPORT를 이용해서 해당 구간을 차지하는 비율을 리턴해보자.
-- 50000원을 봉급이 차지하는 비율에 따라 나눠준다고 할 때 각 사원은 얼마를 받을 수 있을지 추출하자.

SELECT ENAME, SAL,
RATIO_TO_REPORT(SAL) OVER() AS "비  율",
TRUNC(RATIO_TO_REPORT(SAL) OVER()*50000) AS "인상될 월급"
FROM C##SCOTT.EMP;
```
출력결과
```oracle
ENAME             SAL       비  율     인상될 월급
---------- ---------- ---------- ----------
SMITH             800    2.8E-02       1378
ALLEN            1600    5.5E-02       2756
WARD             1250    4.3E-02       2153
JONES            2975    1.0E-01       5124
MARTIN           1250    4.3E-02       2153
BLAKE            2850    9.8E-02       4909
CLARK            2450    8.4E-02       4220
SCOTT            3000    1.0E-01       5167
KING             5000    1.7E-01       8613
TURNER           1500    5.2E-02       2583
ADAMS            1100    3.8E-02       1894
JAMES             950    3.3E-02       1636
FORD             3000    1.0E-01       5167
MILLER           1300    4.5E-02       2239
```
- E-0x 의 의미
  - 10의-0x만큼 곱한 수를 앞의 소수에 곱했을 때 값을 나타낸다.
  - 즉, 2.8E-02 = 2.8 * 10^-2과 같다. -> 2.8 * 0.01 = 0.028
  - 즉, 3.5E+03 = 3.5 * 10^3과 같다. -> 3.5 * 1000 = 3500
- 따라서 이 경우 좀더 보기 쉽게 바꿔보자.
```oracle
ENAME             SAL       비  율     인상될 월급
---------- ---------- ---------- ----------
SMITH             800      0.028       1378
ALLEN            1600      0.055       2756
WARD             1250      0.043       2153
JONES            2975        0.1       5124
MARTIN           1250      0.043       2153
BLAKE            2850      0.098       4909
CLARK            2450      0.084       4220
SCOTT            3000        0.1       5167
KING             5000       0.17       8613
TURNER           1500      0.052       2583
ADAMS            1100      0.038       1894
JAMES             950      0.033       1636
FORD             3000        0.1       5167
MILLER           1300      0.045       2239
```
- 각 사원의 봉급이 차지하는 비율만큼 봉급이 분배되었다.

<br/>

### 예시08 - LAG
```oracle
SELECT ENAME, DEPTNO, SAL,
LAG(SAL, 1, 0) OVER (ORDER BY SAL) AS NEXT_SAL,
LAG(SAL, 1, SAL) OVER (ORDER BY SAL) AS NEXT_SAL02,
LAG(SAL, 1, SAL) OVER (PARTITION BY DEPTNO ORDER BY SAL) AS NEXT_SAL03
FROM C##SCOTT.EMP;
```
출력결과
```oracle
ENAME          DEPTNO        SAL   NEXT_SAL NEXT_SAL02 NEXT_SAL03
---------- ---------- ---------- ---------- ---------- ----------
SMITH              20        800          0        800        800
JAMES              30        950        800        800        950
ADAMS              20       1100        950        950        800
MARTIN             30       1250       1100       1100        950
WARD               30       1250       1250       1250       1250
MILLER             10       1300       1250       1250       1300
TURNER             30       1500       1300       1300       1250
ALLEN              30       1600       1500       1500       1500
CLARK              10       2450       1600       1600       1300
BLAKE              30       2850       2450       2450       1600
JONES              20       2975       2850       2850       1100
FORD               20       3000       2975       2975       3000
SCOTT              20       3000       3000       3000       2975
KING               10       5000       3000       3000       2450
```
- 결과를 두 커럼씩 나누어서 보자.

<br/>

##### LAG(SAL, 1, 0) - NEXT_SAL
```oracle
LAG(SAL, 1, 0)
봉급의 첫번째 전 행의 값을 가져오며, 값이 없을 경우엔 0을 리턴하라는 의미이다.

         SAL   NEXT_SAL 
  ---------- ---------- 
        800          0 - 전 행이 존재하지 않는다. 따라서 0 리턴
        950        800 - 전 행은 800
       1100        950 - 전 행은 950
       1250       1100 - 전 행은 1100
       1250       1250 - .
       1300       1250 - . 
       1500       1300 - . 
       1600       1500      
       2450       1600    
       2850       2450     
       2975       2850 - . 
       3000       2975 - .
       5000       3000 - 전 행은 2975
```
##### LAG(SAL, 1, SAL) = NEXT_SAL02
```oracle
LAG(SAL, 1, SAL)
봉급의 첫번째 전 행 값을 가져오며, 값이 없을 경우엔 봉급을 리턴

        SAL  NEXT_SAL02 
 ----------  ---------- 
        800         800 - 전 행이 존재하지 않는다. 따라서 봉급인 800을 리턴
        950         800 - 전 행은 800
       1100         950 - 위와 동일한 로직
       1250        1100   
       1250        1250   
       1300        1250  
       1500        1300 
       1600        1500  
       2450        1600   
       2850        2450  
       2975        2850  
       3000        2975  
       3000        3000  
       5000        3000 - 위와 동일한 로직, 전 행은 3000
```
##### LAG(SAL, 1, SAL) - PARTITION BY DEPTNO ORDER BY SAL - NEXT_SAL03
```oracle
LAG(SAL, 1, SAL) - PARTITION BY DEPTNO ORDER BY SAL
부서번호 파티션 내에서, 봉급의 첫번째 전 행 값을 가져오며, 값이 없을 경우엔 봉급을 리턴

     DEPTNO        SAL   NEXT_SAL03
 ---------- ----------   ----------
         20        800         800           - *1리턴
         30        950         950                      - ^1리턴
         20       1100         800           - *1리턴
         30       1250         950                      - ^1리턴
         30       1250        1250                      - ^2리턴
         10       1300        1300 - (1)리턴
         30       1500        1250                      - ^3리턴
         30       1600        1500                      - ^4리턴
         10       2450        1300 - (1)리턴
         30       2850        1600                      - ^5리턴
         20       2975        1100           - *2리턴
         20       3000        3000           - *4리턴
         20       3000        2975           - *3리턴
         10       5000        2450 - (2)리턴
```
- 부서번호 10만 따로 보자. 봉급 순으로 정렬해보면
  - 1300(1), 2450(2), 5000(3)이다.
  - 따라서 부서번호 10의 첫번째는 전 행이 없으므로 1300(1)리턴, 두번째는 전 행인 1300(1)리턴,
  - 세번째는 두번째 행이었던 2450(2)을 리턴된 것이다.
- 부서번호 20만 따로 보자. 봉급 순으로 정렬해보면
  - 800(*1), 1100(*2), 2975(*3), 3000(*4), 3000(*5)
  - 따라서 부서번호 20의 첫번째는 전 행이 없으므로 800(*1)리턴, 두번쨰는 전 행인 800(*1)리턴,
  - 세번째는 두번째 행이었던 110(*2)리턴,,, 이런식으로 리턴된다.
  - 3000의 경우 두 행이 존재하는데, 부서번호 파티션에서 봉급으로 정렬했을 때 기준으로 전 행이 결정된다.
- 부서번호 30만 따로 보자. 봉급 순으로 정렬해보면
  - 950(^1), 1250(^2), 1250(^3), 1500(^4), 1600(^5) 2850(^6)
  - 위와 같은 로직으로 전 행의 값들이 리턴되었다.

<br/>

### 예시09 - LEAD
```oracle
SELECT ENAME, DEPTNO, SAL,
LEAD(SAL, 1, 0) OVER (ORDER BY SAL) AS NEXT_SAL,
LEAD(SAL, 1, SAL) OVER (ORDER BY SAL) AS NEXT_SAL02
FROM C##SCOTT.EMP;
```
출력결과
```oracle
ENAME          DEPTNO        SAL   NEXT_SAL NEXT_SAL02
---------- ---------- ---------- ---------- ----------
SMITH              20        800        950        950
JAMES              30        950       1100       1100
ADAMS              20       1100       1250       1250
WARD               30       1250       1250       1250
MARTIN             30       1250       1300       1300
MILLER             10       1300       1500       1500
TURNER             30       1500       1600       1600
ALLEN              30       1600       2450       2450
CLARK              10       2450       2850       2850
BLAKE              30       2850       2975       2975
JONES              20       2975       3000       3000
SCOTT              20       3000       3000       3000
FORD               20       3000       5000       5000
KING               10       5000          0       5000
```
- 위의 LAG와 같은 로직으로 다음 행이 출력되었다.
- NEXT_SAL의 경우, 리턴할 값이 없으면 0을 출력하므로, 가장 마지막 행에 0이 리턴되었다.
- NEXT_SAL02의 경우, 리턴할 값이 없으면 SAL을 출력하므로, 가장 마지막 행에 5000이 리턴되었다.