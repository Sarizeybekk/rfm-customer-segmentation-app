# Retail RFM Customer Segmentation

This project performs customer segmentation using the **Online Retail** dataset based on **RFM analysis** (Recency, Frequency, Monetary) and **KMeans clustering**. Additionally, it provides a **FastAPI** backend for model serving and a **simple web frontend** for easy interaction.

---

##  Project Features

- RFM Feature Engineering
- Customer Clustering using KMeans
- RESTful API with FastAPI
- Web Frontend for predictions

---

##  Project Structure

```
retail_customer_segmentation-app/
│
├── api/
│   ├── model/
│   │   ├── scaler.pkl
│   │   └── kmeans_model.pkl
│   ├── main.py
│   └── requirements.txt
│
└── frontend/
    ├── index.html
    ├── script.js
    └── style.css
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sarizeybekk/rfm-customer-segmentation-app.git
cd rfm-customer-segmentation-app
```

---

##  Backend (API) Setup

### Step 1: Navigate to the API Directory
```bash
cd api
```

### Step 2: Install the Dependencies
```bash
python -m venv env
```
# Windows:
```bash
.\env\Scripts\activate
```
# macOS/Linux :
```bash
source env/bin/activate
```

```bash
pip install -r requirements.txt
```

### Step 3: Start the FastAPI Server
```bash
uvicorn main:app --reload
```

The API will run on:
```
http://127.0.0.1:8000
```
You can test it via Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

##  Frontend Setup

### Step 1: Navigate to the Frontend Directory
```bash
cd frontend
```

### Step 2: Start a Simple HTTP Server
```bash
python -m http.server 3000
```

The frontend will be accessible at:
```
http://localhost:3000
```

**Note:** Ensure that the API server is running simultaneously.

---

##  How to Use

1. Open the web app at `http://localhost:3000`
2. Enter Recency, Frequency, and Monetary values.
3. Click **"Predict Segment"**.
4. The predicted customer segment will be displayed.

---

##  Project Purpose

Help businesses better understand their customers by grouping them into meaningful segments based on purchasing behavior. The project provides both an API and a user interface for quick and easy segment predictions.

---
![image](https://github.com/user-attachments/assets/fb4b4a3b-4b13-43bd-b810-11e553cc73a0)

![image](https://github.com/user-attachments/assets/bcd56612-1011-4331-b327-e0539cad9e17)

![image](https://github.com/user-attachments/assets/a825163a-7569-45f2-b598-652bdf6e8bf5)

