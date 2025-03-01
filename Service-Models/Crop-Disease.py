python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("Fertilizer.csv")

# Encoding categorical variables (State & City)
le_state = LabelEncoder()
le_city = LabelEncoder()
df['State'] = le_state.fit_transform(df['State'])
df['City'] = le_city.fit_transform(df['City'])

# Features and label
X = df[['N', 'P', 'K', 'State', 'City']]
y = df['Fertilizer']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Example prediction
sample = [[50, 30, 20, le_state.transform(["Tamil Nadu"])[0], le_city.transform(["Chennai"])[0]]]
print("Predicted Fertilizer:", model.predict(sample))