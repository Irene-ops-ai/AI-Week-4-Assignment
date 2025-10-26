#  🧠 Breast Cancer Classification using Random Forest
## 📘 Overview
This project uses the **Breast Cancer Wisconsin (Diagnostic) Dataset** to classify tumors as **malignant (M)** or **benign (B)** using a **Random Forest Classifier**.  
It demonstrates data preprocessing, model training, and evaluation using **accuracy** and **F1 score** metrics.

---
## 📂 Dataset
- **Source:** [Kaggle – Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)
- **Filename:** `data.csv`
- **Description:**  
  Each record represents a tumor cell sample with 30 numeric features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.

---
## ⚙️ Technologies Used
- Python 3.x  
- Pandas  
- Scikit-learn  
- Jupyter Notebook and VS Code  

---
## 🧩 Steps Performed
### 1. Data Preparation
- Loaded the dataset using `pandas`.
- Dropped irrelevant columns: `id` and `Unnamed: 32`.
- Encoded the target variable:  
  - Malignant = 1  
  - Benign = 0
 
### 2. Data Splitting
- Divided dataset into **80% training** and **20% testing** sets using `train_test_split`.

### 3. Model Training
- Implemented a **RandomForestClassifier** with 100 estimators and fixed random seed (`random_state=42`).
### 4. Evaluation
- Predicted on the test set.
- Computed the following metrics:
  - **Accuracy Score**
  - **F1 Score**

---
## 📊 Results
| Metric | Value |
|---------|--------|
| Accuracy | ~0.96  |
| F1 Score | ~0.95  |

The model achieved **high accuracy and F1 score**, showing strong performance in distinguishing between malignant and benign tumors.

---
