DOMAIN_DATASET_MAP = {
    "data_science": "data/linkedin_jobs.csv",
    "web_development": "data/web_development_jobs.csv",
    "cybersecurity": "data/cybersecurity_jobs.csv"
}

def get_dataset_path(domain):
    return DOMAIN_DATASET_MAP.get(domain, "data/linkedin_jobs.csv")
