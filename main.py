def calculate_base_and_premium(room_name, selected_services, num_guests):
    """Calcula el costo base de habitación + servicios y añade recargo premium."""
    room_data = next(r for r in ROOM_TYPES.values() if r["name"] == room_name)
    base_cost = room_data["base_cost"]
#Diego Alfonzo
    services_cost = 0
    for srv_name in selected_services:
        srv_data = next(s for s in SERVICES.values() if s["name"] == srv_name)
        services_cost += srv_data["cost"]

        total_cost = base_cost + services_cost

    # Aplicar recargo Premium (15%)
        if room_data["is_premium"] or "VIP Lounge Access" in selected_services:
            total_cost = total_cost * 1.15

    # Retorna el acumulado multiplicado por el número de huéspedes
    return total_cost * num_guests