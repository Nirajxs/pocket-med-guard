import asyncio
import logging
from .tools.claim_parser import parse_claim
from .tools.evidence_fetcher import fetch_evidence
from .tools.verifier import verify_claim
from .memory import MemoryService

logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# HUMAN-LIKE NATURAL MEDICAL RESPONSE
# ---------------------------------------------------------
def generate_human_response(parsed, verdict):
    claim = parsed.get("text", "")
    keywords = parsed.get("keywords", [])
    label = verdict.get("label", "")
    explanation = verdict.get("explanation", "")

    # Base intro
    base = f"🩺 **Let's talk about your question:**\n**“{claim}”**\n\n"

    advice = ""

    # ---------------------------
    # MEDICAL KEYWORD RESPONSES
    # ---------------------------

    if "fever" in keywords:
        advice = (
            "🌡️ **Fever Insight:**\n"
            "- Usually caused by infections\n"
            "- Stay hydrated (ORS, warm water)\n"
            "- Paracetamol helps reduce fever\n"
            "- Avoid cold drinks\n"
            "- Consult doctor if fever >102°F or lasts >3 days\n\n"
        )

    elif "cough" in keywords:
        advice = (
            "🤧 **Cough Insight:**\n"
            "- Warm water helps\n"
            "- Honey + warm water is soothing\n"
            "- Avoid cold drinks\n"
            "- If cough lasts 1 week+, consult doctor\n\n"
        )

    elif "headache" in keywords:
        advice = (
            "🤕 **Headache Insight:**\n"
            "- Stay hydrated\n"
            "- Take rest\n"
            "- Avoid screen for some time\n"
            "- If headache is severe or frequent → consult doctor\n\n"
        )

    elif "diarrhea" in keywords:
        advice = (
            "🚰 **Diarrhea Insight:**\n"
            "- Drink ORS\n"
            "- Avoid oily/spicy food\n"
            "- Eat bananas, rice, curd\n"
            "- If dehydration occurs → doctor needed\n\n"
        )

    elif "vomiting" in keywords:
        advice = (
            "🤢 **Vomiting Insight:**\n"
            "- Drink small sips of water\n"
            "- ORS is helpful\n"
            "- Avoid heavy food\n"
            "- If persists → medical evaluation needed\n\n"
        )

    elif "cold" in keywords:
        advice = (
            "🥶 **Common Cold Insight:**\n"
            "- Steam inhalation helps\n"
            "- Stay warm\n"
            "- Vitamin C intake helps immunity\n\n"
        )

    elif "covid" in keywords or "virus" in keywords:
        advice = (
            "🦠 **Virus/Covid Insight:**\n"
            "- Isolate if symptoms start\n"
            "- Wear mask\n"
            "- Take paracetamol for fever\n"
            "- Monitor oxygen levels\n\n"
        )

    elif "turmeric" in keywords or "honey" in keywords:
        advice = (
            "🌿 Natural remedy noted.\n"
            "They help immunity but **do not cure serious diseases**.\n\n"
        )
        
        
        
    elif "pain" in keywords or "headache" in keywords:
     advice += (
        "💆 **Pain / Headache Response:**\n"
        "- Take proper rest\n"
        "- Drink enough water\n"
        "- Avoid excessive screen use\n"
        "- Mild pain: Paracetamol may help\n"
        "- Severe / repeated pain → get a medical checkup\n\n"
    )

        
        
    elif "cancer" in keywords or "tumor" in keywords:
        advice += (
            "🎗️ Cancer requires proper medical diagnosis. "
            "Home remedies do **not** cure cancer.\n\n"
        )
        
    elif "cold" in keywords:
     advice += (
        "🤧 **Cold Response:**\n"
        "- Steam inhalation helps\n"
        "- Warm fluids soothe the throat\n"
        "- Vitamin C rich foods help immunity\n"
        "- Avoid cold drinks\n"
        "- If cold lasts 7+ days, consult a doctor\n\n"
    )
     
    elif "vomiting" in keywords:
     advice += (
        "🤢 **Vomiting Response:**\n"
        "- Drink ORS to avoid dehydration\n"
        "- Avoid solid foods for a few hours\n"
        "- Do not drink milk or heavy food\n"
        "- If vomiting continues, consult a doctor\n\n"
    )
     
    elif "diabetes" in keywords:
     advice += (
        "🩸 **Diabetes Response:**\n"
        "- Monitor blood sugar regularly\n"
        "- Reduce sugar intake\n"
        "- Walk daily for 30 minutes\n"
        "- Follow doctor-prescribed medicines\n"
        "- Avoid skipping meals\n\n"
    )
     
    elif "virus" in keywords or "infection" in keywords:
     advice += (
        "🦠 **Infection / Virus Response:**\n"
        "- Maintain hygiene\n"
        "- Drink warm fluids\n"
        "- Avoid close contact with sick people\n"
        "- Take adequate rest\n"
        "- If symptoms worsen, get checked\n\n"
    )
     
    elif "immunity" in keywords:
     advice += (
        "🛡️ **Immunity Boost Response:**\n"
        "- Vitamin C rich foods (lemon/orange)\n"
        "- Adequate sleep\n"
        "- Regular exercise\n"
        "- Reduce stress\n"
        "- Stay hydrated\n\n"
    )
     
     
    elif "vitamin" in keywords:
     advice += (
        "🍊 **Vitamin Related Response:**\n"
        "- Include fruits & vegetables\n"
        "- Vitamin D: sunlight exposure helps\n"
        "- Vitamin B12: dairy / supplements\n"
        "- Do not self-medicate high doses\n\n"
    )

    elif "ginger" in keywords:
     advice += (
        "🫚 **Ginger Response:**\n"
        "- Helps soothe throat irritation\n"
        "- Mild anti-inflammatory effect\n"
        "- Can be taken with warm water or tea\n\n"
    )

    elif "honey" in keywords:
     advice += (
        "🍯 **Honey Response:**\n"
        "- Helps with cough and throat irritation\n"
        "- Natural soothing effect\n"
        "- Do NOT give honey to infants below 1 year\n\n"
    )
     
    elif "paracetamol" in keywords:
     advice += (
        "💊 **Paracetamol Response:**\n"
        "- Helps reduce fever & mild pain\n"
        "- Do not exceed 3 doses in 24 hours\n"
        "- Take after food\n\n"
    )
     
    elif "antibiotic" in keywords:
     advice += (
        "💊 **Antibiotic Response:**\n"
        "- Only useful for bacterial infections\n"
        "- Do NOT take without doctor consultation\n"
        "- Complete full course if prescribed\n\n"
    )

    elif "flu" in keywords:
     advice += (
        "🤒 **Flu Care:**\n"
        "- Drink warm fluids\n"
        "- Take rest and avoid cold air\n"
        "- Paracetamol can reduce fever/body ache\n"
        "- See a doctor if symptoms last >3 days\n\n"
    )

    elif "covid" in keywords or "covid-19" in keywords or "coronavirus" in keywords:
     advice += (
        "🦠 **COVID-19 Guidance:**\n"
        "- Isolate if symptoms appear\n"
        "- Monitor oxygen saturation (should be above 95%)\n"
        "- Drink fluids + rest\n"
        "- Seek urgent help if breathing difficulty occurs\n\n"
    )
    elif "infection" in keywords:
     advice += (
        "🧫 **Possible Infection:**\n"
        "- Hydrate properly\n"
        "- Avoid self-medicating with antibiotics\n"
        "- Fever + redness/swelling may indicate infection\n"
        "- Consult doctor if symptoms worsen\n\n"
    )
    elif "malaria" in keywords:
        advice += (
        "🦟 **Malaria Advice:**\n"
        "- High fever + chills are common\n"
        "- Do not delay blood test\n"
        "- Drink ORS/water regularly\n"
        "- Requires proper antimalarial treatment\n\n"
    )
    elif "dengue" in keywords:
     advice += (
        "🩸 **Dengue Care:**\n"
        "- Avoid ibuprofen; use paracetamol only\n"
        "- Drink lots of liquids (ORS, coconut water)\n"
        "- Watch for bleeding or vomiting\n"
        "- Platelet count monitoring may be required\n\n"
    )
    elif "typhoid" in keywords:
        advice += (
        "🧪 **Typhoid Precautions:**\n"
        "- Eat soft, clean food only\n"
        "- Avoid raw street food and cold drinks\n"
        "- Complete full antibiotic course (doctor prescribed)\n"
        "- Rest is essential for recovery\n\n"
    )
    elif "pneumonia" in keywords:
        advice += (
        "🫁 **Pneumonia Warning:**\n"
        "- Persistent cough + fever + breathing difficulty\n"
        "- Needs urgent medical evaluation\n"
        "- Steam inhalation may give relief\n"
        "- Avoid self-medication with antibiotics\n\n"
    )
    elif "asthma" in keywords:
        advice += (
        "😮‍💨 **Asthma Care:**\n"
        "- Keep inhaler rescue medication handy\n"
        "- Avoid dust, smoke, strong smells\n"
        "- Sit upright during breathing difficulty\n"
        "- Seek help if inhaler not providing relief\n\n"
    )

    elif "tired" in keywords:
     advice += (
        "💤 **Possible Tiredness/Fatigue:**\n"
        "- Get enough rest and sleep\n"
        "- Maintain a healthy diet and hydrate\n"
        "- Avoid caffeine or heavy meals before bed\n"
        "- Regular physical activity can improve energy levels\n"
        "- If fatigue persists, consult a doctor to rule out underlying issues\n\n"
    )
     
    elif "body pain" in keywords:
        advice += (
        "💪 **Possible Body Pain:**\n"
        "- Rest and avoid straining your muscles\n"
        "- Apply a warm compress or cold pack to the affected area\n"
        "- Gentle stretching or light exercise can help relieve tension\n"
        "- Stay hydrated and maintain a balanced diet\n"
        "- If pain persists or worsens, seek medical advice\n\n"
    )
    elif "head pain" in keywords:
        advice += (
        "🤕 **Possible Head Pain (Headache):**\n"
        "- Drink plenty of water to stay hydrated\n"
        "- Rest in a quiet, dark space to reduce strain on your eyes and mind\n"
        "- Apply a cold or warm compress to your forehead or neck\n"
        "- Avoid bright lights, loud sounds, and strong smells\n"
        "- Over-the-counter pain relievers (like ibuprofen or paracetamol) may help\n"
        "- If the pain persists or worsens, or if accompanied by nausea, vision changes, or dizziness, consult a doctor\n\n"
    )
   


    # ---------------------------------------------------
    # MEDICINE-RELATED HUMAN RESPONSES
    # ---------------------------------------------------

    if "paracetamol" in keywords or "acetaminophen" in keywords or "dolo" in keywords or "crocin" in keywords:
        advice += (
            "💊 **Paracetamol Information:**\n"
            "- Helps reduce fever and mild to moderate pain\n"
            "- Safe dose (adult): 500mg–1000mg every 6 hours\n"
            "- Do NOT exceed 4g per day\n"
            "- Avoid alcohol while taking paracetamol\n\n"
        )

    if "ibuprofen" in keywords or "painkiller" in keywords or "analgesic" in keywords:
        advice += (
            "💊 **Ibuprofen / Painkiller Info:**\n"
            "- Good for pain, inflammation, body ache\n"
            "- Always take after food (can irritate stomach)\n"
            "- Avoid if you have kidney issues\n"
            "- Not recommended in pregnancy\n\n"
        )

    if "antibiotic" in keywords or "azithromycin" in keywords or "amoxicillin" in keywords:
        advice += (
            "💊 **Antibiotic Information:**\n"
            "- Works ONLY on bacterial infections, NOT viral\n"
            "- Must complete full course once started\n"
            "- Avoid taking without prescription (can cause resistance)\n"
            "- Common side effects: loose motion, stomach upset\n\n"
        )

    if "antiviral" in keywords:
        advice += (
            "💊 **Antiviral Information:**\n"
            "- Used for viral infections like influenza, herpes, hepatitis\n"
            "- Works by slowing down virus replication\n"
            "- Must be taken under doctor supervision\n\n"
        )

    if "antiseptic" in keywords:
        advice += (
            "🧼 **Antiseptic Information:**\n"
            "- Used to clean wounds and prevent infection\n"
            "- Common examples: Dettol, Savlon\n"
            "- Do not use strong antiseptics inside the mouth or eyes\n\n"
        )

    if "cetirizine" in keywords:
        advice += (
            "🤧 **Cetirizine Info (Anti-allergy):**\n"
            "- Helps with sneezing, allergy, runny nose\n"
            "- May cause drowsiness (avoid driving)\n"
            "- Safe for most people but avoid overdose\n\n"
        )

    if "dexamethasone" in keywords:
        advice += (
            "💊 **Dexamethasone Information:**\n"
            "- A corticosteroid used in swelling, severe allergy, breathing issues\n"
            "- Strong medicine — must be taken under medical guidance\n"
            "- Long-term use can cause side effects like weight gain, sugar rise\n\n"
        )

    if "vitamin" in keywords or "zinc" in keywords:
        advice += (
            "🍊 **Vitamins & Zinc Information:**\n"
            "- Helps improve immunity and recovery\n"
            "- Vitamin C and Zinc commonly used in cold/flu\n"
            "- Best taken after food\n"
            "- Avoid overdose — can cause stomach upset\n\n"
        )
        
        
        

 










    # ---------------------------------------
    # UNIVERSAL FALLBACK → REPLY TO ANY TEXT
    # ---------------------------------------
    if advice == "":
        advice = (
            "🙂 I understand your message. "
            "Here’s what I can tell you based on your input:\n"
            "- I'm here to help with medical doubts.\n"
            "- If it's a symptom, I can guide you.\n"
            "- If it's a remedy, I can explain if it's helpful.\n\n"
            
              "🙂 It seems your message does not contain any clear medical symptom.\n"
            "If you're feeling unwell, you can tell me like:\n"
            "- I have fever\n"
            "- I feel tired\n"
            "- I have body pain\n"
           
        )    
        

    # ---------------------------
    # ATTACH AI VERDICT
    # ---------------------------
    verdict_text = (
        f"🧪 **AI Verdict:** {label.replace('_',' ').title()}\n"
        f"📌 {explanation}\n"
    )

    return base + advice + verdict_text

    
        

  
    # -------------------------
    # AI VERDICT ATTACHED
    # -------------------------
    response += (
        f"🧪 **AI Verdict:** {label.replace('_', ' ').title()}\n"
        f"📌 {explanation}\n"
    )

    return response


# ---------------------------------------------------------
# MAIN AGENT
# ---------------------------------------------------------
class ConversationAgent:
    def __init__(self):
        self.memory = MemoryService()

    async def handle_message(self, user_id, message):
        logger.info(f"Received message from {user_id}: {message}")

        # STEP 1 — Parse claim
        parsed = parse_claim(message)

        # STEP 2 — Evidence fetcher (async / non-async safe)
        if asyncio.iscoroutinefunction(fetch_evidence):
            evidence = await fetch_evidence(parsed)
        else:
            loop = asyncio.get_running_loop()
            evidence = await loop.run_in_executor(None, fetch_evidence, parsed)

        # STEP 3 — Verify the claim
        verdict = verify_claim(parsed, evidence)

        # STEP 4 — Human style reply
        human_reply = generate_human_response(parsed, verdict)

        # STEP 5 — Save memory
        self.memory.write(user_id, parsed, verdict)

        # STEP 6 — Return final data
        return {
            "reply": human_reply,
            "parsed": parsed,
            "verdict": verdict,
            "evidence_count": len(evidence)
        }
















