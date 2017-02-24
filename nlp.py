from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.tag import pos_tag_sents
from nltk.stem import *
from stemming.porter2 import stem
import re

user_input = "I have really big lump on my throat. It's swelling up and I don't know what to do."
clean_user_input = []

letters_only = re.sub("[^a-zA-Z]", " ", user_input)

lower_case = letters_only.lower()
words = lower_case.split()

words = [w for w in words if not w in stopwords.words("english")]

stemmer = PorterStemmer()

stemmed_words = [stem(word) for word in words]

symptoms = ['abdominal', 'pain', 'back', 'pain', 'chest', 'pain', 'earache', 'headache', 'chronic', 'pelvic', 'pain', 'toothache', 'ache', 'vaginal', 'pain', 'rectal', 'pain', 'dermatomal', 'pain', 'feel', 'chills', 'fever', 'paresthesia', 'numbness', 'tingling', 'electric', 'tweaks', 'light', 'headed', 'dizzy', 'dizzy', 'black', 'dizzy', 'room', 'spinning', 'around', 'mouth', 'dry', 'nauseated', 'sick', 'like', 'flu', 'like', 'vomit', 'short', 'breath', 'sleepy', 'sweaty', 'thirsty', 'tired', 'weak', 'breathe', 'normally', 'hear', 'normally', 'losing', 'hearing', 'sounds', 'loud', 'ringing', 'hissing', 'ears', 'move', 'one', 'side', 'arm', 'leg', 'pass', 'bowel', 'action', 'normally', 'pass', 'urine', 'normally', 'remember', 'normally', 'see', 'properly', 'blindness', 'blurred', 'vision', 'double', 'vision', 'sleep', 'normally', 'smell', 'things', 'normally', 'speak', 'normally', 'stop', 'passing', 'watery', 'bowel', 'actions', 'stop', 'scratching', 'stop', 'sweating', 'swallow', 'normally', 'taste', 'properly', 'walk', 'normally', 'write', 'normally', 'medical', 'symptoms', 'edit', 'list', 'incomplete', 'help', 'expanding', 'available', 'icd', 'codes', 'listed', 'codes', 'available', 'sign', 'symptom', 'code', 'underlying', 'condition', 'code', 'sign', 'used', 'general', 'cachexia', 'loss', 'appetite', 'weight', 'loss', 'weight', 'gain', 'dry', 'mouth', 'fatigue', 'malaise', 'asthenia', 'muscle', 'weakness', 'pyrexia', 'jaundice', 'pain', 'abdominal', 'pain', 'chest', 'pain', 'bruising', 'sx', 'epistaxis', 'tremor', 'convulsions', 'muscle', 'cramps', 'tinnitus', 'dizziness', 'vertigo', 'syncope', 'hypothermia', 'hyperthermia', 'discharge', 'bleeding', 'swelling', 'deformity', 'sweats', 'chills', 'shivering', 'neurological', 'psychological', 'acalculia', 'acrophobia', 'agnosia', 'agoraphobia', 'akathisia', 'akinesia', 'alexia', 'amusia', 'anhedonia', 'anomia', 'anosognosia', 'anxiety', 'apraxia', 'arachnophobia', 'ataxia', 'bradykinesia', 'cataplexy', 'chorea', 'claustrophobia', 'confusion', 'deliberate', 'self', 'harm', 'drug', 'overdose', 'depression', 'dysarthria', 'dysdiadochokinesia', 'dysgraphia', 'dystonia', 'euphoria', 'hallucination', 'headache', 'hemiballismus', 'ballismus', 'homicidal', 'ideation', 'insomnia', 'lhermitte', 'sign', 'electrical', 'sensation', 'shoots', 'back', 'arms', 'mania', 'paralysis', 'paranoia', 'persecution', 'paresthesia', 'phobia', 'see', 'list', 'phobias', 'prosopagnosia', 'sciatica', 'somnolence', 'suicidal', 'ideation', 'tic', 'tremor', 'ocular', 'amaurosis', 'fugax', 'amaurosis', 'blurred', 'vision', 'dalrymple', 'sign', 'double', 'vision', 'exophthalmos', 'mydriasis', 'miosis', 'nystagmus', 'gastrointestinal', 'anorexia', 'bloating', 'belching', 'blood', 'stool', 'melena', 'hematochezia', 'constipation', 'diarrhea', 'dysphagia', 'dyspepsia', 'flatulence', 'fecal', 'incontinence', 'haematemesis', 'nausea', 'odynophagia', 'proctalgia', 'fugax', 'pyrosis', 'rectal', 'malodor', 'steatorrhea', 'vomiting', 'cardiovascular', 'chest', 'pain', 'claudication', 'palpitation', 'tachycardia', 'bradycardia', 'arrhythmia', 'urologic', 'dysuria', 'hematuria', 'impotence', 'polyuria', 'retrograde', 'ejaculation', 'strangury', 'urinary', 'frequency', 'urinary', 'incontinence', 'urinary', 'retention', 'pulmonary', 'hypoventilation', 'hyperventilation', 'bradypnea', 'apnea', 'cough', 'dyspnea', 'hemoptysis', 'pleuritic', 'chest', 'pain', 'sputum', 'production', 'tachypnea', 'integumentary', 'abrasion', 'alopecia', 'anasarca', 'blister', 'edema', 'hirsutism', 'itching', 'laceration', 'paresthesia', 'rash', 'urticaria', 'obstetric', 'gynaecological', 'abnormal', 'vaginal', 'bleeding', 'bloody', 'show', 'preceding', 'onset', 'labour', 'painful', 'intercourse', 'pelvic', 'pain', 'infertility', 'labour', 'pains', 'vaginal', 'bleeding', 'early', 'pregnancy', 'miscarriage', 'vaginal', 'bleeding', 'late', 'pregnancy', 'vaginal', 'discharge', 'vaginismus']

