import pandas as pd

TEXT_COLUMNS_PRIORITY = [
    "job_skills",
    "job_summary",
    "description",
    "formatted_skills_desc",
    "skills_desc"
]

def load_job_data(csv_path, sample_size=None):
    df = pd.read_csv(csv_path)

    # Identify usable text column
    text_column = None
    for col in TEXT_COLUMNS_PRIORITY:
        if col in df.columns:
            text_column = col
            break

    if text_column is None:
        raise ValueError(
            f"No usable skill text column found. Available columns: {list(df.columns)}"
        )

    df["skill_text"] = df[text_column].astype(str)

    if sample_size:
        df = df.sample(min(sample_size, len(df)), random_state=42)

    return df
