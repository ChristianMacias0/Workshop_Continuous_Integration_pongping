import pytest
# Importamos las funciones y los diccionarios de tu archivo original
from main import calculate_base_and_premium, validate_inputs, ROOM_TYPES, SERVICES

# === TESTS PARA LA PRIMERA FUNCIÓN ===

def test_habitacion_estandar_sin_servicios():
    # Standard (50) + No servicios (0) = 50. No premium. 50 * 1 huesped = 50
    resultado = calculate_base_and_premium("Standard", [], 1)
    assert resultado == 50

def test_habitacion_estandar_con_un_servicio():
    # Standard (50) + Spa (30) = 80. No premium. 80 * 2 huespedes = 160
    resultado = calculate_base_and_premium("Standard", ["Spa Treatment"], 2)
    assert resultado == 160

def test_habitacion_suite_aplica_recargo_premium():
    # Suite es premium de por sí.
    # Suite (100) + No servicios (0) = 100. 
    # Con recargo 15% = 115. 115 * 1 huesped = 115
    resultado = calculate_base_and_premium("Suite", [], 1)
    assert resultado == 115

def test_servicio_vip_aplica_recargo_premium_a_estandar():
    # Standard (50) + VIP Lounge (40) = 90.
    # Tiene servicio VIP, aplica 15% -> 90 * 1.15 = 103.5
    # 103.5 * 1 huesped = 103.5
    resultado = calculate_base_and_premium("Standard", ["VIP Lounge Access"], 1)
    assert resultado == 103.5



def test_validacion_correcta():
    # Datos válidos y confirmados deben retornar True
    assert validate_inputs("Standard", ["Spa Treatment"], True) is True

def test_validacion_cancelada_por_usuario(capsys):
    # Si no se confirma, retorna False y avisa en consola
    assert validate_inputs("Standard", [], False) is False
    captured = capsys.readouterr()
    assert "[Error]" in captured.out

def test_validacion_habitacion_inexistente():
    # Habitación que no existe en el catálogo debe fallar
    assert validate_inputs("HabitacionFalsa", [], True) is False
