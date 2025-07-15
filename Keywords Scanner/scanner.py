# Resume Keyword Scanner 🔍 by Timmy

def load_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read().lower()

def load_keywords(path):
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip().lower() for line in file if line.strip()]

def scan_keywords(resume_text, keywords):
    found = []
    missing = []

    for keyword in keywords:
        if keyword in resume_text:
            found.append(keyword)
        else:
            missing.append(keyword)

    return found, missing

resume_text = load_file("resume.txt")
keywords = load_keywords("keywords.txt")
found, missing = scan_keywords(resume_text, keywords)

print("\n✅ Found Keywords:")
for word in found:
    print(f"  - {word}")

print("\n❌ Missing Keywords:")
for word in missing:
    print(f"  - {word}")
