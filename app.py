from preprocessing import clean_and_tokenize
from ner_module import extract_medical_entities
from ontology_mapper import map_symptoms_to_conditions
from chatbot_response import generate_response

print("Welcome to the HealthBot! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! Stay healthy.")
        break

    # Step 1: Preprocessing
    cleaned_text = clean_and_tokenize(user_input)

    # Step 2: Named Entity Recognition
    symptoms = extract_medical_entities(cleaned_text)

    # Step 3: Ontology Mapping
    mapped_conditions = map_symptoms_to_conditions(symptoms)

    # Step 4: Generate Chatbot Response
    response = generate_response(symptoms, mapped_conditions)
    print("HealthBot:", response, "\n")
