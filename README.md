# Flipkart Product Review Sentiment Analysis

## Project Overview
This project implements a sentiment analysis system for Flipkart product reviews.  
The application classifies user-entered reviews as **Positive** or **Negative** and is deployed as a web application using Streamlit on **AWS EC2**.

The focus of this project is to build a complete end-to-end pipeline from data preprocessing and model training to real-time deployment.

---

## Objective
- Analyze Flipkart product reviews using machine learning
- Classify reviews into **Positive** or **Negative** sentiment
- Deploy a working web application accessible over the internet

---

## Dataset
- Dataset provided by the internship team
- Product: **YONEX MAVIS 350 Nylon Shuttle**
- File used: `reviews_badminton.csv`

### Data Description
Each review contains:
- Review Title
- Review Text
- Rating (1–5)

### Sentiment Labeling Logic
Sentiment labels were derived from ratings as follows:
- **Rating ≥ 4** → Positive (1)
- **Rating ≤ 2** → Negative (0)
- **Rating = 3** → Neutral (excluded from training)

---

## Data Preprocessing
- Combined review title and review text
- Converted text to lowercase
- Removed special characters and unnecessary text such as “READ MORE”
- Normalized extra spaces

Only essential preprocessing steps were used to keep the model simple and deployment stable.

---

## Model Development
- **Feature Extraction:** TF-IDF Vectorization  
  - Unigrams and bigrams
  - Limited feature size for efficiency
- **Model Used:** Logistic Regression
- **Evaluation Metric:** F1-score

The trained vectorizer and model were saved together as a pickle file for deployment.

---

## Web Application
- Framework: **Streamlit**
- Users can enter a product review
- The application predicts whether the review sentiment is **Positive** or **Negative**
- The trained model is loaded from a pickle file for real-time inference

---

## Deployment
- Platform: **AWS EC2**
- Operating System: Ubuntu
- Python virtual environment used for dependency management

### Live Application URL
[Live URL](http://13.61.35.157:8501)


---

## Project Structure
```text
flipkart_sentiment_project/
│
├── reviews_badminton.csv
├── train_sentiment.ipynb
├── sentiment_model.pkl
├── sentiment_app.py
├── requirements.txt
└── README.md
```

How to Run Locally

### 1. Install dependencies:
pip install -r requirements.txt

### 2. Run the Streamlit application:
streamlit run sentiment_app.py


## Conclusion
This project demonstrates a complete machine learning workflow, including data preprocessing, model training and evaluation, model serialization, web application development, and cloud deployment on AWS. The deployed application successfully performs real-time sentiment analysis on Flipkart product reviews.



