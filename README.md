# 🧞‍♂️ SupportGenie - AI Customer Support Chatbot

### 🚀 Internship Task 3 | Machine Learning & NLP

**SupportGenie** is an intelligent customer support agent built using **Google Dialogflow** and **Python**. It is designed to handle automated customer queries, track orders, and provide instant responses using a Knowledge Base trained on real-world datasets.

🔗 **[Click Here to Chat Live with the Bot](https://console.dialogflow.com/api-client/demo/embedded/b361538b-1164-4f0e-8533-05b41e1fdbd7)**
*

---

## 📌 Project Overview
The goal of this project was to build a chatbot that can understand natural language and answer support questions using a hybrid approach:
1.  **Custom Intents:** For structured workflows like "Where is my package?" and collecting Order IDs.
2.  **Knowledge Base:** For handling general FAQs using a cleaned version of the **Kaggle Customer Support on Twitter Dataset**.

## 🛠️ Tech Stack
* **NLP Engine:** Google Dialogflow ES
* **Language:** Python (for Data Preprocessing)
* **Libraries:** `pandas`
* **Data Source:** Kaggle (`twcs.csv` - Customer Support on Twitter)
* **Deployment:** Web Integration via HTML/GitHub Pages

---

## ⚙️ Key Features
* **📦 Order Tracking:** Recognizes "Where is my package?" and asks for an Order ID.
* **🔢 Entity Extraction:** Automatically detects and validates Order Numbers (e.g., "12345").
* **🧠 Knowledge Base:** Trained on 2,000+ real support conversations to answer general queries.
* **💬 Small Talk:** Handles greetings (Welcome) and endings (Goodbye) naturally.
* **🌐 Real-Time Deployment:** Integrated into a custom web interface.

---

## 📂 Project Structure
* **`fix_kaggle.py`**: Python script used to clean the raw Kaggle CSV dataset and format it for Dialogflow.
