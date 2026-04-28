import re

def extract_mda(text):
    """
    Extract MD&A section using keyword patterns.
    """
    pattern = r"management discussion and analysis(.*?)(risk factors|quantitative disclosures)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

    if match:
        return match.group(1).strip()
    return "MD&A section not found."


def extract_risk(text):
    """
    Extract Risk Factors section.
    """
    pattern = r"risk factors(.*?)(unresolved staff comments|properties|legal proceedings)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

    if match:
        return match.group(1).strip()
    return "Risk section not found."
