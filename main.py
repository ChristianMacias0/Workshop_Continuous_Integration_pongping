"""Módulo para el cálculo de costos y validación de membresías de gimnasio."""

# Catálogo de planes y costos base
PLANS = {
    "Basic": {"base_cost": 30, "is_premium": False},
    "Premium": {"base_cost": 80, "is_premium": True},
    "Family": {"base_cost": 120, "is_premium": False}
}

# Características adicionales disponibles
FEATURES = {
    "Personal Training": {"cost": 50, "is_premium": True},
    "Group Classes": {"cost": 25, "is_premium": False},
    "Sauna Access": {"cost": 15, "is_premium": False}
}

def validate_inputs(plan_name, selected_features, confirmed):
    """Valida que los datos ingresados existan en el catálogo y estén confirmados."""
    if not confirmed:
        print("\n[Error] La membresía fue cancelada por el usuario.")
        return False 
    if plan_name not in PLANS:
        print(f"\n[Error] El plan '{plan_name}' no está disponible.")
        return False     
    for feature in selected_features:
        if feature not in FEATURES:
            print(f"\n[Error] La característica extra '{feature}' no está disponible.")
            return False
            
    return True
def calculate_membership_cost(plan_name, selected_features, num_members, confirmed=True):
    """
    Calcula el costo total de la membresía del gimnasio.
    Aplica recargos premium y descuentos especiales.
    """
    if not validate_inputs(plan_name, selected_features, confirmed):
        return -1

    plan_data = PLANS[plan_name]
    base_cost = plan_data["base_cost"]

    features_cost = 0
    has_premium_feature = plan_data["is_premium"]

    for feature in selected_features:
        feat_data = FEATURES[feature]
        features_cost += feat_data["cost"]
        if feat_data["is_premium"]:
            has_premium_feature = True

    total_cost = base_cost + features_cost

    # Aplicar recargo del 15% si incluye características premium
    if has_premium_feature:
        total_cost *= 1.15

    # Multiplicar por la cantidad de personas
    total_cost *= num_members

    # Descuento grupal del 10% si son 2 o más miembros
    if num_members >= 2:
        total_cost *= 0.90

    # Descuentos por ofertas especiales
    if total_cost > 400:
        total_cost -= 50  
    elif total_cost > 200:
        total_cost -= 20  
    return int(round(total_cost, 0))
