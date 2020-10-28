# KAGGLE TITANIC COMPETITION
print(' --------------------- KAGGLE TITANIC COMPETITION  ---------------------')

# importing libraries
import numpy as np
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# importing datasets
train_dataset = pd.read_csv("train.csv")
test_dataset = pd.read_csv("test.csv")
y_test_dataset = pd.read_csv("gender_submission.csv")

# creating train/test and x/y splits
x_train = train_dataset.iloc[:, [4, 6, 7]].values
y_train = train_dataset.iloc[:, 1].values
x_test = test_dataset.iloc[:, [3, 5, 6]].values
y_test = y_test_dataset.iloc[:, 1].values

# labeling genders
ohenc = OneHotEncoder(handle_unknown = 'ignore')
genders = [['male', 0], ['female', 1]]
ohenc.fit(genders)
x_train[:, 0] = ohenc.transform(x_train[:, 0].reshape(-1, 1))

# dealing with nan data
# imp = SimpleImputer(missing_values=np.nan, strategy='mean')
# x_train_imp = imp.fit_transform(x_train)
# x_test_imp = imp.fit_transform(x_test)

# feature scaling
# sc = StandardScaler()
# x_train = sc.fit_transform(x_train)
# x_test = sc.fit_transform(x_test)

import sys
sys.exit()

# ----------------------------- RANDOM FOREST CLASSIFIER ---------------
# training using entropy criterion
rfc = RandomForestClassifier(n_estimators=1000, criterion='entropy', n_jobs=-1)
rfc.fit(x_train_imp, y_train)

# predicting results
y_pred_rfc = rfc.predict(x_test_imp)

# visualising confusion matrix & computing accuracy score
print('\nRandom Forest Classifier (entropy) results:')
print('confusion matrix = \n' + str(confusion_matrix(y_test, y_pred_rfc)))
print('accuracy = ' + str(accuracy_score(y_test, y_pred_rfc)))

# training using gini criterion
rfc2 = RandomForestClassifier(n_estimators=1000, criterion='gini', n_jobs=-1)
rfc2.fit(x_train_imp, y_train)

# predicting results
y_pred_rfc2 = rfc2.predict(x_test_imp)

# visualising confusion matrix & computing accuracy score
print('\nRandom Forest Classifier (gini) results:')
print('confusion matrix = \n' + str(confusion_matrix(y_test, y_pred_rfc2)))
print('accuracy = ' + str(accuracy_score(y_test, y_pred_rfc2)))

# ----------------------------- DECISION TREE CLASSIFIER ---------------
# training using entropy criterion
dtc = DecisionTreeClassifier(criterion = 'entropy')
dtc.fit(x_train_imp, y_train)

# predicting results
y_pred_dtc = dtc.predict(x_test_imp)

# visualising confusion matrix & computing accuracy score
print('\nDecision Tree Classifier (entropy) results:')
print('confusion matrix = \n' + str(confusion_matrix(y_test, y_pred_dtc)))
print('accuracy = ' + str(accuracy_score(y_test, y_pred_dtc)))

# training using gini criterion
dtc2 = DecisionTreeClassifier(criterion = 'gini')
dtc2.fit(x_train_imp, y_train)

# predicting results
y_pred_dtc2 = dtc2.predict(x_test_imp)

# visualising confusion matrix & computing accuracy score
print('\nDecision Tree Classifier (gini) results:')
print('confusion matrix = \n' + str(confusion_matrix(y_test, y_pred_dtc2)))
print('accuracy = ' + str(accuracy_score(y_test, y_pred_dtc2)))

# ----------------------------- K-NN CLASSIFIER ---------------
# training
knn = KNeighborsClassifier(n_neighbors = 10, metric = 'manhattan')
knn.fit(x_train_imp, y_train)

# Predicting the test set results
y_pred_knn = knn.predict(x_test_imp)

# visualising confusion matrix & computing accuracy score
print('\nK-Nearest Neighbours results:')
print('confusion matrix = \n' + str(confusion_matrix(y_test, y_pred_knn)))
print('accuracy = ' + str(accuracy_score(y_test, y_pred_knn)))

# ----------------------------- K-NN CLASSIFIER ---------------


print('\n------------------------------------------------------------------------\n')