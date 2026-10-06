"""Gemini-based explanation module for wastewater treatment recommendations."""

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client()


def local_treatment_explanation(
    pollution_level,
    parameters,
    treatment_steps
):
    """Generate a local treatment explanation if Gemini is unavailable."""

    explanation = f"""


### Pollution Level

The predicted pollution level is **{pollution_level}**.

### Recommended Treatment

The following treatment steps were recommended based on the
predicted pollution level and the entered wastewater parameters:

"""

    for step in treatment_steps:
        explanation += f"- **{step}**\n"

    explanation += """

"""

    for step in treatment_steps:

        if step == "Screening":

            explanation += """
### Screening



Screening is a preliminary treatment process used to remove large
floating and suspended materials from wastewater.

**Why it is recommended**

Screening helps prevent large objects and solid materials from
entering and damaging downstream treatment units.

**How the process works**

Wastewater passes through screens that physically retain larger
materials while allowing wastewater to continue through the treatment
system.

**Benefits**

Screening protects downstream treatment equipment and improves the
overall treatment process.
"""

        elif step == "Primary treatment":

            explanation += """
### Primary Treatment



Primary treatment is a physical treatment stage that mainly removes
settleable and suspended solids from wastewater.

**Why it is recommended**

Primary treatment helps reduce the amount of suspended material
entering the biological and later treatment stages.

**How the process works**

Wastewater is held in a settling unit. Heavier solids settle toward
the bottom, while lighter materials can be removed from the surface.
The clarified wastewater then moves to the next treatment stage.

**Benefits**

Primary treatment reduces suspended solids and lowers the pollutant
load on subsequent treatment processes.
"""

        elif step == "Biological treatment":

            explanation += """
### Biological Treatment



Biological treatment uses microorganisms such as bacteria to break
down biodegradable organic matter present in wastewater.

**Why it is recommended**

Biological treatment is useful when the wastewater contains a
relatively high amount of biodegradable organic matter, such as
indicated by a higher BOD value.

**How the process works**

Wastewater enters a biological treatment unit where microorganisms
interact with the wastewater and consume biodegradable organic
matter. In an aerobic process, oxygen may be supplied to support
microbial activity. The resulting mixture can then pass through a
settling stage where biological solids are separated from the
treated water.

**Benefits**

Biological treatment helps reduce biodegradable organic matter and
BOD, improving the overall quality of wastewater.
"""

        elif step == "Coagulation and filtration":

            explanation += """
### Coagulation and Filtration



Coagulation and filtration are treatment processes used to help
remove suspended and fine particles from wastewater.

**Why it is recommended**

This treatment can be recommended when turbidity indicates a higher
amount of suspended or particulate material.

**How the process works**

During coagulation, suitable treatment chemicals are used to help
small particles come together and form larger particles. The water
then passes through a filtration stage that separates the formed
particles from the water.

**Benefits**

The process can reduce suspended particles and improve water
clarity.
"""

        elif step == "Aeration to improve dissolved oxygen":

            explanation += """
### Aeration



Aeration is a process in which air or oxygen is introduced into
wastewater.

**Why it is recommended**

Aeration can be recommended when the dissolved oxygen level is
relatively low or when oxygen is needed to support aerobic biological
treatment.

**How the process works**

Air or oxygen is introduced into the wastewater using an appropriate
aeration system. This increases oxygen availability in the treatment
process and supports aerobic microorganisms.

**Benefits**

Aeration improves oxygen availability and can support biological
treatment processes that reduce biodegradable organic matter.
"""

        elif step == "Advanced treatment":

            explanation += """
### Advanced Treatment



Advanced treatment refers to additional treatment processes used
after conventional physical and biological treatment to remove
specific remaining contaminants.

**Why it is recommended**

Advanced treatment can be recommended when the wastewater requires
additional pollutant removal beyond basic and biological treatment.

**How the process works**

Advanced treatment can involve processes such as membrane
separation, adsorption, advanced oxidation, nutrient removal, or
other specialized treatment methods. The appropriate process depends
on the type and concentration of contaminants present.

**Benefits**

Advanced treatment provides additional pollutant removal and can
improve the quality of treated wastewater.
"""

        elif step == "Heavy metal removal treatment":

            explanation += """
### Heavy Metal Removal Treatment



Heavy metal removal treatment is used to reduce dissolved metals
present in wastewater.

**Why it is recommended**

This treatment can be recommended when the entered heavy metal
parameters indicate the presence of metals requiring additional
removal.

**How the process works**

Depending on the type of metal and wastewater characteristics,
treatment may use processes such as precipitation, adsorption,
ion exchange, membrane processes, or other suitable technologies.

**Benefits**

Heavy metal removal can reduce metal concentrations and improve
wastewater quality.
"""

    explanation += """
### Overall Benefit

The recommended treatment steps work together to reduce different
types of wastewater pollutants. The Random Forest model predicts the
pollution level, while the treatment optimization component provides
a treatment recommendation based on the prediction and wastewater
parameters.

This is a prototype decision-support recommendation and should not
replace professional wastewater treatment design or site-specific
engineering assessment.
"""

    return explanation


def generate_treatment_explanation(
    pollution_level,
    parameters,
    treatment_steps
):
    """Generate a treatment explanation using Gemini with a local fallback."""

    prompt = f"""
You are an explanation assistant for a B.Tech wastewater treatment
decision-support project.

Predicted Pollution Level:
{pollution_level}

Wastewater Parameters:
{parameters}

Recommended Treatment Steps:
{treatment_steps}

Create a clear educational explanation of the recommended treatment.

IMPORTANT:

Explain ONLY the treatment processes contained in the
Recommended Treatment Steps.

For every recommended treatment, use exactly these headings:

### Treatment Name



Explain what the treatment is.

**Why it is recommended**

Explain why the treatment is relevant to the given pollution level
and wastewater parameters.

**How the process works**

Explain the general step-by-step process so that a B.Tech student
can understand how the treatment is carried out.

**Benefits**

Explain how the treatment can improve wastewater quality.

Do not write these sections as questions.
Do not use question marks in the headings.

Do not explain treatments that are not present in the
Recommended Treatment Steps.

Keep the explanation educational and practical.

Do not provide:
- Exact chemical doses
- Reactor dimensions
- Industrial flow rates
- Industrial operating settings
- Guarantees about safe discharge
- Guarantees about water reuse

Do not claim that the treatment will definitely meet any specific
water-quality standard.

Use simple language suitable for a B.Tech project.

End with:

"This is a prototype decision-support recommendation and should not
replace professional wastewater treatment design or site-specific
engineering assessment."
"""

    # Try Gemini
    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        if response.text:
            return response.text

    except Exception:
        pass

    # Try another Gemini model
    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        if response.text:
            return response.text

    except Exception:
        pass

    # Gemini unavailable → use local explanation
    return local_treatment_explanation(
        pollution_level,
        parameters,
        treatment_steps
    )