import json
import os
from pathlib import Path
import re
import time


def legal_pdf_setup():
    pdf_folder = "./Legal_pdf"
    pdf_links = ""

    for filename in sorted(os.listdir(pdf_folder)):
        if filename.endswith(".pdf"):
            name = filename.replace("-", " ").replace(".pdf", "").title()
            pdf_links += f'<li><a href="{pdf_folder}/{filename}" target="_blank">{name}</a></li>\n'

    with open("./template/Legal.template.html") as f:
        html = f.read()

    html = html.replace("{{PDF_SECTIONS}}", pdf_links)

    with open("Legal-Documentation.html", "w") as f:
        f.write(html)

    print("Legal links generated.")

def load_API():
    with open("Config.json") as f:
        config = json.load(f)
    pages = [
        ("./template/Calender.template.html", "Calender.html"),
        ("./template/Contact-Us.template.html", "Contact-Us.html"),
        ("./template/Newsletter-Sign-Up.template.html", "Newsletter-Sign-Up.html")
    ]
    for template_file, output_file in pages:
        with open(template_file) as f:
            html = f.read()
        for key, value in config.items():
            html = html.replace(f"{{{{{key}}}}}", value)
        with open(output_file, "w") as f:
            f.write(html)

    print("✅ All files generated with config.")

NEWSLETTER_DIR = "./Newsletter"
TEMPLATE_FILE = "./template/Newsletter.template.html"
OUTPUT_FILE = "Newsletter.html"
def format_button(news_id, label):
    return f'<button class="date-button" onclick="showNewsletter(\'{news_id}\')">{label}</button>'

def format_section(news_id, title, paragraphs):
    content = f'<h2>{title}</h2>\n'
    for paragraph in paragraphs:
        content += f'<p style="text-indent: 2em;">{paragraph}</p>\n'
    return f'<div id="{news_id}" class="newsletter">{content}</div>'

def newsletter_setup():
    buttons_html = ""
    sections_html = ""

    if not os.path.exists(NEWSLETTER_DIR):
        print(f"❌ The directory '{NEWSLETTER_DIR}' does not exist.")
        return
    for filename in sorted(os.listdir(NEWSLETTER_DIR)):
        if filename.endswith(".txt"):
            path = os.path.join(NEWSLETTER_DIR, filename)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                print(f"❌ Error reading file {filename}: {e}")
                continue
            parts = filename.replace(".txt", "").split("-")
            if len(parts) != 3:
                print(f"❌ Skipping {filename}, incorrect format.")
                continue

            year, month, label = parts[0], parts[1], parts[2].capitalize()
            news_id = f"{month}{year}"
            full_label = f"{label} {year}"
            lines = content.split("\n")
            title = lines[0].strip()  # First line as title
            paragraphs = []
            current_paragraph = []
            for line in lines[1:]:
                line = line.strip()
                if line:
                    current_paragraph.append(line)
                elif current_paragraph: 
                    paragraphs.append(" ".join(current_paragraph))
                    current_paragraph = []
            if current_paragraph: 
                paragraphs.append(" ".join(current_paragraph))


            buttons_html += format_button(news_id, full_label) + "\n"
            sections_html += format_section(news_id, title, paragraphs) + "\n\n"
    try:
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            template = f.read()
    except Exception as e:
        print(f"❌ Error reading template file: {e}")
        return
    result = template.replace("{{NEWSLETTER_BUTTONS}}", buttons_html)
    result = result.replace("{{NEWSLETTER_SECTIONS}}", sections_html)
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"✅ Generated {OUTPUT_FILE} with {len(buttons_html.splitlines())} newsletters.")
    except Exception as e:
        print(f"❌ Error writing to {OUTPUT_FILE}: {e}")

def main():
    print("Configuring...")
    time.sleep(1)
    try:
        load_API()
        legal_pdf_setup()
        newsletter_setup()
    except Exception as e:
        print("Failed. Error: ", e)

if __name__ == "__main__":
    main()