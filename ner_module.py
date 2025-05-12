def extract_medical_entities(text):
    symptoms = []
    # Add more symptoms for better recognition
    if "lightheaded" in text or "dizzy" in text or "vertigo" in text:
        symptoms.append("lightheadedness")
    if "leg" in text and "weak" in text:
        symptoms.append("leg weakness")
    if "fatigued" in text or "tired" in text:
        symptoms.append("fatigue")
    if "headache" in text:
        symptoms.append("headache")
    if "shortness of breath" in text:
        symptoms.append("shortness of breath")
    if "chest pain" in text:
        symptoms.append("chest pain")
    if "nausea" in text:
        symptoms.append("nausea")
    if "sweating" in text:
        symptoms.append("sweating")
    if "palpitations" in text:
        symptoms.append("palpitations")
    if "coughing" in text:
        symptoms.append("coughing")
    if "abdominal pain" in text:
        symptoms.append("abdominal pain")
    if "faint" in text or "fainting" in text:
        symptoms.append("fainting")
    return symptoms
