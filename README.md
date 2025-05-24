# 🛢️ Well log Analysis and Prediction using Machine learning


This repository hosts machine learning project focused on analyzing and predicting sonic well logs from petrophysical data:

- 🔍 **[Ensemble vs. Standalone Models](ensemble_vs_standalone/README.md)**  
  Comparison between ensemble methods (e.g., Random Forest, Gradient Boosting) and standalone regression models.

- 🔧 **Binary Prediction for Petrophysical Sonic Well Logs (DTC-DTS)**  
  Predicts compressional (DTC) and shear (DTS) sonic logs from other petrophysical measurements in the Volve field.

> 📘 *This README covers the Binary Prediction Project in detail.*

---

## 📌 Project Overview

Sonic logs are essential in petroleum engineering for:

- Identifying lithology and porosity  
- Mapping fluid types and natural fractures  
- Ensuring wellbore stability  
- Seismic calibration for hydrocarbon recovery  

This project utilizes machine learning (especially `ExtraTreesRegressor`) to predict DTC and DTS logs using the Volve dataset and `petrolib`.

---

## 🎯 Problem Statement

📍 **Goal**: Predict DTC and DTS from logs like GR, RT, RHOB, NPHI, etc., for enhanced subsurface characterization in the Volve field.

---

## 🗃️ Dataset

- 📌 **Source**: Volve field (7 wells)
- 📌 **Source**: Midland Basin (2 sections)
- 📦 **Format**: LAS files via `petrolib`
- 🧬 **Features**:
  - Gamma Ray (GR)
  - Resistivity (RT)
  - Density (RHOB)
  - Neutron Porosity Index (NPHI)
  - Compressional (DTC) & Shear Sonic (DTS)
- 🔢 **Size**: ~13,000 samples × 20 variables



---

## ⚙️ Data Preparation

| Step                     | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| ✅ Filtering             | Logs filtered by depth range                                                |
| 🚫 Missing Values        | Imputation or row-wise removal                                               |
| 🚨 Outliers              | Detected and managed                                                         |
| 📏 Standardization       | Features scaled for uniformity                                               |
| 🔗 Correlation Analysis  | Performed pre- and post-cleaning to check multicollinearity                 |

---

## 🧪 Methodology

- 🗂️ **Data Handling**: Read LAS files into Pandas using `petrolib`
- 🔍 **Preprocessing**: Depth filtering, NaN handling, outlier removal, standardization
- 🧠 **Model**: `ExtraTreesRegressor` (chosen for performance)
- ⚙️ **Tuning**: Hyperparameter optimization using `Optuna`
- 📏 **Metrics**:
  - R² Score
  - MSE, RMSE
  - MAE

---

## 🧮 Models Used

**Standalone Models**:
- Linear Regression
- Partial Least Squares

**Ensemble Models**:
- ✅ **ExtraTreesRegressor** (final model)
- Random Forest
- Gradient Boosted Trees

---

## 📊 Results Summary

### 📉 With Outliers

| Model                  | R²    | MSE   | RMSE  | MAE   |
|------------------------|-------|-------|-------|-------|
| Linear Regression      | 0.312 | 0.145 | 0.381 | 0.276 |
| ElasticNet Regression  | 0.346 | 0.138 | 0.371 | 0.265 |
| PLS Regression         | 0.357 | 0.135 | 0.367 | 0.269 |
| SVR                    | 0.284 | 0.151 | 0.389 | 0.285 |
| Random Forest          | 0.892 | 0.022 | 0.148 | 0.104 |
| **ExtraTrees**         | **0.922** | **0.016** | **0.126** | **0.089** |
| Gradient Boosted Trees | 0.874 | 0.026 | 0.161 | 0.112 |

### ✅ Without Outliers

| Model                  | R²    | MSE   | RMSE  | MAE   |
|------------------------|-------|-------|-------|-------|
| Linear Regression      | 0.326 | 0.142 | 0.377 | 0.273 |
| ElasticNet Regression  | 0.359 | 0.135 | 0.367 | 0.262 |
| PLS Regression         | 0.371 | 0.132 | 0.363 | 0.266 |
| SVR                    | 0.298 | 0.148 | 0.385 | 0.282 |
| Random Forest          | 0.905 | 0.020 | 0.141 | 0.100 |
| **ExtraTrees**         | **0.936** | **0.013** | **0.114** | **0.081** |
| Gradient Boosted Trees | 0.887 | 0.024 | 0.155 | 0.107 |

> 💡 **Insight**: `ExtraTreesRegressor` achieved **93.6% R²** (no outliers), confirming its robustness.

---

## 📈 Visualizations

- 📊 Correlation heatmaps (pre & post preprocessing)
- 🌀 Pair plots of key features
- 📉 DTC & DTS prediction plots vs. actual (see `binary_prediction/results/figures/`)

---

## 🧾 Conclusions

- ✅ Ensemble models outperform standalone for sonic log prediction
- ✅ Preprocessing improves accuracy (outlier removal + scaling)
- ✅ High predictive performance (R² > 0.92) on test data
- 🔭 Future Work: Explore DL models (e.g., LSTM, CNNs) and expand feature sets

---

## 🧰 Requirements
- Python 3.8+

- Key Libraries:
- pandas, numpy, scikit-learn, petrolib, optuna, matplotlib
- (see binary_prediction/requirements.txt)

## 📜 License
- Distributed under the MIT License.

---
