import sys

def validar_argumentos():
    """Valida que se ingresen los argumentos correctos"""
    if len(sys.argv) != 5:
        print("Error: Debe ingresar 4 argumentos")
        print("Uso: python conversiones.py [sol] [peso_arg] [dolar] [monto_clp]")
        sys.exit(1)

def convertir_moneda(monto, tasas):
    """Realiza las conversiones de moneda"""
    conversiones = {
        "Soles": monto * tasas["sol"],
        "Pesos Argentinos": monto * tasas["peso_arg"],
        "Dólares": monto * tasas["dolar"]
    }
    return conversiones

def main():
    # Validar argumentos
    validar_argumentos()
    
    try:
        # Obtener tasas de conversión y monto
        tasas = {
            "sol": float(sys.argv[1]),
            "peso_arg": float(sys.argv[2]),
            "dolar": float(sys.argv[3])
        }
        monto_clp = float(sys.argv[4])
        
        # Realizar conversiones
        resultado = convertir_moneda(monto_clp, tasas)
        
        # Mostrar resultados
        print(f"Los {monto_clp:.0f} pesos equivalen a:")
        print(f"{resultado['Soles']:.1f} Soles")
        print(f"{resultado['Pesos Argentinos']:.1f} Pesos Argentinos")
        print(f"{resultado['Dólares']:.1f} Dólares")
        
    except ValueError:
        print("Error: Todos los argumentos deben ser números")
        sys.exit(1)

if __name__ == "__main__":
    main()