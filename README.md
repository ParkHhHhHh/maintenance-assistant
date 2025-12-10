# Military Vehicle Maintenance Assistant (Mock Data)

This project models the maintenance workflow I supported during my military service as the **1st Vehicle Driver responsible for the battalion commander’s vehicle**.  
Because all operational data is confidential, I reconstructed the system using **mock datasets**, while preserving the **exact engineering logic, decision-making patterns, and maintenance reasoning** used in real operations.

This project demonstrates how domain-specific experience can be transformed into a **data-driven maintenance prediction system** using modern engineering tools.

---

## 🚀 Project Summary

Military vehicles operate under demanding conditions and must remain mission-ready at all times.  
As the driver of the battalion commander’s vehicle, I monitored:

- mileage progression  
- engine-hour accumulation  
- environmental stress (temperature, terrain)  
- upcoming maintenance requirements  
- vehicle fault history and severity  

This system re-creates those workflows through:

1. **Data preprocessing & cleaning**  
2. **Feature engineering inspired by real maintenance logic**  
3. **Machine learning prediction of maintenance intervals**  
4. **REST API for querying vehicle health**  
5. **Visualization dashboard for operational insights**

Although the data is simulated, the engineering reasoning reflects real mission requirements.

---

## 🛠 Tech Stack

- **Python** (pandas, numpy, matplotlib)
- **Machine Learning:** scikit-learn (RandomForest)
- **API:** FastAPI + Uvicorn
- **Model Persistence:** joblib
- **Visualization:** Jupyter Notebook dashboard
- **Architecture:** Modular, production-style project layout

---

## 📂 Project Structure

```powershell
maintenance-assistant/
├── data/
├── src/
├── api/
├── dashboard/
├── tests/
├── README.md
└── requirements.txt
```

---

## 🔍 Problem Definition

Traditional maintenance planning is **manual, reactive, and time-consuming**.  
Drivers and mechanics must track multiple variables to decide:

- When will this vehicle require maintenance next?  
- Which vehicles are at highest operational risk?  
- How do environmental factors accelerate wear?  

This project answers these questions by building a **predictive maintenance model** based on:

- mileage  
- engine usage  
- recent fault history  
- environmental stress  
- derived operational ratios  

---

## 🧠 Feature Engineering (Modeled After Real Military Reasoning)

Key engineered features:

### **`usage_ratio`**
Represents operational load:

usage_ratio = mileage / (engine_hours + 1)

Higher ratios often indicate higher stress per engine-hour.

---

### **`temp_stress`**
Binary encoding of vehicles exposed to high-temperature operation (> 32°C):

temp_stress = 1 if temperature > 32 else 0

High heat accelerates engine and fluid degradation.

---

These features replicate the real factors I used to assess vehicle readiness during service.

---

## 🤖 Model Training

A RandomForestRegressor predicts:

### **`days_until_maintenance`**

Training pipeline:
1. Load + merge datasets
2. Preprocess missing values
3. Generate engineered features
4. Split train/test sets
5. Train RandomForest model
6. Save as `model.pkl`

To train:

python src/train_model.py

---

## 🌐 REST API (FastAPI)

The API exposes real-time predictions based on vehicle status inputs:

### ▶ Start server

uvicorn api.main:app --reload

### ▶ Endpoints
- `GET /` – health check  
- `POST /predict` – returns predicted days until next maintenance

Swagger UI automatically available at:

http://127.0.0.1:8000/docs

---

## 📊 Dashboard (Jupyter Notebook)

The Jupyter dashboard (`dashboard/dashboard.ipynb`) includes:

- correlation heatmaps  
- mileage vs maintenance interval trends  
- usage_ratio analysis  
- temperature stress effect  
- model prediction samples  
- actual vs predicted comparison  

This serves as a **human-interpretable maintenance decision tool**, similar to what a driver or mechanic would reference.

---

## 📈 Example Insight

From the mock dataset:

- Vehicles with high **usage_ratio** tend to require maintenance sooner  
- High-temperature operation reduces maintenance intervals  
- The model provides consistent predictions aligned with manual reasoning patterns from field operations  

These insights reflect real maintenance logic used in mission settings.

---

## 🧪 Tests

Basic unit tests ensure:

- the model loads correctly  
- predictions return valid numeric outputs  
- feature engineering functions behave as expected

pytest tests/

---

## 🚧 Future Improvements

Planned enhancements include:

- Time-series modeling (LSTM or Prophet)
- Anomaly detection for sudden performance drops
- Web dashboard with real-time vehicle monitoring
- Integration of additional environmental data (humidity, terrain classification)
- Deployment as a containerized microservice

---

## 🎖 Personal Motivation

This system reflects how I approached my actual military responsibility:

As the battalion commander’s vehicle driver, I had to ensure that the vehicle  
was always operational, predictable, and ready for any mission—including long-distance movements, VIP transport, and night operations.

The mental framework I used in the field—tracking engine load, environmental conditions, and maintenance cycles—is directly represented in this engineering system.

It demonstrates my belief that **real-world experience can be elevated through data-driven engineering**, and shows the mindset I will bring to academic research and software engineering work.

---

## 📬 Contact

If you are reviewing this project as part of an application,  
I am happy to provide additional technical explanation or discuss the operational reasoning behind the maintenance logic.

Email: roy040315@gmail.com

GitHub: https://github.com/ParkHhHhHh

---

## ⭐ Final Note

Although this project uses mock data, it represents **a faithful engineering reconstruction** of  
how operational readiness is managed in a real military environment.

It demonstrates:

- technical depth  
- domain understanding  
- engineering structure  
- practical problem-solving  
- ability to convert field experience into software systems  

Exactly the qualities expected from a successful CS/DS/MIS transfer student.
