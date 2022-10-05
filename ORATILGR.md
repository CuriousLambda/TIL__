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
-- 사원테이블에서 부서별로 봉급으로, 가장큰값, 작은값, 중간값, 평균, 합계를 구해보자.

SELECT DEPTNO, MAX(SAL), MIN(SAL), MEDIAN(SAL), ROUND(AVG(SAL),-1), SUM(SAL)
FROM C##SCOTT.EMP
GROUP BY DEPTNO;
```
출력결과
```oracle
DEPTNO	MAX(SAL)	MIN(SAL)	MEDIAN(SAL)	ROUND(AVG(SAL),-1)	SUM(SAL)
10	5000	        1300	    2450	        2920	        8750
20	3000	        800	    2987.5	        2310	        13875
30	2850	        950	    1375	        1570	        9400
```
   