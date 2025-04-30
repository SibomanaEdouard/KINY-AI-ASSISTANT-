import random
import string
from itertools import combinations


# --- Step 1: Text Normalization ---
def normalize_text(text):
    text = text.strip().lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# --- Step 2: Intents and Patterns ---
INTENTS = {
    "greeting": {
        "patterns": ["muraho", "hello", "mwiriwe", "wiriweho"],
        "responses": [
            "Muraho neza! Nishimiye kukubona hano.",
            "Mwiriwe! Ufite ikibazo ushaka kumbaza?"
        ]
    },
    "ask_news": {
        "patterns": ["amakuru", "amakuru yawe", "amakuru y'umunsi", "amakuru y'icyumweru", "amakuru ya mugitondo", "amakuru ya nijoro"],
        "responses": [
            "Amakuru ni meza cyane, urakoze kubaza!",
            "Umunsi wagenze neza, ndashimira Imana. Wowe se?",
            "Icyumweru cyagenze neza rwose, wowe ho?",
            "Mugitondo wagenze neza cyane! Wowe uko byagenze?",
            "Nijoro wagenze neza cyane, ndabashimiye!",
        ]
    },
        "gratitude": {
        "patterns": ["urakoze", "murakoze", "murakoze cyane", "ndashimira", "turabashimira"],
        "responses": [
            "Murakoze cyane! Imana ibahe umugisha.",
            "Twishimiye ko dukorana neza. Urakoze cyane!"
        ]
    },
    "default": {
        "patterns": [],
        "responses": [
            "Ndababarira, sinashoboye kukumva neza. Ongera ugerageze.",
            "Sinabyumvise neza, ushobora gusubiramo ikibazo?",
        ]
    }
}

# --- Step 3: QA dictionary (your factual questions) ---
QA = {
    "ni iki gituma u rwanda rwitwa igihugu cy'imisozi igihumbi": 
        "Kubera ko gifite imisozi myinshi cyane itatse igihugu cyose.",
    "umusozi muremure mu rwanda ni uwuhe": 
        "Ni Karisimbi, ufite uburebure bwa metero 4,507.",
    "ni irihe shyamba rinini riboneka mu rwanda": 
        "Ni ishyamba rya Nyungwe.",
    "ni izihe ndimi zikoreshwa cyane mu rwanda": 
        "Ikinyarwanda, Icyongereza, Igifaransa, n'Igiswahili.",
    "ni iki cyihariye ku muco nyarwanda": 
        "Gukunda igihugu, gusabana, kubaha abakuru, nimigenzo nk'igisabo."
}

# --- Step 4: Build Keyword Map for QA ---
KEYWORD_MAP = {}
for question in QA:
    words = normalize_text(question).split()
    for n in [2, 3]:
        if len(words) >= n:
            for combo in combinations(words, n):
                key = " ".join(sorted(combo))
                if key not in KEYWORD_MAP:
                    KEYWORD_MAP[key] = []
                KEYWORD_MAP[key].append(question)

# --- Step 5: Matching Functions ---
def match_with_keywords(normalized_input):
    words = normalized_input.split()

    # Exact match
    for question in QA:
        if normalize_text(question) == normalized_input:
            return question

    # Try keyword combinations
    potential_matches = {}
    for n in [3, 2]:
        if len(words) >= n:
            for combo in combinations(words, n):
                key = " ".join(sorted(combo))
                if key in KEYWORD_MAP:
                    for question in KEYWORD_MAP[key]:
                        potential_matches[question] = potential_matches.get(question, 0) + n

    if potential_matches:
        return max(potential_matches.items(), key=lambda x: x[1])[0]

    return None

def match_intent(normalized_input):
    for intent, data in INTENTS.items():
        for pattern in data["patterns"]:
            if normalize_text(pattern) in normalized_input:
                return intent
    return "default"

# --- Step 6: Final Response Function ---
class Hypothesis:
    def __init__(self, text):
        self.text = text

def get_response(user_input):
    # Ensure user_input is a Hypothesis object
    if isinstance(user_input, Hypothesis):
        user_input = user_input.text  # Extract the text from the Hypothesis object

    normalized_input = normalize_text(user_input)

    # Step 1: Try matching QA first
    matched_question = match_with_keywords(normalized_input)
    if matched_question:
        return QA[matched_question]

    # Step 2: Try matching an Intent
    intent = match_intent(normalized_input)
    return random.choice(INTENTS[intent]["responses"])
