def medical_expert_system():
    print("🤖 Welcome to the Hospital Expert System!")
    print("Answer with yes or no.\n")

    fever = input("Do you have a fever? ").lower()
    cough = input("Do you have a cough? ").lower()
    fatigue = input("Are you feeling fatigued? ").lower()
    headache = input("Do you have a headache? ").lower()
    breath = input("Do you have difficulty breathing? ").lower()

    # Inference engine (rule-based logic)
    if fever == "yes" and cough == "yes" and breath == "yes":
        print("🔍 You might have COVID-19. Please get tested and isolate.")
    elif fever == "yes" and cough == "yes" and fatigue == "yes":
        print("🩺 You might have the flu. Consult a doctor.")
    elif cough == "yes" and headache == "yes":
        print("💊 You might have a common cold. Rest and drink fluids.")
    else:
        print("✅ Your symptoms don’t match common diagnoses. Please consult a doctor.")

# Run the expert system
medical_expert_system()
