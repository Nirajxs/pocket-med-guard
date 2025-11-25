def verify_claim(parsed, evidence):
    claim = parsed.get("text", "").lower()

    if not evidence:
        return {
            "label": "no_evidence_found",
            "confidence": 0.25,
            "explanation": "No supporting evidence found. This does not mean the claim is false."
        }

    total_score = sum(e.get("score", 0) for e in evidence)

    negative = ["not effective", "no evidence", "not recommended", "not proven"]

    for doc in evidence:
        snip = doc.get("snippet", "").lower()
        if any(n in snip for n in negative):
            return {
                "label": "likely_false",
                "confidence": 0.85,
                "explanation": "Available evidence suggests this claim is not supported."
            }

    if total_score >= 5:
        return {
            "label": "likely_true",
            "confidence": 0.82,
            "explanation": "Strong evidence suggests this claim may be true."
        }

    if total_score >= 1:
        return {
            "label": "inconclusive_but_supported",
            "confidence": 0.55,
            "explanation": "Some evidence supports this claim, but not strongly."
        }

    return {
        "label": "inconclusive",
        "confidence": 0.40,
        "explanation": "Evidence is too weak to decide."
    }
