# -*- coding: utf-8 -*-
"""Creditcard fraud detection .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13_KAxBfDk40hJGm3lheii38XQxikI4Iy
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df=pd.read_csv('creditcard.csv')

df.head()

df.shape

df = df.drop_duplicates()

df.shape

df.info()

df.describe()

fraudlent_transaction = df[df['Class'] == 1]
legimate_transaction = df[df['Class'] == 0]

fraudlent_transaction.shape

legimate_transaction.shape

plt.figure(figsize=(10,6))
sns.countplot(data=df,x='Class')
plt.title('Distribution of fraudlent against legimate transactions')
plt.xticks((1,0),labels=['fraudlent_transaction','legimate_transaction'])
plt.show()

sns.histplot(data=df,x='Time',kde=True)
plt.title('Distribuion of time')
plt.show()

plt.figure(figsize=(10,5))
sns.heatmap(data=df.corr(),annot=False,linewidths=0.5)

plt.show()

normal = df[df['Class']==0]
fraud = df[df['Class']==1]

normal.shape

fraud.shape

X = df.drop(columns='Class')
y = df['Amount']

X

y

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df=pd.read_csv('creditcard.csv')

X = df.drop('Class', axis=1)
y = df['Class']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

isolation_forest = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
isolation_forest.fit(X_test)

# Predict outliers/anomalies
y_pred_test = isolation_forest.predict(X_test)

y_pred_test[y_pred_test == 1] = 0
y_pred_test[y_pred_test == -1] = 1

print("Testing Classification Report:")
print(classification_report(y_test, y_pred_test))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

df=pd.read_csv('creditcard.csv')

X = df.drop('Class', axis=1)
y = df['Class']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Logistic Regression
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_test, y_test)

# Decision Tree
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_test, y_test)

# Predictions
y_pred_log_reg = log_reg.predict(X_test)
y_pred_decision_tree = decision_tree.predict(X_test)

# Evaluation
print("Logistic Regression Classification Report:")
print(classification_report(y_test, y_pred_log_reg))

print("\nDecision Tree Classification Report:")
print(classification_report(y_test, y_pred_decision_tree))

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Load the fraud detection model (e.g., Isolation Forest)
model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)

# Function to preprocess and predict fraud for incoming transactions
def detect_fraud(transaction):
    # Preprocess the incoming transaction (e.g., scale the features)
    transaction_scaled = scaler.transform([transaction])
    is_fraudulent = model.predict(transaction_scaled)

scaler = StandardScaler()

incoming_transactions = [
    [100.23, 25.6, 0.5],   # Example transaction 1
    [200.56, 40.8, 0.8],   # Example transaction 2
    [500.0, 10.0, 1.2]
]

for transaction in incoming_transactions:
    detect_fraud(transaction)

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from queue import Queue
import threading

def detect_fraud(transaction, model, scaler):
    # Preprocess the incoming transaction (e.g., scale the features)
    transaction_scaled = scaler.transform([transaction])

def process_transactions(queue, model, scaler):
    while True:
        transaction = queue.get()
        detect_fraud(transaction, model, scaler)
        queue.task_done()

model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)

scaler = StandardScaler()

transaction_queue = Queue()

processing_thread = threading.Thread(target=process_transactions, args=(transaction_queue, model, scaler))
processing_thread.daemon = True
processing_thread.start()

incoming_transactions = [
    [100.23, 25.6, 0.5],   #  transaction 1
    [200.56, 40.8, 0.8],   #  transaction 2
    [500.0, 10.0, 1.2]     #  transaction 3
]

for transaction in incoming_transactions:
    transaction_queue.put(transaction)

transaction_queue.join()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df=pd.read_csv('creditcard.csv')

df['Amount_high'] = (df['Amount'] > df['Amount'].mean() + 2 * df['Amount'].std()).astype(int)
df['Amount_low'] = (df['Amount'] < df['Amount'].mean() - 2 * df['Amount'].std()).astype(int)

X = df.drop(['Class'], axis=1)
y = df['Class']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_test, y_test)

y_pred = rf_clf.predict(X_test)

print(classification_report(y_test, y_pred))

