"""
Tests for Calibration Curve class
command_line: python -m pytest tests/test_calibration_curve.py
"""

import pytest

from app.models import calibration_curve


@pytest.fixture
def cc_values():
    return {
        'absorbance': [0.1516, 0.3826, 0.4281, 0.6545, 0.7118, 0.9565],
        'concentration': [0.20, 0.40, 0.60, 0.80, 1.00, 1.2]
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
    assert cc.a == pytest.approx(1.296948404730149, rel=1e-4)


def test_b(cc):
    assert cc.b == pytest.approx(-0.010100867396502676, rel=1e-4)


def test_r_squared(cc):
    assert cc.r_squared == pytest.approx(0.9705806025969832, rel=1e-4)


def test_concentration(cc):
    assert cc(2) == pytest.approx(2.5837959420637, rel=1e-4)
