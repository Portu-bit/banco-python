# Banco Python

Ejercicio de programación orientada a objetos que modela cuentas bancarias con depósitos, retiros y transferencias.

## Funcionalidades
- Crear cuentas con titular y saldo inicial.
- Depositar y retirar dinero.
- Transferir fondos entre cuentas.
- Consultar el saldo.
- Validar montos finitos y positivos.
- Usar `Decimal` para evitar errores comunes de precisión de `float`.
- Validar ambas cuentas antes de modificar saldos en una transferencia.

> Este proyecto es un simulador educativo en memoria. No conecta con bancos reales ni debe utilizarse para custodiar dinero.

## Requisitos
Python 3.10 o superior. Para ejecutar las pruebas, instala pytest:

```bash
python -m pip install pytest
```

## Ejecutar
```bash
python main.py
```

## Pruebas
```bash
python -m pytest -q
```
