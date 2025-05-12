# Simulated ontology-based mapping

def map_symptoms_to_conditions(symptoms):
    condition_map = {
        "lightheadedness": ["Anemia", "Orthostatic Hypotension"],
        "leg weakness": ["Peripheral Neuropathy", "Multiple Sclerosis"]
    }
    conditions = []
    for symptom in symptoms:
        conditions.extend(condition_map.get(symptom, []))
    return list(set(conditions))