stemmed_sympyoms = ['abdomin', 'pain', 'back', 'pain', 'chest', 'pain', 'earach', 'headach', 'chronic', 'pelvic', 'pain', 'toothach', 'ach', 'vagin', 'pain', 'rectal', 'pain', 'dermatom', 'pain', 'feel', 'chill', 'fever', 'paresthesia', 'numb', 'tingl', 'electr', 'tweak', 'light', 'head', 'dizzi', 'dizzi', 'black', 'dizzi', 'room', 'spin', 'around', 'mouth', 'dri', 'nauseat', 'sick', 'like', 'flu', 'like', 'vomit', 'short', 'breath', 'sleepi', 'sweati', 'thirsti', 'tire', 'weak', 'breath', 'normal', 'hear', 'normal', 'lose', 'hear', 'sound', 'loud', 'ring', 'hiss', 'ear', 'move', 'one', 'side', 'arm', 'leg', 'pass', 'bowel', 'action', 'normal', 'pass', 'urin', 'normal', 'rememb', 'normal', 'see', 'proper', 'blind', 'blur', 'vision', 'doubl', 'vision', 'sleep', 'normal', 'smell', 'thing', 'normal', 'speak', 'normal', 'stop', 'pass', 'wateri', 'bowel', 'action', 'stop', 'scratch', 'stop', 'sweat', 'swallow', 'normal', 'tast', 'proper', 'walk', 'normal', 'write', 'normal', 'medic', 'symptom', 'edit', 'list', 'incomplet', 'help', 'expand', 'avail', 'icd', 'code', 'list', 'code', 'avail', 'sign', 'symptom', 'code', 'under', 'condit', 'code', 'sign', 'use', 'general', 'cachexia', 'loss', 'appetit', 'weight', 'loss', 'weight', 'gain', 'dri', 'mouth', 'fatigu', 'malais', 'asthenia', 'muscl', 'weak', 'pyrexia', 'jaundic', 'pain', 'abdomin', 'pain', 'chest', 'pain', 'bruis', 'sx', 'epistaxi', 'tremor', 'convuls', 'muscl', 'cramp', 'tinnitus', 'dizzi', 'vertigo', 'syncop', 'hypothermia', 'hyperthermia', 'discharg', 'bleed', 'swell', 'deform', 'sweat', 'chill', 'shiver', 'neurolog', 'psycholog', 'acalculia', 'acrophobia', 'agnosia', 'agoraphobia', 'akathisia', 'akinesia', 'alexia', 'amusia', 'anhedonia', 'anomia', 'anosognosia', 'anxieti', 'apraxia', 'arachnophobia', 'ataxia', 'bradykinesia', 'cataplexi', 'chorea', 'claustrophobia', 'confus', 'deliber', 'self', 'harm', 'drug', 'overdos', 'depress', 'dysarthria', 'dysdiadochokinesia', 'dysgraphia', 'dystonia', 'euphoria', 'hallucin', 'headach', 'hemiballismus', 'ballismus', 'homicid', 'ideat', 'insomnia', 'lhermitt', 'sign', 'electr', 'sensat', 'shoot', 'back', 'arm', 'mania', 'paralysi', 'paranoia', 'persecut', 'paresthesia', 'phobia', 'see', 'list', 'phobia', 'prosopagnosia', 'sciatica', 'somnol', 'suicid', 'ideat', 'tic', 'tremor', 'ocular', 'amaurosi', 'fugax', 'amaurosi', 'blur', 'vision', 'dalrympl', 'sign', 'doubl', 'vision', 'exophthalmo', 'mydriasi', 'miosi', 'nystagmus', 'gastrointestin', 'anorexia', 'bloat', 'belch', 'blood', 'stool', 'melena', 'hematochezia', 'constip', 'diarrhea', 'dysphagia', 'dyspepsia', 'flatul', 'fecal', 'incontin', 'haematemesi', 'nausea', 'odynophagia', 'proctalgia', 'fugax', 'pyrosi', 'rectal', 'malodor', 'steatorrhea', 'vomit', 'cardiovascular', 'chest', 'pain', 'claudic', 'palpit', 'tachycardia', 'bradycardia', 'arrhythmia', 'urolog', 'dysuria', 'hematuria', 'impot', 'polyuria', 'retrograd', 'ejacul', 'stranguri', 'urinari', 'frequenc', 'urinari', 'incontin', 'urinari', 'retent', 'pulmonari', 'hypoventil', 'hyperventil', 'bradypnea', 'apnea', 'cough', 'dyspnea', 'hemoptysi', 'pleurit', 'chest', 'pain', 'sputum', 'product', 'tachypnea', 'integumentari', 'abras', 'alopecia', 'anasarca', 'blister', 'edema', 'hirsut', 'itch', 'lacer', 'paresthesia', 'rash', 'urticaria', 'obstetr', 'gynaecolog', 'abnorm', 'vagin', 'bleed', 'bloodi', 'show', 'preced', 'onset', 'labour', 'pain', 'intercours', 'pelvic', 'pain', 'infertil', 'labour', 'pain', 'vagin', 'bleed', 'earli', 'pregnanc', 'miscarriag', 'vagin', 'bleed', 'late', 'pregnanc', 'vagin', 'discharg', 'vaginismus']

