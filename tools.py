from docx import Document
import re


def write_to_docx(text):
    """Writing text to .docx"""
    print("Creating docx file...\n")

    doc = Document()

    # Başlıqları və mətni ayır
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue

        # Başlıq (tam sətir böyük hərflərlə və ulduzsuz)
        if re.fullmatch(r"\*{0,2}[A-ZƏÖÜĞÇŞİ\s]+", line):
            clean_title = line.replace("*", "").strip()
            doc.add_heading(clean_title, level=1)

        # Bullet point
        elif line.startswith("* "):
            bullet_text = line[2:].strip()
            # Qalın sözləri formatlamaq üçün
            paragraph = doc.add_paragraph(style='List Bullet')
            while "**" in bullet_text:
                before, bold, after = re.split(r"\*\*(.+?)\*\*", bullet_text, 1)
                paragraph.add_run(before)
                paragraph.add_run(bold).bold = True
                bullet_text = after
            paragraph.add_run(bullet_text)

        # Adi mətn
        else:
            paragraph = doc.add_paragraph()
            while "**" in line:
                before, bold, after = re.split(r"\*\*(.+?)\*\*", line, 1)
                paragraph.add_run(before)
                paragraph.add_run(bold).bold = True
                line = after
            paragraph.add_run(line)

    doc.save(r"../results/output.docx")

def write_to_txt(text):
    """Writing parsed text to .txt"""
    print("Creating txt file...\n")


    pass