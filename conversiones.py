precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}


def filtro(productos:dict[str,int],umbral:int, modo:str = "mayor"):
    if modo == "mayor":
        for k, v in productos.items():
            print(k,v)