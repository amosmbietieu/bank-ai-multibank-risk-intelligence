import pandas as pd

def compare_banks():
    data = {
        "Bank": ["JPMorgan", "Bank of America", "Wells Fargo"],
        "Risk Score": [0.22, 0.35, 0.28],
        "Sentiment": [0.14, 0.08, 0.10]
    }

    return pd.DataFrame(data)
