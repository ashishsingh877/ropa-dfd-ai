import os
import json
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def analyze_ropa(ropa_text):

    prompt = f"""
You are a privacy architecture expert.

Convert the following RoPA into a DFD structure.

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
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    # remove markdown formatting
    content = content.replace("```json","").replace("```","")

    try:
        return json.loads(content)
    except:
        return {
            "entities":["User"],
            "processes":["Processing"],
            "datastores":["Database"],
            "flows":[
                ["User","Processing"],
                ["Processing","Database"]
            ]
        }
