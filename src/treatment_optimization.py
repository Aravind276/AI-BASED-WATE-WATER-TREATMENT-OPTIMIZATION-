


# Function to recommend treatment process
def recommend_treatment(
    pollution_level,
    turbidity,
    bod,
    do,
    lead,
    mercury,
    arsenic
):

    treatment_process = []

    # --------------------------------
    # Pollution level based treatment
    # --------------------------------

    if pollution_level == 0:
        treatment_process.append("Screening")
        treatment_process.append("Basic filtration")

    elif pollution_level == 1:
        treatment_process.append("Screening")
        treatment_process.append("Primary treatment")
        treatment_process.append("Biological treatment")

    elif pollution_level == 2:
        treatment_process.append("Screening")
        treatment_process.append("Primary treatment")
        treatment_process.append("Advanced treatment")

    # --------------------------------
    # Turbidity treatment
    # --------------------------------

    if turbidity > 5:
        treatment_process.append(
            "Coagulation and filtration"
        )

    # --------------------------------
    # BOD treatment
    # --------------------------------

    if bod > 10:
        treatment_process.append(
            "Biological treatment for BOD reduction"
        )

    # --------------------------------
    # DO treatment
    # --------------------------------

    if do < 4:
        treatment_process.append(
            "Aeration to improve dissolved oxygen"
        )

    # --------------------------------
    # Heavy metal treatment
    # --------------------------------

    if lead > 0.01 or mercury > 0.001 or arsenic > 0.01:
        treatment_process.append(
            "Heavy metal removal treatment"
        )

    # Remove duplicate treatment steps
    treatment_process = list(dict.fromkeys(treatment_process))

    return treatment_process


# Function for treatment analysis
def treatment_analysis(pollution_level):

    if pollution_level == 0:

        treatment = "Basic treatment"
        efficiency = "60-70%"
        energy = "Low"

    elif pollution_level == 1:

        treatment = "Biological treatment"
        efficiency = "70-80%"
        energy = "Medium"

    else:

        treatment = "Advanced treatment"
        efficiency = "80-90%"
        energy = "High"

    return treatment, efficiency, energy


def run_cli():
    """Run the original command-line version of the treatment module."""
    print("\n==========================================")
    print(" Wastewater Treatment Optimization")
    print("==========================================")
    print("\nEnter Wastewater Parameters")

    pollution_level = int(
        input("Enter Pollution Level (0=Low, 1=Medium, 2=High): ")
    )
    input("Enter pH: ")
    turbidity = float(input("Enter Turbidity (NTU): "))
    input("Enter Temperature (°C): ")
    do = float(input("Enter DO (mg/L): "))
    bod = float(input("Enter BOD (mg/L): "))
    lead = float(input("Enter Lead (mg/L): "))
    mercury = float(input("Enter Mercury (mg/L): "))
    arsenic = float(input("Enter Arsenic (mg/L): "))

    treatment_process = recommend_treatment(
        pollution_level, turbidity, bod, do, lead, mercury, arsenic
    )
    treatment, efficiency, energy = treatment_analysis(pollution_level)
    level_name = {0: "LOW", 1: "MEDIUM", 2: "HIGH"}.get(
        pollution_level, "INVALID"
    )

    print("\n==========================================")
    print(" Treatment Recommendation")
    print("==========================================")
    print("Pollution Level:", level_name)
    print("\nRecommended Treatment Process:")
    for index, process in enumerate(treatment_process, start=1):
        print(f"Step {index}: {process}")

    print("\n==========================================")
    print(" Treatment Analysis")
    print("==========================================")
    print("Main Treatment:", treatment)
    print("Estimated Treatment Efficiency:", efficiency)
    print("Energy Consumption:", energy)
    print("\nTreatment optimization completed.")


if __name__ == "__main__":
    run_cli()
