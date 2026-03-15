from groq import Groq
import os, json

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_ropa(ropa_text):

    prompt = f"""
Convert the following RoPA description into a DFD structure.

Return JSON with:

entities
processes
datastores
flows

Example:

{{
 "entities": ["Customer"],
 "processes": ["Customer Support"],
 "datastores": ["CRM"],
 "flows": [
   ["Customer","Customer Support"],
   ["Customer Support","CRM"]
 ]
}}

RoPA:
{ropa_text}
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role":"user","content":prompt}]
    )

    return json.loads(response.choices[0].message.content)