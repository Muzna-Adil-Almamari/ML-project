# Real Estate Price Prediction Project 
##  Objectives
The objective of this project is to build a predictive model to estimate property prices using real estate data collected from public APIs. It includes data collection, cleaning, integration, modeling, and optionally exposing APIs for cleaning and prediction.

---
## API Used
- **ATTOM API** – Property details,  and sales  data

---
## Data Collection and Cleaning Process

- Data was collected via API calls and saved as raw CSV files.
- Core cleaning steps included:
  - Filtering relevant columns for modeling.
  - Handling missing values with group-based imputation methods.
  - Encoding categorical features using one-hot encoding.
  - Scaling numerical features where applicable.
  - remove outliers

---
## Modeling Approach and Results

- Multiple regression models were trained and evaluated:
  - Linear Regression
  - Polynomial Regression (degree 2)
  - Lasso Regression
  - Ridge Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - Support Vector Regression (SVR)
 
  
- Model performance was compared using metrics such as MAE, MSE, RMSE, and R-squared (R2).
- The **Random Forest Regressor** provided the best predictive performance with the highest R2 score.

---
## Model Performance Summary (R² Score)

| Model               | R² Score | Notes                                                                 |
|---------------------|----------|-----------------------------------------------------------------------|
| **Linear Regression**     | 0.46     | Baseline model; underfitting.                                         |
| **Polynomial Regression** | 0.52     | Slightly better, but may overfit and is harder to generalize.         |
| **Lasso Regression**      | 0.46     | Performs like linear; regularization didn’t improve.                  |
| **Ridge Regression**      | 0.46     | Same as linear; doesn’t capture nonlinearity.                         |
| **Decision Tree**         | 0.62     | Good improvement; captures non-linear patterns.                       |
| **Random Forest**         | 0.68     | ✅ **Best performer overall**. Robust and generalizes well.           |
| **SVM Regressor**         | 0.47     | Low score; not optimal for this data or needs tuning.                |

