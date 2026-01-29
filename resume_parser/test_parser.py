from resume_parser import parse_resume

result = parse_resume("sample_resume.pdf")

print(result["metadata"])
print(result["clean_text"][:500])
