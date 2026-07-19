from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
import numpy as np
import os
import time

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load trained model
model = load_model("model/eco_sort_model.keras")

# Class names
class_names = [
    "cardboard",
    "glass",
    "metal",
    "paper",
    "plastic",
    "trash"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filename = secure_filename(file.filename)

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(filepath)

    # Load Image
    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Prediction Time Start
    start_time = time.time()

    prediction = model.predict(img_array)

    # Prediction Time End
    end_time = time.time()
    prediction_time = round(end_time - start_time, 3)

    predicted_index = np.argmax(prediction)
    predicted_class = class_names[predicted_index]
    confidence = round(float(np.max(prediction)) * 100, 2)

    # -------------------------------
    # Waste Disposal Suggestions
    # -------------------------------
    suggestions = {
        "paper": "📄 Recycle this paper in the Paper Recycling Bin.",
        "plastic": "🥤 Clean and recycle in the Plastic Recycling Bin.",
        "glass": "🍾 Place in the Glass Recycling Bin.",
        "metal": "🥫 Send to a Metal Recycling Center.",
        "cardboard": "📦 Fold and recycle with paper products.",
        "trash": "🗑 Dispose in the General Waste Bin."
    }

    # -------------------------------
    # Recycling Tips
    # -------------------------------
    tips = {
        "paper": "♻ Paper can be recycled up to 7 times.",
        "plastic": "♻ Clean plastic before putting it in the recycling bin.",
        "glass": "♻ Glass can be recycled endlessly without losing quality.",
        "metal": "♻ Metal is one of the most valuable recyclable materials.",
        "cardboard": "♻ Flatten cardboard boxes before recycling.",
        "trash": "♻ Reduce waste whenever possible to help the environment."
    }

    # -------------------------------
    # Environmental Impact
    # -------------------------------
    impacts = {
        "paper": "🌳 Recycling paper saves trees, water and reduces landfill waste.",
        "plastic": "🐢 Recycling plastic protects marine life and reduces pollution.",
        "glass": "🏭 Recycling glass saves raw materials and energy.",
        "metal": "⚡ Recycling metal saves huge amounts of energy and natural resources.",
        "cardboard": "📦 Recycling cardboard helps reduce deforestation.",
        "trash": "🚮 Proper disposal keeps our surroundings clean and prevents pollution."
    }

    # -------------------------------
    # Estimated CO₂ Savings
    # -------------------------------
    co2_data = {
        "paper": "≈ 900 g CO₂ saved per kg recycled.",
        "plastic": "≈ 1500 g CO₂ saved per kg recycled.",
        "glass": "≈ 315 g CO₂ saved per kg recycled.",
        "metal": "≈ 9000 g CO₂ saved per kg recycled.",
        "cardboard": "≈ 700 g CO₂ saved per kg recycled.",
        "trash": "No significant CO₂ savings."
    }

    suggestion = suggestions.get(predicted_class, "Dispose responsibly.")
    tip = tips.get(predicted_class, "Help keep the environment clean.")
    impact = impacts.get(predicted_class, "Protect the environment.")
    co2_saved = co2_data.get(predicted_class, "N/A")

    return render_template(
    "result.html",
    prediction=predicted_class.title(),
    confidence=confidence,
    image_file=filename,
    suggestion=suggestion,
    tip=tip,
    impact=impact,
    co2_saved=co2_saved,
    prediction_time=prediction_time,
    model_name="CNN (Convolutional Neural Network)",
    dataset_name="TrashNet Dataset",
    input_size="224 × 224",
    total_classes="6",
    framework="TensorFlow + Flask"
)
if __name__ == "__main__":
    app.run(debug=True)