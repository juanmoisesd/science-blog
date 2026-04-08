import os
import json
import requests
from bs4 import BeautifulSoup
from jinja2 import Template
import xml.etree.ElementTree as ET
import time
from deep_translator import GoogleTranslator

# Simple cache for translations
translation_cache = {}

# Configuration
BASE_URL = "https://juanmoisesdelaserna.es/wp-json/wp/v2"
USERNAME = "DoctorenPsicologia"
PASSWORD = "dp&LVjv3Y%Vbn!C5pu)w)4"

LANGUAGES = {
    "eng": {"name": "Psychology & Neuroscience Blog", "lang": "en", "dir": "ltr"},
    "fra": {"name": "Blog en psychologie et neurosciences", "lang": "fr", "dir": "ltr"},
    "deu": {"name": "Psychologie & Neurowissenschaften Blog", "lang": "de", "dir": "ltr"},
    "spa": {"name": "Blog de Psicología y Neurociencias", "lang": "es", "dir": "ltr"},
    "ita": {"name": "Blog di psicologia e neuroscienze", "lang": "it", "dir": "ltr"},
    "por": {"name": "Blog de psicologia e neurociências", "lang": "pt", "dir": "ltr"},
    "nld": {"name": "Blog over psychologie en neurowetenschappen", "lang": "nl", "dir": "ltr"},
    "pol": {"name": "Blog o psychologii i neuronauce", "lang": "pl", "dir": "ltr"},
    "ron": {"name": "Blog de psihologie și neuroștiințe", "lang": "ro", "dir": "ltr"},
    "ces": {"name": "Blog o psychologii a neurovědách", "lang": "cs", "dir": "ltr"},
    "hun": {"name": "Pszichológiai és idegtudományi blog", "lang": "hu", "dir": "ltr"},
    "swe": {"name": "Blogg om psykologi och neurovetenskap", "lang": "sv", "dir": "ltr"},
    "ell": {"name": "Ιστολόγιο ψυχολογίας και νευροεπιστήμης", "lang": "el", "dir": "ltr"},
    "bul": {"name": "Блог за психология и неврология", "lang": "bg", "dir": "ltr"},
    "dan": {"name": "Blog om psykologi og neurovidenskab", "lang": "da", "dir": "ltr"},
    "fin": {"name": "Psykologian ja neurotieteen blogi", "lang": "fi", "dir": "ltr"},
    "slk": {"name": "Blog o psychológii a neurovede", "lang": "sk", "dir": "ltr"},
    "hrv": {"name": "Blog o psihologiji i neuroznanosti", "lang": "hr", "dir": "ltr"},
    "lit": {"name": "Psichologijos ir neuromokslų tinklaraštis", "lang": "lt", "dir": "ltr"},
    "lav": {"name": "Psiholoģijas un neirozinātnes blogs", "lang": "lv", "dir": "ltr"},
    "slv": {"name": "Blog o psihologiji in nevroznanosti", "lang": "sl", "dir": "ltr"},
    "est": {"name": "Psühholoogia ja neuroteaduse blogi", "lang": "et", "dir": "ltr"},
    "gle": {"name": "Blag síceolaíochta agus néareolaíochta", "lang": "ga", "dir": "ltr"},
    "mlt": {"name": "Blog tal-psikoloġija u n-newroxxjenza", "lang": "mt", "dir": "ltr"},
    "ara": {"name": "مدونة في علم النفس وعلوم الأعصاب", "lang": "ar", "dir": "rtl"},
    "rus": {"name": "Блог по психологии и нейронаукам", "lang": "ru", "dir": "ltr"},
    "zho": {"name": "心理学与神经科学博客", "lang": "zh", "dir": "ltr"},
    "hin": {"name": "मनोविज्ञान और तंत्रिका विज्ञान ब्लॉग", "lang": "hi", "dir": "ltr"},
    "jpn": {"name": "心理学・神経科学ブログ", "lang": "ja", "dir": "ltr"},
    "heb": {"name": "בלוג בפסיכולוגיה ונוירולוגיה", "lang": "he", "dir": "rtl"},
    "ind": {"name": "Blog psikologi dan ilmu saraf", "lang": "id", "dir": "ltr"},
    "ben": {"name": "মনোবিজ্ঞান ও স্নায়ুবিজ্ঞান ব্লগ", "lang": "bn", "dir": "ltr"},
    "tur": {"name": "Psikoloji ve nörobilim blogu", "lang": "tr", "dir": "ltr"},
    "kor": {"name": "심리학 및 신경과학 블로그", "lang": "ko", "dir": "ltr"},
    "vie": {"name": "Blog tâm lý học và thần kinh học", "lang": "vi", "dir": "ltr"},
    "fas": {"name": "وبلاگ روانشناسی og علوم اعصاب", "lang": "fa", "dir": "rtl"},
}

