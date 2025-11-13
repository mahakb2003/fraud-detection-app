# Fraud Detection System  
### Machine Learning Model for Real-Time Transaction Risk Scoring

[UI Screenshot](https://github.com/mahakb2003/fraud-detection-app/blob/main/Screenshot%20(31).png?raw=true)
## 1. Overview  
This project demonstrates the development of a production-oriented **Fraud Detection System** designed to identify high-risk financial transactions in real time. It is is an end-to-end **Fraud Detection System** .
It combines **data science, machine learning, business reasoning, and interactive UI** to demonstrate how modern financial platforms mitigate risk.
 
It focuses on solving a core business challenge in digital banking and payment systems:  
**reducing financial loss by detecting fraudulent transfers without disrupting legitimate user activity.**

The system integrates:
- A scalable machine learning pipeline  
- Rigorous handling of imbalanced transaction data  
- A clean and intuitive Gradio interface for business teams  

---

## 2. Business Context  
Fraud detection is one of the most critical components in the financial ecosystem.  
Organizations face challenges such as:

- Extremely **imbalanced datasets** (fraud < 0.2%)  
- The need for **instant decisioning**  
- Balancing **customer experience** with **risk mitigation**  
- Preventing **false negatives**, which directly translate to monetary loss  

This project replicates a real scenario faced by banks, wallets, and fintech companies, where ML models must operate reliably at scale while supporting business decisions.

---

## 3. Solution Design  

### 3.1 Data Processing  
- Executed comprehensive exploratory analysis  
- Cleaned and standardized numerical features  
- Encoded categorical attributes using OneHotEncoding  
- Used **SMOTE** to address severe class imbalance  

### 3.2 Machine Learning Model  
A Scikit-Learn pipeline was designed with:

- **StandardScaler** for numerical scaling  
- **OneHotEncoder** for categorical features  
- **Logistic Regression** with balanced class weighting  
- Reproducible training and evaluation structure  

The model was serialized using Joblib for deployment readiness.

---

## 4. Model Performance (Real Metrics) 


The model was trained on **1.9M+ transactions**.

### Classification Metrics  
The model was trained and evaluated on **1.9M+ real transactions**.

| Metric | Non-Fraud (0) | Fraud (1) |
|--------|-----------------|--------------|
| Precision | 1.00 | 0.02 |
| Recall | 0.95 | 0.95 |
| F1 Score | 0.97 | 0.04 |

### Confusion Matrix  
[[1804159, 102163],
[ 122, 2342]]


### Interpretation  
- **High recall (95%) for fraud cases**, which is essential in operational environments  
- Ensures the system catches nearly all fraudulent transactions  
- Precision is expectedly low due to extreme class imbalance — typical in BFSI fraud scenarios  

This demonstrates a practical, risk-averse strategy aligned with real business needs.

---

## 5. User Interface (Gradio)  
A streamlined interface was developed for:

- Fraud analysts  
- Risk teams  
- Product managers  
- Operations teams  

The UI allows users to input transaction details and instantly receive a fraud risk prediction.  
This bridges the gap between data science and decision-making teams by providing a simple, reliable front end.

---

## 6. Running the Project  

### Install dependencies  


pip install -r requirements.txt


### Start the application  


python app.py


The interface opens automatically or runs on `http://127.0.0.1:7860`.

---

## 7. Project Structure  


├── app.py # Gradio UI
├── fraud_detection.py # ML pipeline and training script
├── fraud_detection_pipeline.pkl # Serialized model
├── AIML Dataset.csv # Dataset
├── main.ipynb # Exploratory analysis and training
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 8. Key Skills Demonstrated  

### Technical  
- Machine Learning (Scikit-Learn)  
- Imbalanced Data Handling (SMOTE)  
- Pipeline Engineering  
- Model Deployment using Gradio  
- Exploratory Data Analysis  
- Serialization and reproducibility  

### Business  
- Understanding of fraud risk frameworks  
- Cost-sensitive modeling  
- Decision support systems for BFSI  
- Translating ML outputs into business insights  

---

## 9. About the Author  
**Mahak Bisht**  
Data Analyst & Machine Learning Enthusiast  
Focused on building reliable, scalable, business-driven data solutions.  
GitHub: https://github.com/mahakb2003
