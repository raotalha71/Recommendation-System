# train_model.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

# Step 1: Load the dataset
# Replace with the path to your CSV file
data = pd.read_csv('dataset.csv')

# Step 2: Select features and target
features = ['Cost Ratio (%)', 'Debt-Service Coverage Ratio', 'FFO per Share', 
            'FY Dividend Yield (%)', 'Gearing Ratio (%)', 'NAV per Share', 
            'Net Operating Income', 'Net Stock Issuance', 'PB Ratio', 'Return Percentage']
X = data[features]
y = data['Buy_Hold_Sell']

# Step 3: Scale the features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=features)

# Step 4: Split the data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Evaluate the model
y_pred = model.predict(X_test)
print("Model Evaluation:")
print(classification_report(y_test, y_pred))

# Step 7: Check feature importance
feature_importance = pd.DataFrame({
    'Feature': features,
    'Importance': model.feature_importances_
})
print("\nFeature Importance:")
print(feature_importance.sort_values(by='Importance', ascending=False))

# Step 8: Save the model and scaler
with open('financial_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("\nModel and scaler saved successfully!")