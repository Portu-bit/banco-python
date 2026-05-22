from .excepciones import SaldoInsuficienteError

class CuentaBancaria:
    def __init__(self, titular, saldo):
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.titular = titular
        self.saldo = saldo


    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva")
        self.saldo += cantidad
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo:.2f}")
    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva")
        if cantidad > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar el retiro")
        self.saldo -= cantidad
        print(f"Retiro exitoso. Nuevo saldo: {self.saldo:.2f}")
    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.titular} es: {self.saldo:.2f}")
        
    def transferir(self, cantidad, cuenta_destino):
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva")
        if cantidad > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar la transferencia")
        self.retirar(cantidad)
        cuenta_destino.depositar(cantidad)
        print(f"Transferencia exitosa. Nuevo saldo: {self.saldo:.2f}")
        