def calcular_consumo(distancia, combustivel_gasto):
    consumo_medio = round(distancia / combustivel_gasto, 2)

    print("=== Relatório de Consumo de Combustível ===")
    print(f"Distância percorrida: {distancia:.2f} km")
    print(f"Combustível gasto: {combustivel_gasto:.2f} litros")
    print(f"Consumo médio: {consumo_medio:.2f} km/l")

if __name__ == "__main__":
    distancia_percorrida = 300  # km
    combustivel_utilizado = 25  # litros

    calcular_consumo(distancia_percorrida, combustivel_utilizado)
