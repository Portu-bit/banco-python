from decimal import Decimal, InvalidOperation

from .excepciones import SaldoInsuficienteError


class CuentaBancaria:
    """Cuenta bancaria en memoria con validación de montos."""

    def __init__(self, titular, saldo=0):
        if not isinstance(titular, str) or not titular.strip():
            raise ValueError("El titular no puede estar vacío.")
        self.titular = titular.strip()
        self.saldo = self._convertir_monto(saldo, "El saldo", permitir_cero=True)

    @staticmethod
    def _convertir_monto(cantidad, etiqueta="La cantidad", permitir_cero=False):
        if isinstance(cantidad, bool):
            raise ValueError(f"{etiqueta} debe ser un número válido.")
        try:
            monto = Decimal(str(cantidad))
        except (InvalidOperation, TypeError, ValueError):
            raise ValueError(f"{etiqueta} debe ser un número válido.") from None
        if not monto.is_finite():
            raise ValueError(f"{etiqueta} debe ser un número finito.")
        if monto < 0 or (not permitir_cero and monto == 0):
            condicion = "no puede ser negativo." if permitir_cero else "debe ser positivo."
            raise ValueError(f"{etiqueta} {condicion}")
        return monto

    def depositar(self, cantidad):
        monto = self._convertir_monto(cantidad, "El depósito")
        self.saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo:.2f}")
        return self.saldo

    def retirar(self, cantidad):
        monto = self._convertir_monto(cantidad, "El retiro")
        if monto > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar el retiro.")
        self.saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: {self.saldo:.2f}")
        return self.saldo

    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.titular} es: {self.saldo:.2f}")
        return self.saldo

    def transferir(self, cantidad, cuenta_destino):
        monto = self._convertir_monto(cantidad, "La transferencia")
        if not isinstance(cuenta_destino, CuentaBancaria):
            raise ValueError("La cuenta de destino no es válida.")
        if cuenta_destino is self:
            raise ValueError("No puedes transferir dinero a la misma cuenta.")
        if monto > self.saldo:
            raise SaldoInsuficienteError(
                "Saldo insuficiente para realizar la transferencia."
            )

        # Both balances are changed only after all validations succeed.
        self.saldo -= monto
        cuenta_destino.saldo += monto
        print(
            f"Transferencia de {monto:.2f} a {cuenta_destino.titular} exitosa. "
            f"Nuevo saldo: {self.saldo:.2f}"
        )
        return self.saldo
