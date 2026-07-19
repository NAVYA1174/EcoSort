# ♻️ EcoSortAI

## Smart Waste Classification Using Artificial Intelligence

EcoSortAI is an AI-powered web application that classifies waste images into different categories using a Convolutional Neural Network (CNN). The application also provides recycling guidance, environmental impact information, and waste disposal suggestions to encourage responsible waste management.

---

## Problem Statement

Improper waste segregation leads to pollution, inefficient recycling, and environmental damage. Many people are unsure which recycling bin to use for different types of waste.

EcoSortAI helps users identify waste correctly and provides recommendations for proper disposal.

---

## Solution

The user uploads an image of waste.

The AI model analyzes the image and predicts its category.

The system displays:

- Waste Category
- Confidence Score
- Waste Disposal Suggestion
- Recycling Tip
- Environmental Impact
- Estimated CO₂ Savings

---

## Features

- AI-based Waste Classification
- Image Upload
- Real-time Prediction
- Confidence Score
- Recycling Suggestions
- Environmental Impact Information
- CO₂ Savings Information
- Modern Flask Web Interface

---

## Waste Categories

- Cardboard
- Glass
- Metal
- Paper
- Plastic
- Trash

---

## Technologies Used

### Frontend

- HTML5
- CSS3

### Backend

- Flask
- Python

### Artificial Intelligence

- TensorFlow
- Keras
- NumPy
- Pillow

---

## Dataset

Dataset Used:

TrashNet Dataset

Contains six categories of recyclable waste images.

---

## Project Structure

```
EcoSortAI/
│
├── model/
│   └── eco_sort_model.keras
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── uploads/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```
git clone <repository-link>
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## Future Improvements

- Mobile Application
- Live Camera Detection
- Multi-language Support
- Smart Recycling Center Locator
- Barcode-based Waste Detection

---

## Team

Hack-ocalypse '26 Project

Project Name:

EcoSortAI

---

## License

This project is developed for educational and hackathon purposes.