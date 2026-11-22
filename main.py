from src.cuenta import CuentaBancaria
from src.excepciones import SaldoInsuficienteError


def main():
    try:
        cuenta = CuentaBancaria("Juan Pérez", 1000)
        cuenta.mostrar_saldo()
        cuenta.depositar(500)
        cuenta.retirar(200)
        cuenta.mostrar_saldo()

        cuenta_destino = CuentaBancaria("María López", 0)
        cuenta.transferir(100, cuenta_destino)
        cuenta_destino.mostrar_saldo()
    except (ValueError, SaldoInsuficienteError) as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
