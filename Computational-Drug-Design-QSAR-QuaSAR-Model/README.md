# Computational Drug Design: QSAR / QuaSAR Model for log EC50 Prediction

## Project Overview
This project was completed as part of the Computational Drug Design course. The project focused on developing a QSAR / QuaSAR model to predict biological activity using log EC50 values and molecular descriptors.

## Objectives
- To build a QSAR model for predicting biological activity.
- To use molecular descriptors for activity prediction.
- To evaluate model performance using RMSE and R² values.
- To interpret the relationship between descriptors and predicted log EC50.
- To identify important molecular features affecting compound potency.

## Model Type
- QuaSAR Model
- Partial Least Squares (PLS) regression
- Activity field: log EC50

## Dataset and Model Details
- Observations: 141
- Descriptors: 5
- Components used: 5
- RMSE: 0.46999
- R²: 0.71818
- Cross-validated RMSE: 0.49669
- Cross-validated R²: 0.68557

## Molecular Descriptors Used
- SMR_VSA6
- Q_VSA_HYD
- SlogP_VSA7
- PEOE_VSA+1
- PEOE_VSA-1

## QSAR Equation
log EC50 =
-3.94166
+ 0.00671 × SMR_VSA6
+ 0.01197 × Q_VSA_HYD
- 0.00520 × SlogP_VSA7
- 0.01440 × PEOE_VSA+1
+ 0.01059 × PEOE_VSA-1

## Key Interpretation
The model suggests that molecular potency is influenced by hydrophobicity, polarizability, lipophilicity, and partial charge-related descriptors. Positive charge-related and lipophilic features may improve potency, while some hydrophobic/polarizability and negative charge-related features may reduce potency.

## Tools and Concepts Used
- MOE
- QuaSAR modelling
- QSAR analysis
- Partial Least Squares regression
- Molecular descriptors
- log EC50 prediction
- RMSE and R² evaluation
- Cross-validation

## Skills Demonstrated
- Computational drug design
- QSAR modelling
- Molecular descriptor interpretation
- Regression-based activity prediction
- Model evaluation
- Scientific interpretation of drug design models
