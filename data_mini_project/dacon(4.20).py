# 데이콘 병원 개폐업 알아맞추기

import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score
import shap
import xgboost as xgb
import lightgbm as lgb
import seaborn as sns
import matplotlib.pyplot as plt


os.chdir('C:\\Users\\Admin\\Documents\\카카오톡 받은 파일\\데이콘(뼝원)')

train_prod_df = pd.read_csv('train.csv')
test_prod_df = pd.read_csv('test.csv')

# str로 바꿔야 replace가 먹힌다 그래서 바꾼다음에 ,를 없애주었다. 최종적으로 실수 값으로 변경

test_prod_df.employee1 = test_prod_df.employee1.astype('str').str.replace(",", "").astype('float')
test_prod_df.employee2 = test_prod_df.employee2.astype('str').str.replace(",", "").astype('float')

train_prod_df.employee1 = train_prod_df.employee1.astype('float')
train_prod_df.employee2 = train_prod_df.employee2.astype('float')
train_prod_df.OC= train_prod_df.OC.astype('str').str.replace(" ","")