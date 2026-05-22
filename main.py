#crear cuenta bancaria
from src.excepciones import SaldoInsuficienteError
from src.cuenta import CuentaBancaria
def main():
    try:
        cuenta = CuentaBancaria("Juan Pérez", 1000)
        cuenta.mostrar_saldo()
        cuenta.depositar(500)
        cuenta.retirar(200)
        cuenta.mostrar_saldo()
    except ValueError as ve:
        print(f"Error: {ve}")
    except SaldoInsuficienteError as sie:
        print(f"Error de saldo insuficiente: {sie}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()