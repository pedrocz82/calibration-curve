"""
Tests for Calibration Curve class
command_line: python -m pytest tests/test_calibration_curve.py
"""

import pytest

from app.models import calibration_curve


@pytest.fixture
def cc_values():
    return {
        'absorbance': [0.20, 0.40, 0.60, 0.80, 1.00, 1.2],
        'concentration': [0.1516, 0.3826, 0.4281, 0.6545, 0.7118, 0.9565]
    }


@pytest.fixture
def cc(cc_values):
    return calibration_curve.CalibrationCurve(**cc_values)


def test_create_cc(cc, cc_values):
    for attr_name in cc_values:
        print('getattr(cc, attr_name)')
        print(getattr(cc, attr_name))
        assert getattr(cc, attr_name) == cc_values.get(attr_name)


def test_a(cc):
    assert cc.a == pytest.approx(0.6816715006305171, rel=1e-4)


def test_b(cc):
    assert cc.b == pytest.approx(0.03313303909205536, rel=1e-4)


def test_concentration(cc):
    assert cc(2) == pytest.approx(1.3964760403530896, rel=1e-4)
