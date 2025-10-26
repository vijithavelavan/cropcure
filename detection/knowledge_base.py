DISEASE_INFO = {
    'Healthy': {
        'symptoms': 'No visible symptoms. Plant appears healthy with normal green coloration.',
        'treatment': 'Continue regular care and monitoring. Maintain proper watering and fertilization.'
    },
    'Bacterial_Blight': {
        'symptoms': 'Water-soaked lesions on leaves, yellowing, and wilting. Lesions may have yellow halos.',
        'treatment': 'Apply copper-based bactericides. Remove infected plant parts. Improve air circulation.'
    },
    'Brown_Spot': {
        'symptoms': 'Brown circular spots with yellow halos on leaves. Spots may merge causing leaf death.',
        'treatment': 'Apply fungicides containing mancozeb or chlorothalonil. Remove infected debris.'
    },
    'Leaf_Blast': {
        'symptoms': 'Diamond-shaped lesions with gray centers and brown borders. Severe infections cause leaf death.',
        'treatment': 'Use fungicides like tricyclazole or propiconazole. Ensure proper field drainage.'
    },
    'Tungro': {
        'symptoms': 'Yellow-orange discoloration of leaves, stunted growth, and reduced tillering.',
        'treatment': 'Control green leafhopper vectors. Use resistant varieties. Remove infected plants.'
    }
}

def get_disease_info(disease_name):
    return DISEASE_INFO.get(disease_name, {
        'symptoms': 'Unknown disease symptoms.',
        'treatment': 'Consult agricultural expert for proper diagnosis and treatment.'
    })