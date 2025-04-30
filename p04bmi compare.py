평균제곱오차(MSE): 0.617099
실제(BMI):23.96
실제(BMI):15.15
실제(BMI):27.60
실제(BMI):31.41
실제(BMI):29.10
from sklearn.model_selection import  train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3 ,  random_state=42)
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)