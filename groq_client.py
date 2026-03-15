import os
import json
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

def analyze_ropa(ropa_text):

    prompt = f"""
You are a privacy architect.

Convert the following RoPA into a structured DFD.

Return ONLY valid JSON.

Format:

{{
 "entities": [],
 "processes": [],
 "datastores": [],
 "flows": []
}}

RoPA:
{ropa_text}
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content.strip()

    # remove markdown formatting if AI adds it
    content = content.replace("```json", "").replace("```", "")

    try:
        return json.loads(content)

    except:
        # fallback if AI response breaks
        return {
            "entities": ["User"],
            "processes": ["Processing"],
            "datastores": ["Database"],
            "flows": [
                ["User","Processing"],
                ["Processing","Database"]
            ]
        }
