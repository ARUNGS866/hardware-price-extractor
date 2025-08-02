# hardware.py

import os
from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletionMessageParam
)

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_data_from_paragraph(paragraph: str) -> str:
    prompt = f"""
You are a financial data extractor for hardware items. 
Given the below paragraph, extract a table with rows as "Item" (e.g., Door, Plywood), and columns: 
"Estimated Price", "Actual Price". 

Paragraph:
\"\"\"{paragraph}\"\"\"

Return result as a markdown table.
"""

    messages: list[ChatCompletionMessageParam] = [
        ChatCompletionSystemMessageParam(
            role="system",
            content="You are a helpful assistant that extracts structured data from text."
        ),
        ChatCompletionUserMessageParam(
            role="user",
            content=prompt
        )
    ]

    # 🔁 UPDATED MODEL
    response = client.chat.completions.create(
        model="llama3-70b-8192",  # Replaced decommissioned model
        messages=messages
    )

    return response.choices[0].message.content
