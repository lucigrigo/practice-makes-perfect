# importing libraries
import numpy as np
import pandas as pd

# importing datasets
train_dataset = pd.read_csv("train.csv")
test_dataset = pd.read_csv("test.csv")
y_test_dataset = pd.read_csv("gender_submission.csv")

# creating train/test x/y splits
x_train = train_dataset.iloc[:, [2, 5, 6, 7]]
y_train = train_dataset.iloc[:, 1]
x_test = test_dataset.iloc[:, [1, 4, 5, 6]]
y_test = y_test_dataset.iloc[:, 1]

# dealing with nan data
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
x_train_imp = imp.fit_transform(x_train)
x_test_imp = imp.fit_transform(x_test)

#from sklearn.preprocessing import OneHotEncoder
#ohc = OneHotEncoder(handle_unknown='ignore', categorical_features = [1])
#x_train[:, 4] = ohc.fit_transform(x_train[:, 4].reshape(-1, 1)).toarray()
#x_test = ohc.fit_transform(x_test[:, 3].reshape(-1, 1))

#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#x_train = sc.fit_transform(x_train)
#x_test = sc.fit_transform(x_test)

# training Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=1000, criterion='entropy',
                                    n_jobs=-1, warm_start='True')
classifier.fit(x_train_imp, y_train)

# predicting results
y_pred = classifier.predict(x_test_imp)

# visualising confusion matrix & computing accuracy score
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)