import os
import re

LANGUAGES = {
    "eng": "Psychology & Neuroscience Blog",
    "fra": "Blog en psychologie et neurosciences",
    "deu": "Psychologie & Neurowissenschaften Blog",
    "spa": "Blog de Psicología y Neurociencias",
    "ita": "Blog di psicologia e neuroscienze",
    "por": "Blog de psicologia e neurociências",
    "nld": "Blog over psychologie en neurowetenschappen",
    "pol": "Blog o psychologii i neuronauce",
    "ron": "Blog de psihologie și neuroștiințe",
    "ces": "Blog o psychologii a neurovědách",
    "hun": "Pszichológiai és idegtudományi blog",
    "swe": "Blogg om psykologi och neurovetenskap",
    "ell": "Ιστολόγιο ψυχολογίας και νευροεπιστήμης",
    "bul": "Блог за психология и неврология",
    "dan": "Blog om psykologi og neurovidenskab",
    "fin": "Psykologian ja neurotieteen blogi",
    "slk": "Blog o psychológii a neurovede",
    "hrv": "Blog o psihologiji i neuroznanosti",
    "lit": "Psichologijos ir neuromokslų tinklaraštis",
    "lav": "Psiholoģijas un neirozinātnes blogs",
    "slv": "Blog o psihologiji in nevroznanosti",
    "est": "Psühholoogia ja neuroteaduse blogi",
    "gle": "Blag síceolaíochta agus néareolaíochta",
    "mlt": "Blog tal-psikoloġija u n-newroxxjenza",
    "ara": "مدونة في علم النفس وعلوم الأعصاب",
    "rus": "Блог по психологии и нейронаукам",
    "zho": "心理学与神经科学博客",
    "hin": "मनोविज्ञान और तंत्रिका विज्ञान ब्लॉग",
    "jpn": "心理学・神経科学ブログ",
    "heb": "בלוג בפסיכולוגיה ונוירולוגיה",
    "ind": "Blog psikologi dan ilmu saraf",
    "ben": "মনোবিজ্ঞান ও স্নায়ুবিজ্ঞান ব্লগ",
    "tur": "Psikoloji ve nörobilim blogu",
    "kor": "심리학 및 신경과학 블로그",
    "vie": "Blog tâm lý học và thần kinh học",
    "fas": "وبلاگ روانشناسی og علوم اعصاب",
}

for lang_code, lang_name in LANGUAGES.items():
    lang_dir = lang_code

    # Obtén todos los archivos HTML excepto index.html
    html_files = []
    if os.path.exists(lang_dir):
        for file in os.listdir(lang_dir):
            if file.endswith('.html') and file != 'index.html':
                html_files.append(file)

    html_files.sort()

    # Crea el HTML del índice
    html_content = f'''<!DOCTYPE html>
<html lang="{lang_code}" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{lang_name}</title>
    <style>
        body {{ font-family: sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px; background-color: #f6f6f6; }}
        h1 {{ color: #333; border-bottom: 2px solid #0645ad; padding-bottom: 10px; }}
        .article-list {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin-top: 20px; }}
        .article-card {{ background: white; padding: 15px; border: 1px solid #ddd; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .article-card:hover {{ box-shadow: 0 4px 8px rgba(0,0,0,0.2); transition: 0.3s; }}
        .article-card a {{ color: #0645ad; text-decoration: none; font-size: 16px; font-weight: bold; }}
        .article-card a:hover {{ text-decoration: underline; }}
        .back-link {{ margin-bottom: 20px; }}
        .back-link a {{ color: #0645ad; text-decoration: none; }}
    </style>
</head>
<body>
    <div class="back-link">
        <a href="../index.html">← Back to language selection</a>
    </div>
    <h1>{lang_name}</h1>
    <p>Total articles: {len(html_files)}</p>
    <div class="article-list">
'''

    for html_file in html_files:
        article_title = html_file.replace('.html', '').replace('-', ' ').title()
        html_content += f'''        <div class="article-card">
            <a href="{html_file}">{article_title}</a>
        </div>
'''

    html_content += '''    </div>
</body>
</html>'''

    # Guarda el índice
    index_path = os.path.join(lang_dir, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ Created {lang_code}/index.html with {len(html_files)} articles")

print("\\n✅ All language indexes created!")
