# Titanic Survival Predictor

Web app yang memprediksi peluang selamat penumpang Titanic berdasarkan input user.

**Use case:** Membantu memahami faktor-faktor yang mempengaruhi survival rate penumpang Titanic melalui ML model yang interaktif.

## Live Demo

🚀 [https://huggingface.co/spaces/AdsyaDev/titanic-survival-predictor]

## Tech Stack

- Python, scikit-learn (Logistic Regression)
- Streamlit (web app)
- Pandas, NumPy (data processing)
- Matplotlib, Seaborn (EDA visualization)

## Model Performance

- **Accuracy:** 81%
- **Algorithm:** Logistic Regression
- **Features:** Pclass, Sex, Age, SibSp, Parch, Fare

## Key Findings (EDA)

- Wanita memiliki survival rate jauh lebih tinggi dari pria
- Penumpang kelas 1 lebih banyak yang selamat
- Harga tiket berkorelasi positif dengan peluang selamat

## Cara Menjalankan Lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Struktur Project

```
project-01/
├── data/               # Dataset Titanic
├── notebooks/          # EDA dan model training
├── model/              # Saved model (.pkl)
├── outputs/            # Grafik EDA
├── src/                # Training scripts
├── app.py              # Streamlit app
└── requirements.txt
```

## Visualisasi EDA

![EDA Charts](outputs/eda-charts.png)
