import pytest

from card_validator.validator import get_issuer


def test_get_issuer_visa():
    assert get_issuer("4243 4312 5342 1231") == 'Visa'


def test_get_issuer_master():
    assert get_issuer("5143 4312 5342 1216") == 'MasterCard'
    with pytest.raises(ValueError):
        get_issuer("5643 4312 5342 1231")


def test_get_issuer_amex():
    assert get_issuer("3443 4312 5342 123") == 'American Express'
    with pytest.raises(ValueError):
        get_issuer("3643 4312 5342 1231")


def test_length():
    with pytest.raises(ValueError):
        get_issuer("3443 4312 5342 1231")

    with pytest.raises(ValueError):
        get_issuer("3643 4312 5342 1231")

    assert get_issuer("3443 4312 5342 123") == 'American Express'
