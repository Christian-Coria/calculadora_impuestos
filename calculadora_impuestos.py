print("Calculadora de Impuestos".center(50,"."))

pago = int(input("introduzca el valor del pago sin impuesto: "))
impuesto = int(input("introduzca el monto del impuesto: "))

def calcular_impuesto(pago,impuesto):
    pago_final = pago + pago * impuesto / 100
    return pago_final


pago_con_impuestos = calcular_impuesto(pago,impuesto)
print(f"pago con inpuesto {pago_con_impuestos}")
print("...finalizando...".center(50,"*"))