import pytest
from calculate import calc


def test_calc_square_area():
    assert calc('square', 'area', [4]) == 16


def test_calc_square_perimeter():
    assert calc('square', 'perimeter', [4]) == 16


def test_calc_circle_area():
    assert pytest.approx(calc('circle', 'area', [3]), 0.01) == 28.27


def test_calc_circle_perimeter():
    assert pytest.approx(calc('circle', 'perimeter', [3]), 0.01) == 18.85


def test_calc_invalid_figure():
    with pytest.raises(ValueError):
        calc('figure', 'area', [3])


def test_calc_invalid_function():
    with pytest.raises(ValueError):
        calc('circle', 'volume', [3])


def test_calc_invalid_size():
    with pytest.raises(ValueError):
        calc('circle', 'area', [3, 4])


def test_calc_triangle_not_supported():
    with pytest.raises(ValueError):
        calc('triangle', 'area', [3, 4, 5])