no_duplicate_stemmed_symptoms = ['spot','sore', 'throat', 'hyperventil', 'code', 'help', 'edema', 'scratch', 'move', 'amusia', 'fecal', 'urinari', 'diarrhea', 'sleep', 'miscarriag', 'discharg', 'sleepi', 'convuls', 'onset', 'dyspnea', 'tire', 'gastrointestin', 'show', 'chorea', 'rash', 'sensat', 'vaginismus', 'hyperthermia', 'labour', 'black', 'under', 'stranguri', 'persecut', 'bradykinesia', 'dysphagia', 'ejacul', 'shoot', 'apnea', 'around', 'tinnitus', 'mydriasi', 'hiss', 'stop', 'dermatom', 'hypoventil', 'prosopagnosia', 'odynophagia', 'mania', 'vomit', 'walk', 'dyspepsia', 'bruis', 'loss', 'hematuria', 'like', 'rectal', 'edit', 'tachypnea', 'syncop', 'integumentari', 'list', 'cataplexi', 'malodor', 'pregnanc', 'lose', 'miosi', 'tic', 'alexia', 'side', 'vision', 'hallucin', 'vagin', 'flatul', 'anomia', 'weight', 'hemiballismus', 'back', 'infertil', 'sign', 'dysuria', 'see', 'paralysi', 'cachexia', 'ballismus', 'pass', 'proper', 'sciatica', 'arm', 'agoraphobia', 'depress', 'vertigo', 'paresthesia', 'constip', 'obstetr', 'stool', 'intercours', 'icd', 'earli', 'blur', 'claustrophobia', 'condit', 'gynaecolog', 'overdos', 'arrhythmia', 'sweati', 'ocular', 'acalculia', 'leg', 'late', 'asthenia', 'weak', 'akinesia', 'abras', 'tremor', 'impot', 'cough', 'bleed', 'anorexia', 'dysarthria', 'akathisia', 'abdomin', 'nausea', 'ach', 'paranoia', 'drug', 'malais', 'dri', 'thing', 'frequenc', 'sweat', 'confus', 'action', 'swallow', 'loud', 'blind', 'dalrympl', 'acrophobia', 'harm', 'hypothermia', 'claudic', 'feel', 'tweak', 'pulmonari', 'cramp', 'one', 'chronic', 'phobia', 'fatigu', 'urolog', 'ataxia', 'ring', 'urticaria', 'speak', 'urin', 'avail', 'use', 'earach', 'doubl', 'sputum', 'suicid', 'euphoria', 'breath', 'shiver', 'electr', 'nauseat', 'lacer', 'tachycardia', 'hemoptysi', 'headach', 'head', 'alopecia', 'bowel', 'muscl', 'deliber', 'fugax', 'sx', 'hear', 'gain', 'rememb', 'palpit', 'ear', 'spin', 'symptom', 'chill', 'sound', 'room', 'anosognosia', 'bloat', 'bradypnea', 'flu', 'proctalgia', 'anxieti', 'haematemesi', 'jaundic', 'neurolog', 'anasarca', 'hirsut', 'psycholog', 'retent', 'exophthalmo', 'retrograd', 'hematochezia', 'dizzi', 'cardiovascular', 'pelvic', 'general', 'dysgraphia', 'incomplet', 'anhedonia', 'amaurosi', 'thirsti', 'somnol', 'pyrosi', 'apraxia', 'pleurit', 'self', 'medic', 'deform', 'nystagmus', 'write', 'chest', 'preced', 'sick', 'belch', 'polyuria', 'appetit', 'lhermitt', 'smell', 'tingl', 'product', 'fever', 'pain', 'itch', 'normal', 'insomnia', 'swell', 'steatorrhea', 'wateri', 'dysdiadochokinesia', 'mouth', 'blood', 'numb', 'toothach', 'blister', 'expand', 'incontin', 'short', 'light', 'pyrexia', 'arachnophobia', 'bloodi', 'homicid', 'epistaxi', 'abnorm', 'dystonia', 'melena', 'bradycardia', 'tast', 'ideat', 'agnosia']

disease_symptoms = {"Chicken Pox":['blister', 'scab', 'ulcer', 'spot', 'fatigu', 'fever', 'appetit', 'headach', 'itch', 'swell'], "Goitre": ['lump', 'swell', 'coughing', 'heartbeat', 'breath', 'throat']}

actual_symptoms = set(stemmed_words).intersection(no_duplicate_stemmed_symptoms)

final_symptoms = list(set(disease_symptoms["Chicken Pox"]).intersection(actual_symptoms))

maxNum = 0
final_disease = ""

for disease in disease_symptoms:
    list_of_symptoms = list(set(disease_symptoms[disease]).intersection(actual_symptoms))
    if maxNum > len(list_of_symptoms):
        pass
    else:
        final_disease = disease
        maxNum = len(list_of_symptoms)

print(final_disease)
