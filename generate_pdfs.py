import os
import re
from markdown_pdf import Section, MarkdownPdf

docs = [
    "Project_Documentation.md",
    "SRS.md",
    "Testing_Report.md",
    "Technical_Debt_Plan.md",
    "User_Manual.md"
]

base_dir = r"h:\Urban-Heat-Prediction-main\StudentID_UrbanHeat_Accra"

for doc in docs:
    md_path = os.path.join(base_dir, doc)
    pdf_path = os.path.join(base_dir, doc.replace(".md", ".pdf"))
    
    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Remove markdown internal links but keep text
        content = re.sub(r'\[([^\]]+)\]\(#[^\)]+\)', r'\1', content)
            
        pdf = MarkdownPdf()
        pdf.add_section(Section(content))
        pdf.save(pdf_path)
        print(f"Generated {pdf_path}")
    else:
        print(f"File not found: {md_path}")
