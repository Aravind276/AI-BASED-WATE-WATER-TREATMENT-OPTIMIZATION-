"""Gemini-based explanation module for wastewater treatment recommendations."""

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client()


def generate_treatment_explanation(
    pollution_level,
    parameters,
    treatment_steps
):
    """Generate a simple explanation of the treatment recommendation."""

    prompt = f"""
You are an explanation assistant for a B.Tech wastewater
treatment decision-support project.

Pollution Level:
{pollution_level}

Wastewater Parameters:
{parameters}

Recommended Treatment Steps:
{treatment_steps}

Give a simple and concise explanation.

Include these sections:

1. What does the recommended treatment mean?
2. Why was it recommended based on the given parameters?
3. How is it generally performed?
4. How can it help improve wastewater quality?

Explain only the treatment processes that are present
in the Recommended Treatment Steps.

Do not provide:
- Exact chemical doses
- Reactor dimensions
- Flow rates
- Industrial operating settings
- Guarantees about safe discharge or reuse

Do not claim that the treatment will definitely meet
any specific water-quality standard.

End with this statement:

"This is a prototype decision-support recommendation
and should not replace professional wastewater treatment
design or site-specific engineering assessment."

Keep the explanation suitable for a B.Tech project
and approximately 300-400 words.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text