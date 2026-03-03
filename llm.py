from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a startup COO-level Business Intelligence agent.
Be concise, strategic, and insight-driven.
Highlight risks, opportunities, and operational insights.
Never fabricate numbers.
Only use provided metrics.
"""

def generate_answer(metrics, question):

    context = f"""
    Metrics:
    Total Revenue: {metrics['total_revenue']}
    Total Deals: {metrics['total_deals']}
    Open Deals: {metrics['open_deals']}
    Stalled Deals (>14 days inactive): {metrics['stalled_deals']}
    Average Deal Size: {metrics['avg_deal_size']}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": context + "\nQuestion: " + question},
        ],
    )

    return response.choices[0].message.content
