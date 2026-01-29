from .constants import SUPPORTED_DOMAINS

def detect_domain(skills):
    scores = {
        "data_science": {"python", "pandas", "numpy", "sql", "machine learning"},
        "web_development": {"html", "css", "javascript", "react", "node.js"},
        "cybersecurity": {"network security", "siem", "penetration testing"}
    }

    domain_score = {
        domain: len(set(skills) & keywords)
        for domain, keywords in scores.items()
    }

    best_domain = max(domain_score, key=domain_score.get)

    # 🚨 If no meaningful overlap → unsupported
    if domain_score[best_domain] < 2:
        return "unsupported"

    return best_domain
