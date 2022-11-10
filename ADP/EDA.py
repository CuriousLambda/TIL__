import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


## 1. 데이터 로드
data = load_iris()
print(data.keys())
print(data.DESCR)




## 2-1. DataFrame 변환 - feature 테이블 만들기
features = pd.DataFrame(data = data.data, columns = data.feature_names)
print(features)




## 2-2. DataFrame 변환 - target 테이블 만들기
targets = pd.DataFrame(data = data.target, columns = ["species"])
print(targets)




## 2-3. feature와 target 테이블 통합시키기 - concat활용
iris = pd.concat([features, targets], axis = 1)
print(iris)
# axis = 0 : 위 아래로 합치기
# axis = 1 : 옆 방향으로 합치기




## 2-4. 컬럼명의 공백 제거
iris.rename({'sepal length (cm)' : 'sepal_length', 'sepal width (cm)' : 'sepal_width',
'petal length (cm)' : 'petal_length', 'petal width (cm)' : 'petal_width'}, axis = 1, inplace = True)
print(iris)




## 2-5. species의 행 값을 분류 명으로 변경
## 현재 setosa = 0, virgicolor = 1, virginica = 2로 되어있는 상태, 이 숫자들을 문자로 바꿔주기
iris['species'] = iris['species'].map({0 : 'setosat', 1 : 'virgicolor', 2 : 'virginica'})
print(iris)


## 2-6. 결측값 처리 : null, NaN, None, na등등 확인
nacnt = iris.isna().sum(axis = 0)
print(nacnt)
# 결측 개수를 알기위해서 sum 사용




## 2-7. 기초통계분석 - 데이터 크기, 데이터 행렬 형태, 데이터 타입, 분포, feature간의 관계 등 확인
iris.info()
stat_info = iris.describe()
print(stat_info)




## 2-8. 상관분석 : 두 feature간 관계 확인
corr = iris.corr()
print(corr)

## < 상관분석 결과> ##
# 다중공선성 : 어떤 독립변수가 다른 독립변수와 완벽한 선형 독립이 아닌 경우
#             즉, 독립변수끼리 서로 의존(상관이 있는)하는 관계
# 상관계수가 높은 feature 들은 다중공선성 문제를 야기시킬 수 있다. -> 두 feature 중 한 feature만 분석에 사용
# 독립변서가 서로 의존하게 되면 과최적화(over-fitting) 문제가 발생해 회귀 결과의 안정성을 해칠 가능성이 높아진다,
# 이럴 경우 크게 3가지를 고려해볼 수 있다.
#   1) 변수 선택법으로 의존적인 변수 삭제
#   2) PCA(principal component analysis) 주성분분석 방법으로 의존적인 성분 삭제 
#   3) 정규화(regularized)




## 2-9. 집계분석
group = iris.groupby('species').size()
# count는 결측값을 제외하고 카운팅하기 때문에 size로 확인




## 2-10-1. 이상치 탐색 , 그래프로 확인 - botxplot
def boxplot_iris(feature_names, dataset):
    i = 1
    plt.figure(figsize=(11,9))

    for col in feature_names:
        plt.subplot(2,2,i)
        plt.axis('on')
        plt.tick_params(axis = 'both', left = True)
        dataset[col].plot(kind = 'box', subplots = True)
        plt.title(col)
        i += 1
    
    plt.show()
boxplot_iris(iris.columns[:-1], iris)

## < 그래프 결과 분석 > ##
# sepal_length와 sepal_width는 박스길이가 짧다. -> 데이터가 좁게 분포되어 있다.
# petal_length와 petal_width는 박스길이가 길다. -> 데이터가 넓게 분포되어 있다.
# sepal_width에서 이상치 탐지됨.




## 2-10-2. 이상치 탐색, 그래프로 확인 - histogram
def histogram_iris(feature_names, dataset):
    i = 1
    plt.figure(figsize=(11,9))

    for col in feature_names:
        plt.subplot(2,2,i)
        plt.axis('on')
        plt.tick_params(axis = 'both', left = True)
        dataset[col].hist()
        plt.title(col)
        i += 1
    
    plt.show()
histogram_iris(iris.columns[:-1], iris)

## < 그래프 결과 분석 > ##
# sepal_width의 히스토그램 분포 가운데에 집중 -> sepal_width의 데이터는 중앙에 집중
# petal_length는 빈도수가 높긴 하지만 데이터가 낮은쪽에 치중되어 있음




## 2-10-3. 상관관계 시각화 - heatmap
# corr = iris.corr() 2-8에서 했음
cmap = sns.diverging_palette(220, 10, as_cmap = True)

plt.figure(figsize=(11,9))
sns.heatmap(corr, cmap = cmap, vmax = 1.0, vmin = -1.0, center = 0, square  = True, linewidths= .5, cbar_kws = {'shrink' : .5})
plt.show()




## 2-10-4. 상관관계 시각화 - pairplot
sns.pairplot(iris, hue = 'species')
plt.show()