import pandas as pd 
import matplotlib.pyplot as plt 
import pickle 
import numpy as np 

from sklearn.model_selection import train_test_split 
import sklearn.metrics as metrics 
from sklearn.linear_model import LogisticRegression 
import seaborn as sns 
PATH = 'Crop_recommendation.csv'

data = pd.read_csv('Crop_recommendation.csv') 

data.head()
data.info() 

data.describe() 
data['label'].unique()
data['label'].value_counts()

plt.rcParams['figure.figsize'] = (10, 10) 
plt.rcParams['figure.dpi'] = 60

features = ['N', 'P', 'K', 'temperature', 
			'humidity', 'ph', 'rainfall'] 

for i, feat in enumerate(features): 
	plt.subplot(4, 2, i + 1) 
	sns.distplot(data[feat], color='greenyellow') 
	if i < 3: 
		plt.title(f'Ratio of {feat}', fontsize=12) 
	else: 
		plt.title(f'Distribution of {feat}', fontsize=12) 
	plt.tight_layout() 
	plt.grid()
sns.pairplot(data, hue='label') 
import seaborn as sns
import matplotlib.pyplot as plt

numeric_data = data.select_dtypes(include=[float, int])

fig, ax = plt.subplots(1, 1, figsize=(15, 9))
sns.heatmap(numeric_data.corr(), annot=True, cmap='viridis', ax=ax)
ax.set(xlabel='Features', ylabel='Features')

plt.title('Correlation between different features', fontsize=15, c='black')
plt.show()

features = data[['N', 'P', 'K', 'temperature','humidity', 'ph', 'rainfall']] 
labels = data['label'] 
X_train, X_test,Y_train, Y_test = train_test_split(features,labels,test_size=0.2,random_state=42) 
LogReg = LogisticRegression(random_state=42).fit(X_train, Y_train) 

predicted_values = LogReg.predict(X_test) 

accuracy = metrics.accuracy_score(Y_test, 
								predicted_values) 

print("Logistic Regression accuracy: ", accuracy)

print(metrics.classification_report(Y_test, predicted_values))

import pickle
with open('trained_model.pkl', 'wb') as file:
    pickle.dump(LogReg, file)
with open('trained_model.pkl', 'rb') as file:
    LogReg = pickle.load(file)
def predict_crop(input_data):
    input_df = pd.DataFrame([input_data], columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    prediction = LogReg.predict(input_df)
    return prediction[0]

def get_user_input():
    input_data = {
        'N': float(input("Enter value for Nitrogen (N): ")),
        'P': float(input("Enter value for Phosphorus (P): ")),
        'K': float(input("Enter value for Potassium (K): ")),
        'temperature': float(input("Enter value for Temperature: ")),
        'humidity': float(input("Enter value for Humidity: ")),
        'ph': float(input("Enter value for pH: ")),
        'rainfall': float(input("Enter value for Rainfall: "))
    }
    return input_data

user_input = get_user_input()

predicted_crop = predict_crop(user_input)
print(f"The recommended crop is: {predicted_crop}")

from sklearn.metrics import accuracy_score
predicted_values = LogReg.predict(X_test)
accuracy = accuracy_score(Y_test, predicted_values)

print("Logistic Regression accuracy: ", accuracy)

