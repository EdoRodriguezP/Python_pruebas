#numero = 345            # numero ingresado

numero = int(input("ingresa un numero"))

if numero % 2 == 0:     # modulo da el resto de la division en entero, si es 0 se impime par

    print(f"el numero  :{numero} . ingtresado es par")
else:
    print(f"el numero  :{numero} . ingtresado es impar")