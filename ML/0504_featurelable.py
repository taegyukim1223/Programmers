# 학습데이터 예측데이터
# feature, lable 지도 학습에 나오는 개념
# 학습해야할 데이터를 feature라고 합니다.
# 예측해야할 것 : label
# 함수개념에서
# x = feature y = label 이라고 생각하자
# 학습을 위한 데이터에는 feature와 label이 모두 존재

# 과대적합 / 과소적합
# 머신러닝 학습시킬 때 best complexty까지 학습시켜야 한다.
# 학습을 위한 데이터를 validation set을 20% 준다.
# validation set으로 검증을 시키다가 validation error가 올라가면 학습을 멈춰준다.
# 학습할때 validation set에 섞여서 들어가면 절대 안됩니다.

# pre-processing (Garbage in, Garbage out!)
# 1.결측치 impouter
# 2.이상치
# 3.정규화
# 4.표준화
# 5.샘플링 over/under sampling
# 6.피처공학 

import numpy as np
import pandas as pd

train = pd.read_csv('https://bit.ly/fc-ml-titanic')
# print(train.head())
# print("hello")

# 전처리를 해줘야 한다.
# 학습 피쳐와 학습 레이블, 검증 피쳐와 검증 레이블로 나눠줘야 한다.
# 가장 먼저 피쳐와 레이블을 정의한다.
# 그다음 적잘한 비율로 train set 과 validation set을 나눠준다.

feature = [
'Pclass', 'Sex', 'Age', 'Fare'
]

label = [
    'Survived'
]

train[feature].head()


