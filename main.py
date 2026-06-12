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
def calculate_booking(room_name, selected_services, num_guests, confirmed=True):
    """Une las partes lógicas para dar el resultado final de la reserva."""
    from hotel_system import validate_inputs, calculate_base_and_premium, apply_discounts
    if not validate_inputs(room_name, selected_services, confirmed):
        return -1

    subtotal = calculate_base_and_premium(room_name, selected_services, num_guests)
    return apply_discounts(subtotal, num_guests)

def get_room_and_guests():
"""Captura los datos iniciales del cliente en la consola."""
print("=" * 45 + "\n BIENVENIDO AL SISTEMA DE RESERVAS - HOTEL\n" + "=" * 45)
print("\n[Paso 1] Seleccione el tipo de habitación:")
for key, value in ROOM_TYPES.items():
print(f" {key}. {value['name']} (${value['base_cost']}/noche)")

room_choice = input("Seleccione una opción (1-3): ").strip()
if room_choice not in ROOM_TYPES:
print("[Error] Opción inválida."); return None, None

try:
num_guests = int(input("\n[Paso 2] Ingrese el número de huéspedes: "))
if num_guests <= 0:
print("[Error] Debe ser mayor a 0."); return None, None
except ValueError:
print("[Error] Entrada inválida."); return None, None

return ROOM_TYPES[room_choice]["name"], num_guests


def apply_discounts(total_cost, num_guests):
    """Aplica descuentos grupales y ofertas especiales al total."""
    # Descuento por grupo (2 o más huéspedes)
    if num_guests >= 2:
        print("\n-> ¡Descuento Grupal! Se aplicó un 10% de descuento al total base.")
        total_cost = total_cost * 0.90

# Descuentos por ofertas especiales fijas
    if total_cost > 400:
        print("-> ¡Oferta Especial! Descuento adicional de $50 por superar los $400.")
        total_cost -= 50
    elif total_cost > 200:
        print("-> ¡Oferta Especial! Descuento adicional de $20 por superar los $200.")
        total_cost -= 20

    return int(total_cost)