def translate_text(text, target_lang):
    """Translate text using GoogleTranslator."""
    if not text or target_lang == 'en':
        return text

    cache_key = (text, target_lang)
    if cache_key in translation_cache:
        return translation_cache[cache_key]

    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        if len(text) > 4500:
            # Simple chunking by paragraphs if too long
            parts = text.split('\n')
            translated_parts = []
            current_chunk = ""
            for part in parts:
                if len(current_chunk) + len(part) < 4500:
                    current_chunk += part + '\n'
                else:
                    translated_parts.append(translator.translate(current_chunk))
                    current_chunk = part + '\n'
            if current_chunk:
                translated_parts.append(translator.translate(current_chunk))
            result = "".join(translated_parts)
        else:
            result = translator.translate(text)

        translation_cache[cache_key] = result
        return result
    except Exception as e:
        print(f"Translation error for {target_lang}: {e}")
        return text

def fetch_content(endpoint):
    """Fetch all items from a WP REST API endpoint with pagination."""
    results = []
    page = 1
    while True:
        print(f"Fetching {endpoint} page {page}...")
        try:
            response = requests.get(
                f"{BASE_URL}/{endpoint}",
                params={"per_page": 100, "page": page},
                auth=(USERNAME, PASSWORD),
                timeout=30
            )
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            break

        if response.status_code != 200:
            print(f"Status code {response.status_code} for page {page}")
            break
        
        items = response.json()
        if not items:
            break
        
        results.extend(items)
        page += 1
        
        total_pages = int(response.headers.get('X-WP-TotalPages', 1))
        if page > total_pages:
            break
            
    return results

def save_raw_content():
    """Fetch and save posts and pages to raw_content/."""
    os.makedirs("raw_content", exist_ok=True)
    
    posts = fetch_content("posts")
    with open("raw_content/posts.json", "w", encoding="utf-8") as f:
        json.dump(posts, f)
        
    pages = fetch_content("pages")
    with open("raw_content/pages.json", "w", encoding="utf-8") as f:
        json.dump(pages, f)
    
    print(f"Saved {len(posts)} posts and {len(pages)} pages.")

def rewrite_content(item, lang_code, lang_info):
    """Rewrite content for a given item and language."""
    original_title = item.get('title', {}).get('rendered', '')
    target_lang = lang_info['lang']

    rewritten_title = translate_text(original_title, target_lang)
    
    desc_base = f"Latest scientific perspectives on {original_title}. Updated 2024 analysis in {lang_info['name']}."
    rewritten_description = translate_text(desc_base, target_lang)
    
    keywords_base = f"science, psychology, neuroscience, research, {original_title}"
    rewritten_keywords = translate_text(keywords_base, target_lang)

    tldr_en = [
        "Updated scientific analysis for 2024.",
        "Focus on psychology and neuroscience perspectives.",
        "Easy-to-read summary of complex research findings."
    ]
    tldr = [translate_text(point, target_lang) for point in tldr_en]
    
    # Extract original content and strip HTML
    original_content_html = item.get('content', {}).get('rendered', '')
    soup = BeautifulSoup(original_content_html, "html.parser")
    plain_text = soup.get_text(separator="\n")
    
    translated_body = translate_text(plain_text, target_lang)
    
    # Format translated body into paragraphs
    content = "".join([f"<p>{p}</p>" for p in translated_body.split('\n') if p.strip()])
    
    return {
        "title": rewritten_title,
        "description": rewritten_description,
        "keywords": rewritten_keywords,
        "tldr": tldr,
        "content": content,
        "headings": [],
        "date_published": item.get('date', '2024-01-01'),
        "slug": item.get('slug', 'index'),
        "lang": lang_info['lang'],
        "lang_code": lang_code,
        "dir": lang_info['dir'],
        "blog_name": lang_info['name'],
        "related": []
    }

