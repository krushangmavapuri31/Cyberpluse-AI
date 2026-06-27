KEYWORDS =  [
    "cve",
    "zero-day",
    "exploit",
    "malware",
    "ransomware",
    "phishing",
    "breach",
    "vulnerability",
    "ddos",
    "botnet",
    "sql injection",
    "xss",
    "authentication bypass",
    "privilege escalation",
    "remote code execution",
    "cryptography",
    "encryption",
    "ethical hacking",
    "bug bounty",
    "penetration testing",
    "ctf",
    "attack",
    "hacker",
    "backdoor",
    "trojan",
    "apt"
]

# Filter Function

def is_relevant(article):
    title = article["title"].lower()

    for keywords in KEYWORDS:
        if keywords in title:
            print(f"Matched: {keywords} -> {title}")
            return True
        
    return False
    

# Filter List of Articles

def filter_articles(articles):
    filtered = []
    
    for article in articles:
        if is_relevant(article):
            filtered.append(article)
    
    return filtered
