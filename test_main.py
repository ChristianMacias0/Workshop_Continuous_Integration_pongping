"""Pruebas unitarias para el sistema de reservas del hotel."""
# pylint: disable=import-error
import pytest
from main import calculate_base_and_premium, validate_inputs

def test_habitacion_estandar_sin_servicios():
    """Valida el costo base de una habitacion estandar sin servicios extra."""
    resultado = calculate_base_and_premium("Standard", [], 1)
    assert resultado == 50

def test_habitacion_estandar_con_un_servicio():
    """Valida el costo de habitacion estandar sumando un servicio basico."""
    resultado = calculate_base_and_premium("Standard", ["Spa Treatment"], 2)
    assert resultado == 160

def test_habitacion_suite_aplica_recargo_premium():
    """Comprueba que las habitaciones de tipo Suite apliquen el 15% premium."""
    resultado = calculate_base_and_premium("Suite", [], 1)
    assert resultado == 115

def test_servicio_vip_aplica_recargo_premium_a_estandar():
    """Verifica que el servicio VIP aplique el 15% de recargo a una estandar."""
    resultado = calculate_base_and_premium("Standard", ["VIP Lounge Access"], 1)
    assert resultado == pytest.approx(103.5)

def test_validacion_correcta():
    """Confirma que las entradas validas devuelvan un estado verdadero."""
    assert validate_inputs("Standard", ["Spa Treatment"], True) is True

def test_validacion_cancelada_por_usuario(capsys):
    """Evalua que una cancelacion explicita retorne falso y muestre alerta."""
    assert validate_inputs("Standard", [], False) is False
    captured = capsys.readouterr()
    assert "[Error]" in captured.out

def test_validacion_habitacion_inexistente():
    """Asegura que el sistema rechace habitaciones fuera del catalogo."""
    assert validate_inputs("HabitacionFalsa", [], True) is False
