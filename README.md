# 🔍 Fraud Detection System  
### Machine Learning Model for Real-Time Transaction Risk Scoring

![UI Screenshot](https://github.com/mahakb2003/fraud-detection-app/blob/main/Screenshot%20(31).png?raw=true)

---

## 1. Overview  
This project presents a production-ready **Fraud Detection System** designed to identify high-risk financial transactions in real time.  

It is built as an end-to-end pipeline that integrates:

- A fully engineered **machine learning pipeline**  
- **Imbalanced data handling** using SMOTE  
- **Automated preprocessing** within the model  
- An easy-to-use **interactive UI** for business teams  

The system addresses a real-world banking challenge:  
**detecting fraudulent transfers without blocking genuine customers.**

---

## 2. Business Problem  
Financial institutions and fintech platforms face challenges like:

- Extremely **imbalanced datasets** (fraud < 0.2%)  
- Requirement for **instant decision-making**  
- Huge financial loss due to **false negatives**  
- Maintaining a smooth **user experience**  

This project simulates real BFSI risk conditions and shows how ML reduces fraud losses.

---

## 3. Solution Architecture  

### **Data Processing**
- Performed exploratory data analysis  
- Standardized numeric features  
- OneHotEncoded the categorical "type" column  
- Applied **SMOTE** to balance fraud cases  

### **Machine Learning Pipeline**
A reproducible ML pipeline built using:

- StandardScaler  
- OneHotEncoder (drop="first")  
- SMOTE  
- Logistic Regression with balanced class weights  

The final pipeline is exported using Joblib for deployment.

---

## 4. Model Performance  

Trained on **1.9M+ real transaction records**, the model achieved:

### **Classification Metrics**
| Metric | Non-Fraud (0) | Fraud (1) |
|--------|-----------------|-----------|
| Precision | 1.00 | 0.02 |
| Recall | 0.95 | 0.95 |
| F1 Score | 0.97 | 0.04 |

### **Confusion Matrix**
[[1804159, 102163],
[ 122, 2342]]


### **Interpretation**
- High recall for fraud cases (95%) — essential for risk systems  
- Low precision is expected due to extreme imbalance  
- Business benefit: **almost all fraud attempts are detected**  

---

## 5. User Interface  
A clean, business-friendly UI built for:

- Fraud analysts  
- Risk management teams  
- Product managers  
- Operations teams  

Users enter transaction details and get instant ML predictions.

---

## 6. Running the Project  

### **Install dependencies**
```bash
pip install -r requirements.txt
 
Run the application
python app.py


The interface opens automatically at:
➡ http://127.0.0.1:7860/

7. Project Structure
├── app.py                       # User interface
├── fraud_detection.py           # Training pipeline
├── fraud_detection_pipeline.pkl # Final ML model
├── AIML Dataset.csv             # Dataset
├── main.ipynb                   # EDA + training
├── requirements.txt             # Dependencies
└── README.md                    # Documentation

8. Skills Demonstrated
Technical Skills

Machine Learning (Scikit-Learn)

Working with imbalanced data (SMOTE)

Pipeline engineering

EDA and feature engineering

Joblib model serialization

ML deployment

Business Skills

Understanding fraud risk frameworks

Cost-sensitive fraud modeling

Operational decision-making in BFSI

Creating tools for analysts and business users

9. About the Author

Mahak Bisht
Data Analyst & Machine Learning Enthusiast

Focused on building scalable, real-world, business-driven ML solutions.
🔗 GitHub: https://github.com/mahakb2003





