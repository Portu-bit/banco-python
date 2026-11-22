from decimal import Decimal

import pytest

from src.cuenta import CuentaBancaria
from src.excepciones import SaldoInsuficienteError


def test_account_uses_decimal_and_validates_owner():
    account = CuentaBancaria("  Ana  ", "100.10")
    assert account.titular == "Ana"
    assert account.saldo == Decimal("100.10")
    with pytest.raises(ValueError):
        CuentaBancaria(" ", 0)


@pytest.mark.parametrize("amount", [0, -1, True, "abc", float("nan"), float("inf")])
def test_deposit_rejects_invalid_amounts(amount):
    account = CuentaBancaria("Ana", 100)
    with pytest.raises(ValueError):
        account.depositar(amount)
    assert account.saldo == Decimal("100")


def test_deposit_and_withdraw_update_balance():
    account = CuentaBancaria("Ana", 100)
    account.depositar("25.50")
    account.retirar(10)
    assert account.saldo == Decimal("115.50")


def test_withdraw_rejects_insufficient_funds_without_mutation():
    account = CuentaBancaria("Ana", 20)
    with pytest.raises(SaldoInsuficienteError):
        account.retirar(21)
    assert account.saldo == Decimal("20")


def test_transfer_updates_both_accounts():
    source = CuentaBancaria("Ana", 100)
    destination = CuentaBancaria("Luis", 5)
    source.transferir("30.25", destination)
    assert source.saldo == Decimal("69.75")
    assert destination.saldo == Decimal("35.25")


def test_transfer_is_atomic_when_validation_fails():
    source = CuentaBancaria("Ana", 100)
    destination = CuentaBancaria("Luis", 5)
    with pytest.raises(SaldoInsuficienteError):
        source.transferir(200, destination)
    assert source.saldo == Decimal("100")
    assert destination.saldo == Decimal("5")


def test_transfer_rejects_invalid_destination_and_same_account():
    account = CuentaBancaria("Ana", 100)
    with pytest.raises(ValueError):
        account.transferir(10, object())
    with pytest.raises(ValueError):
        account.transferir(10, account)
    assert account.saldo == Decimal("100")


def test_withdraw_rejects_invalid_amounts():
    account = CuentaBancaria("Ana", 100)
    for amount in (0, -5, True, "not a number"):
        with pytest.raises(ValueError):
            account.retirar(amount)
    assert account.saldo == Decimal("100")
