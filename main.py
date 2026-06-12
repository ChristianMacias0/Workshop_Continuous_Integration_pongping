"""Módulo para el cálculo de costos y validación de reservas."""
def calculate_base_and_premium(room_name, selected_services, num_guests):
    """Calcula el costo base de habitación + servicios y añade recargo premium."""
    room_data = next(r for r in ROOM_TYPES.values() if r["name"] == room_name)
    base_cost = room_data["base_cost"]
    # Diego Alfonzo
    services_cost = 0
    for srv_name in selected_services:
        srv_data = next(s for s in SERVICES.values() if s["name"] == srv_name)
        services_cost += srv_data["cost"]

    total_cost = base_cost + services_cost

    if room_data["is_premium"] or "VIP Lounge Access" in selected_services:
        total_cost = total_cost * 1.15

    return round(total_cost * num_guests, 2)

# Catálogo de habitaciones y sus costos base (por noche)
ROOM_TYPES = {
    "1": {"name": "Standard", "base_cost": 50, "is_premium": False},
    "2": {"name": "Suite", "base_cost": 100, "is_premium": True},
    "3": {"name": "Family", "base_cost": 150, "is_premium": False}
}
# Servicios adicionales disponibles
SERVICES = {
    "1": {"name": "Spa Treatment", "cost": 30},
    "2": {"name": "All-Inclusive Meal", "cost": 20},
    "3": {"name": "VIP Lounge Access", "cost": 40}
}

def validate_inputs(room_name, selected_services, confirmed):
    """Valida que los datos ingresados existan en el catálogo."""
    if not confirmed:
        print("\n[Error] La reserva fue cancelada por el usuario.")
        return False
    if room_name not in [room["name"] for room in ROOM_TYPES.values()]:
        print(f"\n[Error] La habitación '{room_name}' no está disponible.")
        return False
    valid_services = [srv["name"] for srv in SERVICES.values()]
    for service in selected_services:
        if service not in valid_services:
            print(f"\n[Error] El servicio '{service}' no está disponible.")
            return False
    return True
