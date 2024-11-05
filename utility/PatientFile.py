class PatientTranslations:
    def translate_allergies(allergy_string):
        translations = {
            'localAnesthetic': 'داروی بی‌حسی موضعی',
            'painkiller': 'مسکن',
            'specialFood': "غذای خاص",
            'antibioticsAllergy': "انواع آنتی‌بیوتیک‌ها",
        }

        allergies = allergy_string.split('-')

        
        translated_allergies = []
        for allergy in allergies:
            translated_allergies.append(translations.get(allergy, allergy)) 

        return ' - '.join(translated_allergies)

    def translate_diseases(disease_string):
        translations = {
            'gastrointestinal': 'بیماری‌های گوارشی',
            'thyroidDisease': 'تیروئید',
            'MS': "ام اس",
            'respiratory': "بیماری‌های تنفسی",
            'blood': "بیماری‌های خونی",
            'herpes': "ابتلا به تبخال",
            'hepatitis': "هپاتیت",
            'cancer': "سرطان",
            'kidney': "بیماری‌های کلیوی",
            'hormone': "اختلالات هورمونی",
        }

        diseases = disease_string.split('-')
        
        translated_diseases = []
        for disease in diseases:
            translated_diseases.append(translations.get(disease, disease)) 

        return ' - '.join(translated_diseases)

    def translate_medications(medication_string):
        translations = {
            'contraceptive': 'داروی ضد بارداری',
            'aspirin': 'آسپرین',
            'roaccutane': 'راکوتان',
            'sedative': 'آرام‌بخش‌ها',
            'heart': 'داروی قلبی',
            'anticoagulants': 'ضد انعقادها',
            'insulin': 'انسولین',
            'thyroidMedicine': 'تیروئید',
            'antibioticsMedicine': 'آنتی‌بیوتیک‌ها',
            'Minoxidil': 'ماینوکسیدیل',
        }

        medications = medication_string.split('-')

        
        translated_medications = []
        for medication in medications:
            translated_medications.append(translations.get(medication, medication)) 

        return ' - '.join(translated_medications)