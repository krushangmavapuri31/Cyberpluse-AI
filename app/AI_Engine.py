import json
import ollama


def extract_json(text):
    start = text.find("{")
    end = text.rfind("}") + 1
    return text[start:end]


def analyze_article(article):
    prompt = f"""
    You are a cybersecurity analyst.

    Analyze this headline:
    {article['title']}

    Return ONLY valid JSON:

    {{
      "category": "...",
      "severity": "...",
      "summary": "...",
      "why_it_matters": "..."
    }}

    Categories:
    - Malware
    - Vulnerability
    - Breach
    - Web Security
    - Cryptography
    - Threat Intel

    Severity:
    - Low
    - Medium
    - High
    - Critical
    """

    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    output = response["message"]["content"]
    cleaned = extract_json(output)
    parsed = json.loads(cleaned)
    try:
        parsed = json.loads(output)
        return parsed
    except json.JSONDecodeError:
        print("Failed to parse JSON")
        return {
            "category": "Unknown",
            "severity": "Unknown",
            "summary": output,
            "why_it_matters": "Parsing failed"
        }
    

if __name__ == "__main__":
    article = {
        "title": "New Linux exploit enables root access"
    }

    result = analyze_article(article)
    print("\n===== Parsed Output =====")
    print("Category:", result["category"])
    print("Severity:", result["severity"])
    print("Summary:", result["summary"])
    print("Why:", result["why_it_matters"])