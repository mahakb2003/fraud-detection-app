import gradio as gr
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipeline.pkl")

def predict_fraud(transaction_type, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest):
    
    df = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    pred = model.predict(df)[0]
    return "🚨 FRAUD" if pred == 1 else "✔️ SAFE"

ui = gr.Interface(
    fn=predict_fraud,
    inputs=[
        gr.Dropdown(["PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN", "DEBIT"], label="Transaction Type"),
        gr.Number(label="Amount"),
        gr.Number(label="Old Balance (Sender)"),
        gr.Number(label="New Balance (Sender)"),
        gr.Number(label="Old Balance (Receiver)"),
        gr.Number(label="New Balance (Receiver)")
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="Fraud Detection System",
    description="Enter transaction details to check if it is fraud."
)

ui.launch()
