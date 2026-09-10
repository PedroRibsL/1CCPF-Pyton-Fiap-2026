from datetime import date

def model_lead(name, email, company, step = "novo"):
    """Estrutura um lead como um dicionario """
    return {
        "name": name,
        "email": email,
        "company": company,
        "Step": step,
        "created": date.today().isoformat(),
    }