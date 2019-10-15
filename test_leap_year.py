import pytest

import main

PROPER_YEARS = (2000, 1996, 2008)
WRONG_YEARS = (1997, 2001, 1900)
WRONG_INPUTS = (13.12, "Adam")


@pytest.mark.parametrize("p_proper_year", PROPER_YEARS)
def test_proper_year(p_proper_year):
    assert main.check_year_leap(p_proper_year)


@pytest.mark.parametrize("p_wrong_year", WRONG_YEARS)
def test_wrong_year(p_wrong_year):
    assert not main.check_year_leap(p_wrong_year)


@pytest.mark.parametrize("p_wrong_input", WRONG_INPUTS)
def test_wrong_input(p_wrong_input):
    assert main.check_year_leap(p_wrong_input) == "Wrong Input"
