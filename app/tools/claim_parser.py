import re

MEDICAL_KEYWORDS = [
    # Common symptoms
    "fever", "cough", "cold", "headache", "nausea", "vomiting", "diarrhea",
    "fatigue", "weakness", "pain", "bodyache", "sore throat", "dizziness",
    "breathlessness", "chills", "sweating", "rash", "itching", "swelling",

    # Common diseases
    "flu", "covid", "covid-19", "coronavirus", "infection", "malaria",
    "dengue", "typhoid", "pneumonia", "asthma", "diabetes", "cancer",
    "hypertension", "bp", "blood pressure", "cholesterol", "migraine",
    "arthritis", "tuberculosis", "tb", "jaundice",

    # Viral & bacterial
    "virus", "bacteria", "fungus", "fungal", "viral", "bacterial",
    "infection", "influenza", "hepatitis", "hiv",

    # Medicines
    "paracetamol", "acetaminophen", "dolo", "crocin", "ibuprofen",
    "antibiotic", "antiviral", "azithromycin", "amoxicillin",
    "antiseptic", "cetirizine", "dexamethasone", "vitamin", "zinc",
    "ORS", "painkiller", "analgesic",

    # Treatments
    "cure", "treat", "treatment", "therapy", "prevent", "reduce", "heal",
    "relief", "soothe",

    # Home remedies
    "turmeric", "haldi", "honey", "ginger", "adrak", "garlic", "lemon",
    "tea", "kadha", "ayurvedic", "herbal", "steam",

    # Body parts (for symptoms)
    "chest", "lungs", "stomach", "skin", "throat", "nose", "ear", "eye",

    # Emergency issues
    "heart attack", "stroke", "faint", "collapse", "bleeding",
    "burn", "allergy", "anaphylaxis",

    # Misc health
    "immunity", "weight loss", "diet", "exercise", "food poisoning",
]


def parse_claim(text: str):
    cleaned = text.lower().strip()

    found = [kw for kw in MEDICAL_KEYWORDS if kw in cleaned]

    backup = re.findall(r"\b[a-zA-Z]{5,}\b", cleaned)

    keywords = list(set(found + backup[:3]))

    return {"text": text, "keywords": keywords}
