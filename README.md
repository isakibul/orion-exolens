# ExoLense

## Project Summary
ExoLense is a predictive tool designed to identify potential exoplanets based on user-provided astronomical data. Using machine learning models, it processes features like orbital period, transit duration, and transit depth to predict the likelihood of a planet’s presence. This project addresses the challenge of efficiently analyzing large datasets of celestial observations and aids researchers in prioritizing candidate exoplanets for further study.

---

## Project Details
**What it does / How it works:**  
ExoLense takes user input of various planetary and stellar features, processes them using a trained machine learning model, and provides a prediction on the likelihood of an exoplanet.  

**Benefits:**  
- Speeds up identification of potential exoplanets.  
- Provides a user-friendly interface for researchers and astronomy enthusiasts.  
- Reduces manual computation and increases accuracy using ML predictions.  

**Intended Impact:**  
The project helps in early detection of exoplanets, contributing to space exploration research and providing a tool for educational purposes.

**Creativity & Considerations:**  
- Interactive web interface for easy data input.  
- User Input Guide to ensure accurate predictions.  
- Focused on usability and scientific relevance.  

---

## Tools & Technologies
- **Google Docs** – Documentation  
- **VSCode** – Code editor  
- **Google Chrome** – Testing web interface  
- **GitHub** – Version control  

**Programming & Libraries:**  
- Python  
- Flask  
- Pandas  
- Scikit-learn  
- Joblib  

---


## User Input Guide
ExoLense provides a guide for users to correctly input feature data to ensure accurate predictions. Each feature includes descriptive hints, expected units, and example values to prevent incorrect input.

---

## Installation & Setup

1. Clone the repository:
git clone https://github.com/isakibul/orion-exolens.git

2. Clone the repository:
cd orion-exolens

3. Set up a Python virtual environment:
python -m venv venv

4. Activate the virtual environment:<br>
Linux/macOS: source venv/bin/activate<br>
Windows: venv\Scripts\activate

5. Upgrade pip (optional)<br>
pip install --upgrade pip

6. Install project dependencies<br>
pip install -r requirements.txt

7. Run the Flask application<br>
python app.py

8. Open your browser then navigate to: http://127.0.0.1:5000