def generate_index_pages(posts, pages, output_dir):
    """Generate index.html for root and for each language."""
    root_template = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Science Blog - Multilingual Portal</title>
        <style>
            body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            ul { list-style-type: none; padding: 0; }
            li { margin-bottom: 10px; }
            a { color: #0645ad; text-decoration: none; font-size: 1.2em; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>Science Blog</h1>
        <p>Select your language:</p>
        <ul>
            {% for code, info in languages.items() %}
            <li><a href="{{ code }}/index.html">{{ info.name }} ({{ code }})</a></li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """)
    with open(os.path.join(output_dir, "index.html"), "w") as f:
        f.write(root_template.render(languages=LANGUAGES))

    lang_template = Template("""
    <!DOCTYPE html>
    <html lang="{{ lang_code }}" dir="{{ dir }}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ blog_name }}</title>
        <style>
            body { font-family: sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px; background-color: #f6f6f6; }
            h1 { color: #333; border-bottom: 2px solid #0645ad; padding-bottom: 10px; }
            .article-list { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin-top: 20px; }
            .article-card { background: white; padding: 15px; border: 1px solid #ddd; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .article-card:hover { box-shadow: 0 4px 8px rgba(0,0,0,0.2); transition: 0.3s; }
            .article-card a { color: #0645ad; text-decoration: none; font-size: 16px; font-weight: bold; }
            .article-card a:hover { text-decoration: underline; }
            .back-link { margin-bottom: 20px; }
            .back-link a { color: #0645ad; text-decoration: none; }
        </style>
    </head>
    <body>
        <div class="back-link">
            <a href="../index.html">← Back to language selection</a>
        </div>
        <h1>{{ blog_name }}</h1>
        <div class="article-list">
            {% for item in items %}
            <div class="article-card">
                <h2><a href="{{ item.slug }}.html">{{ item.title }}</a></h2>
                <p>{{ item.description }}</p>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """)

    for lang_code, lang_info in LANGUAGES.items():
        lang_dir = os.path.join(output_dir, lang_code)
        os.makedirs(lang_dir, exist_ok=True)
        
        lang_items = []
        for item in (posts + pages):
             title = item.get('title', {}).get('rendered', '')
             translated_title = translate_text(title, lang_info['lang'])
             desc = f"Scientific update about {title}"
             translated_desc = translate_text(desc, lang_info['lang'])
             # Ensure the prefix itself is also translated if it missed it
             if "Scientific update about" in translated_desc:
                 translated_prefix = translate_text("Scientific update about", lang_info['lang'])
                 translated_desc = translated_desc.replace("Scientific update about", translated_prefix)
             lang_items.append({
                 "slug": item.get('slug'),
                 "title": translated_title,
                 "description": translated_desc
             })
             
        with open(os.path.join(lang_dir, "index.html"), "w") as f:
            f.write(lang_template.render(
                blog_name=lang_info['name'],
                lang_code=lang_code,
                dir=lang_info['dir'],
                items=lang_items
            ))

def generate_sitemap(all_urls, output_dir):
    """Generate sitemap.xml."""
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url in all_urls:
        url_el = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_el, "loc")
        loc.text = url
    
    # Prettify the output
    xmlstr = ET.tostring(urlset, encoding='utf-8')
    import xml.dom.minidom
    dom = xml.dom.minidom.parseString(xmlstr)
    with open(os.path.join(output_dir, "sitemap.xml"), "w") as f:
        f.write(dom.toprettyxml())

def generate_robots(output_dir):
    """Generate robots.txt."""
    with open(os.path.join(output_dir, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\n")
        f.write("Sitemap: https://juanmoisesd.github.io/science-blog/sitemap.xml\n")

def full_generation():
    """Execute full site generation."""
    output_dir = "."
    
    if not os.path.exists("raw_content/posts.json"):
        save_raw_content()
        
    with open("raw_content/posts.json", "r", encoding="utf-8") as f:
        posts = json.load(f)
    with open("raw_content/pages.json", "r", encoding="utf-8") as f:
        pages = json.load(f)
    
    article_template = Template("""
    <!DOCTYPE html>
    <html lang="{{ lang_code }}" dir="{{ dir }}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ title }} | {{ blog_name }}</title>
        <meta name="description" content="{{ description }}">
        <meta name="keywords" content="{{ keywords }}">
        <link rel="canonical" href="https://juanmoisesd.github.io/science-blog/{{ lang_code }}/{{ slug }}.html">
        <meta property="og:title" content="{{ title }}">
        <meta property="og:description" content="{{ description }}">
        <meta property="og:url" content="https://juanmoisesd.github.io/science-blog/{{ lang_code }}/{{ slug }}.html">
        <meta property="og:type" content="article">
        <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "Article",
          "headline": "{{ title }}",
          "description": "{{ description }}",
          "inLanguage": "{{ lang }}",
          "datePublished": "{{ date_published }}",
          "author": { "@type": "Person", "name": "Juan Moisés de la Serna" }
        }
        </script>
        <style>
            body { font-family: 'Linux Libertine', 'Georgia', serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f6f6f6; }
            article { background-color: #fff; padding: 40px; border: 1px solid #a7d7f9; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            h1 { border-bottom: 1px solid #a2a9b1; margin-bottom: 0.25em; padding: 0; font-family: 'Linux Libertine', 'Georgia', serif; font-weight: normal; }
            h2, h3 { border-bottom: 1px solid #a2a9b1; padding-bottom: 0.3em; margin-top: 1.5em; }
            p { margin: 0.5em 0 1em; }
            .tldr { background-color: #f8f9fa; border: 1px solid #eaecf0; padding: 15px; margin-bottom: 20px; }
            .toc { background-color: #f8f9fa; border: 1px solid #a2a9b1; padding: 10px; display: inline-block; margin-bottom: 20px; font-size: 0.9em; }
            .toc h2 { border: none; margin-top: 0; font-size: 1em; text-align: center; }
            ul, ol { margin-bottom: 1em; }
            a { color: #0645ad; text-decoration: none; }
            a:hover { text-decoration: underline; }
            .related-articles { margin-top: 40px; border-top: 2px solid #a2a9b1; padding-top: 20px; }
            @media (max-width: 600px) { body { padding: 10px; } article { padding: 20px; } }
        </style>
    </head>
    <body>
        <article>
            <h1>{{ title }}</h1>
            <div class="tldr">
                <strong>TL;DR:</strong>
                <ul>{% for point in tldr %}<li>{{ point }}</li>{% endfor %}</ul>
            </div>
            {% if headings %}
            <div class="toc">
                <h2>Contents</h2>
                <ul>{% for h in headings %}<li><a href="#{{ h.id }}">{{ h.text }}</a></li>{% endfor %}</ul>
            </div>
            {% endif %}
            <div class="content">{{ content|safe }}</div>
            <div class="related-articles">
                <h3>Related Articles</h3>
                <ul>{% for rel in related %}<li><a href="{{ rel.url }}">{{ rel.title }}</a></li>{% endfor %}</ul>
            </div>
        </article>
    </body>
    </html>
    """)
    
    all_urls = ["https://juanmoisesd.github.io/science-blog/index.html"]
    
    print("Generating index pages...")
    generate_index_pages(posts, pages, output_dir)
    
    for lang_code, lang_info in LANGUAGES.items():
        print(f"Generating content for {lang_code}...")
        lang_dir = os.path.join(output_dir, lang_code)
        
        for item in (posts + pages):
            rewritten = rewrite_content(item, lang_code, lang_info)
            html = article_template.render(**rewritten)
            
            filepath = os.path.join(lang_dir, f"{rewritten['slug']}.html")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            
            all_urls.append(f"https://juanmoisesd.github.io/science-blog/{lang_code}/{rewritten['slug']}.html")
            
    generate_sitemap(all_urls, output_dir)
    generate_robots(output_dir)
    print("Generation complete.")

if __name__ == "__main__":
    full_generation()
