import glob, os
import re

def fetch_evidence(parsed_claim):
    """Smart offline evidence search with relevance scoring."""
    results = []
    keywords = parsed_claim.get("keywords", [])

    if not keywords:
        return results

    # Convert keywords to lowercase
    keywords = [k.lower() for k in keywords]

    # Search all .txt files inside data/sources folder
    for fname in glob.glob(os.path.join("data", "sources", "*.txt")):
        try:
            with open(fname, "r", encoding="utf-8") as f:
                text = f.read().lower()

            # Count keyword matches
            score = sum(text.count(k) for k in keywords)

            if score > 0:
                # Extract a meaningful snippet around the first match
                first_key = keywords[0]
                idx = text.find(first_key)

                start = max(0, idx - 100)
                end = min(len(text), idx + 300)
                snippet = text[start:end]

                # Clean snippet
                snippet = re.sub(r"\s+", " ", snippet).strip()

                results.append({
                    "source": os.path.basename(fname),
                    "score": score,
                    "snippet": snippet
                })

        except Exception:
            continue

    # Sort by best evidence first
    results.sort(key=lambda x: x["score"], reverse=True)
    return results
