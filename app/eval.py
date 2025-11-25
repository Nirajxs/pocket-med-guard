import pandas as pd
from .tools.claim_parser import parse_claim
from .tools.evidence_fetcher import fetch_evidence
from .tools.verifier import verify_claim
from sklearn.metrics import classification_report
import os

def run_eval():
    path = os.path.join('data','claims_test.csv')
    df = pd.read_csv(path)
    preds = []
    for _, row in df.iterrows():
        p = parse_claim(row.claim_text)
        e = fetch_evidence(p)
        v = verify_claim(p, e)
        preds.append(v['label'])
    print(classification_report(df.label, preds))

if __name__ == '__main__':
    run_eval()
