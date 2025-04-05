# Recommendation-System
Stock Recommendation System based on gold stocks in Malaysia 
# Financial Prediction Power BI Project

This project uses Power BI, Python, and machine learning to predict stock recommendations (Buy, Hold, Sell) based on financial metrics and price changes.

## Features
- Interactive Power BI dashboard with slicers for financial metrics and stock prices.
- Python script for prediction using a RandomForestClassifier.
- Pre-trained model and scaler included (`financial_model.pkl`, `scaler.pkl`).

## How to Use
1. Open the `.pbix` file in Power BI Desktop.
2. Adjust the slicers to input financial metrics and stock prices.
3. View the prediction (Buy, Hold, Sell) in the Python visual.

## Files
- `FinancialPrediction.pbix`: Power BI file.
- `predict.py`: Python script for prediction.
- `financial_model.pkl`: Pre-trained RandomForestClassifier model.
- `scaler.pkl`: Pre-trained scaler for feature scaling.

# Financial Stock Prediction with Power BI and Python

This project leverages Power BI and Python to predict stock recommendations (Buy, Hold, Sell) based on financial metrics and price changes. It combines interactive data visualization in Power BI with machine learning (using a RandomForestClassifier) to provide actionable insights for financial analysis.

## 📋 Project Overview

The project includes a Power BI dashboard where users can input financial metrics (e.g., Cost Ratio, FFO per Share) and stock prices (`close` and `new_close`) using slicers. A Python visual in Power BI then processes these inputs, applies a pre-trained machine learning model, and outputs a recommendation: Buy, Hold, or Sell.

### Key Features
- **Interactive Dashboard**: Use Power BI slicers to input financial metrics and stock prices.
- **Machine Learning Prediction**: A RandomForestClassifier model predicts stock recommendations based on financial metrics and the scaled return percentage.
- **Historical Data Visualization**: Visualize historical stock data (from the `dataset` table) using a line chart and table in Power BI.
- **Customizable Inputs**: Adjust financial metrics and price values to see how they impact the prediction.

## 📊 Screenshots

![Power BI Dashboard](screenshots/dashboard.png)  
*Interactive Power BI dashboard with slicers and prediction output.*

## 🚀 Getting Started

### Prerequisites
- **Power BI Desktop**: Download and install from [Microsoft’s website](https://powerbi.microsoft.com/en-us/downloads/).
- **Python**: Install Python (version 3.7 or higher) and the required libraries:
  - pandas
  - scikit-learn
  - matplotlib
  - Run the following command to install them:
