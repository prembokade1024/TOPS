"""

1. data set : salary 
2. feature selection 
3. train split 
4. feature scale  :fit_transform(),transform()
5. linear model : linear model , model.fit() .model.predict,r2score = r2(y_test,predict)
6. ridge : ridge model(alpha=1) , model.fit() .model.predict,r2score = r2(y_test,predict)\
7. lasso : lasso model(alpha=100) , model.fit() .model.predict,r2score = r2(y_test,predict)\
8. elasticnet :elasticnet model(alpha=100,l1_ratio=.5) , model.fit() .model.predict,r2score = r2(y_test,predict)

| Alpha | Effect                                        |
| ----- | --------------------------------------------- |
| 0     | No regularization (same as Linear Regression) |
| 0.001 | Very little regularization                    |
| 0.01  | Small regularization                          |
| 0.1   | Mild regularization                           |
| 1     | Default in most examples                      |
| 10    | Strong regularization                         |
| 100   | Very strong regularization                    |
| 1000  | May cause underfitting                        |

The alpha and l1_ratio values are hyperparameters, meaning there is no fixed value. They are usually chosen by cross-validation


| Model      | Recommended Value         |
| ---------- | ------------------------- |
| Ridge      | alpha=1                 	 |
| Lasso      | alpha=0.1 or alpha=1 	 |
| ElasticNet | alpha=1, l1_ratio=0.5 	 |
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler 

# read excel 
df =pd.read_excel("salary_regularization (1).xlsx")

# features selection :
X=df.drop(['Salary'],axis=1)
y=df['Salary']

#spilt data:
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
 
# scale data :
scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train,y_train)
X_test_scale = scaler.transform(X_test)

# model :
lr = LinearRegression()
lr.fit(X_train_scale,y_train)
prediction_1 =lr.predict(X_test_scale)

# model lasso :

ls = Lasso(alpha=100)
ls.fit(X_train_scale,y_train)
prediction_2 =ls.predict(X_test_scale)

# model ridge :

ri = Ridge(alpha=1)
ri.fit(X_train_scale,y_train)
prediction_3 =ri.predict(X_test_scale)

# model elasticnet :
El = ElasticNet(alpha=1,l1_ratio=0.5)  # 50 % lasso and 50 % ridge
El.fit(X_train_scale,y_train)
prediction_4 =El.predict(X_test_scale)

# print r2score :
r2_lr = r2_score(y_test, prediction_1)
r2_lasso = r2_score(y_test, prediction_2)
r2_ridge = r2_score(y_test, prediction_3)
r2_elasticnet = r2_score(y_test, prediction_4) 

# compare :
comparison_df = pd.DataFrame({
    'Model':['Linear Regression','Lasso(L1)','Ridge','ElasticNet(L1 + L2)'],
    'R2_Score':[r2_lr,r2_lasso,r2_ridge,r2_elasticnet]
})

print(comparison_df.sort_values(by='R2 Score', ascending=False).to_string(index=False))
print("\n")
# conculsion : 
