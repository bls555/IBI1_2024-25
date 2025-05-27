def calculate_paracetamol_dose(weight, strength):
    """
    Calculate the dose of paracetamol for children based on weight and strength.
    Parameters:
    weight (int): The weight of the child in kg.
    strength (int): The strength of paracetamol in mg/5 ml (either 120 or 250).
    Returns:
    float: The volume of paracetamol in ml.
    """
    # check if weight is valid for children
    if not 10 <= weight <= 100:
        return ("Error, the weight must be between 10 and 100 kg.")
         

    # check if strength is valid
    if strength not in [120, 250]:
        return ("Error, the strength of paracetamol must be either 120 mg/5 ml or 250 mg/5 ml.")
        

    # calculate the dose in mg, and the volume in ml
    dose_mg = 15 * weight
    dose_ml = (dose_mg / strength) * 5

    return (f"the child of {weight} kg needs {dose_ml} ml paracetamol, whose strengh is {strength} mg/5 ml ")

#example
weight = 30  #weight is 30 kg
strength = 120  # strength is 120 mg/5 ml

print(calculate_paracetamol_dose(weight, strength))