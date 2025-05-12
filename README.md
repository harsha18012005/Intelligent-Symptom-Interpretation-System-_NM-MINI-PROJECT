# 🧠 Intelligent Symptom Interpretation System

## 📄 Project Abstract

The **Intelligent Symptom Interpretation System** is a healthcare-focused chatbot designed to bridge the gap between informal patient symptom descriptions and medically recognized conditions. Many patients express their symptoms using vague or non-clinical language, making it difficult for automated systems to interpret their health concerns accurately. This project leverages Natural Language Processing (NLP) techniques to clean and parse user input, identify key medical symptoms using Named Entity Recognition (NER), and map those symptoms to probable conditions through an ontology-based approach. The chatbot then provides a human-readable response suggesting possible conditions and encourages users to consult healthcare professionals. This system demonstrates a practical application of NLP in health informatics, enabling better triaging and digital symptom checking in clinical environments.


## 📘 Project Overview
The **Intelligent Symptom Interpretation System** is a chatbot designed for healthcare settings that interprets vague or indirect symptom descriptions from patients and maps them to probable medical conditions. This is especially useful in hospitals where patients may describe symptoms like “I feel dizzy when I get up” instead of using clinical terminology.

---

## 🎯 Objectives
- Interpret vague, non-clinical symptom inputs from users.
- Use NLP for preprocessing and Named Entity Recognition (NER).
- Map identified symptoms to medical conditions using a simple ontology.
- Provide a chatbot-style interface with helpful responses.

---

## 🧩 Components
| Module | Function |
|--------|----------|
| `app.py` | Main chatbot loop |
| `preprocessing.py` | Cleans and lemmatizes input |
| `ner_module.py` | Extracts medical-related symptoms |
| `ontology_mapper.py` | Maps symptoms to probable conditions |
| `chatbot_response.py` | Generates user-facing replies |

---

## 🗃 Example Input & Output

**User Input:**

I feel lightheaded sometimes, and my legs feel weak after walking.

**Chatbot Output:**

Based on your symptoms (lightheadedness, leg weakness), you might be experiencing one of the following conditions: Anemia, Orthostatic Hypotension, Peripheral Neuropathy, Multiple Sclerosis. Please consult a healthcare professional for an accurate diagnosis.


**Screenshot of the Chatbot Output:**
![Chatbot Output Example](screenshots/output_screenshot.png)


---

## 🛠 How to Run (Windows, macOS, Linux)

### ✅ Prerequisites
- Python 3.8+
- `spaCy` and English language model

---

### 🖥 Installation Steps (Windows)

1. **Install Python** (if not already installed) from [python.org](https://www.python.org/downloads/).
2. **Open Command Prompt** (press `Win + R`, type `cmd`, and press Enter).
3. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```
4. **Run the Chatbot**:
    ```bash
    python app.py
    ```

---

### 🍏 Installation Steps (macOS)

1. **Install Python** (if not already installed) from [python.org](https://www.python.org/downloads/).
2. **Open Terminal** (press `Cmd + Space`, type `Terminal`, and press Enter).
3. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```
4. **Run the Chatbot**:
    ```bash
    python app.py
    ```

---

### 🐧 Installation Steps (Linux)

1. **Install Python** (if not already installed) from [python.org](https://www.python.org/downloads/).
2. **Open Terminal**.
3. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```
4. **Run the Chatbot**:
    ```bash
    python app.py
    ```

---

## 📂 Files Included
- `app.py` – Main chatbot script
- `preprocessing.py` – Input cleaner
- `ner_module.py` – Extracts symptoms
- `ontology_mapper.py` – Symptom-condition mapping
- `chatbot_response.py` – Response builder
- `requirements.txt` – Python dependencies
- `README.md` – This file

---

---

## 🎞 Presentation Slides

You can view the project presentation here: [Intelligent_Symptom_Interpretation_System.pptx](Intelligent_Symptom_Interpretation_System.pptx)


---

## 🧠 Future Improvements
- Real medical NER using SciSpacy or Med7
- Use SNOMED or ICD-10 for advanced ontology mapping
- Deep learning model for better context understanding
- Web-based interface

---

## 👨‍⚕️ Disclaimer
This tool is **not a diagnostic system**. It is an academic project for demonstration purposes only. Always consult a healthcare professional for medical advice.

---

## 📜 License
MIT License (for academic use)
