"""Pruebas unitarias para el sistema de membresías del gimnasio."""

# pylint: disable=import-error
from main import calculate_membership_cost, validate_inputs

def test_plan_basico_sin_extras():
    """Valida el costo de un plan básico para un solo miembro sin características extra."""
    resultado = calculate_membership_cost("Basic", [], 1)
    assert resultado == 30

def test_recargo_premium_y_oferta_especial():
    """Verifica recargo del 15% por plan premium y el descuento de $20 al superar los $200."""
    # Premium base: 80. + Personal Training (50) = 130.
    # Es Premium -> 130 * 1.15 = 149.5
    # Son 2 miembros -> 149.5 * 2 = 299.
    # Descuento grupal (10%) -> 299 * 0.90 = 269.1
    # Supera $200, se restan $20 -> 269.1 - 20 = 249.1 -> Se redondea a 249
    resultado = calculate_membership_cost("Premium", ["Personal Training"], 2)
    assert resultado == 249

def test_descuento_mayor_a_400():
    """Asegura que se aplique el descuento de $50 al superar los $400 en total."""
    # Family base: 120. + Group Classes (25) = 145.
    # Son 4 miembros -> 145 * 4 = 580.
    # Descuento grupal 10% -> 580 * 0.90 = 522.
    # Supera $400, se restan $50 -> 522 - 50 = 472.
    resultado = calculate_membership_cost("Family", ["Group Classes"], 4)
    assert resultado == 472

def test_plan_invalido_retorna_menos_uno():
    """Garantiza que ingresar un plan que no existe en el catálogo devuelva -1."""
    resultado = calculate_membership_cost("PlanFalso", [], 1)
    assert resultado == -1

def test_cancelacion_retorna_menos_uno(capsys):
    """Revisa que una cancelación explícita devuelva -1 y emita el error en consola."""
    resultado = calculate_membership_cost("Basic", [], 1, confirmed=False)
    assert resultado == -1
    captured = capsys.readouterr()
    assert "[Error]" in captured.out

def test_validacion_correcta():
    """Confirma que ingresar datos válidos devuelva un estado verdadero."""
    assert validate_inputs("Basic", ["Sauna Access"], True) is True

def test_validacion_cancelada_por_usuario(capsys):
    """Evalúa que una cancelación explícita retorne falso y muestre alerta."""
    assert validate_inputs("Basic", [], False) is False
    captured = capsys.readouterr()
    assert "[Error]" in captured.out

def test_validacion_plan_inexistente():
    """Asegura que el sistema rechace planes fuera del catálogo."""
    assert validate_inputs("PlanFalso", [], True) is False

def test_validacion_servicio_inexistente():
    """Asegura que el sistema rechace servicios extra fuera del catálogo."""
    assert validate_inputs("Basic", ["ServicioFalso"], True) is False
