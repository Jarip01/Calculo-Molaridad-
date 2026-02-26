# Leer datos
masa_soluto = float(input("Ingresa la masa del soluto (g): "))
masa_molar = float(input("Ingresa la masa molar (g/mol):"))
volumen_ml = float(input("Ingresa el volumen de la solución (ml): "))

# Convertir el volumen a litros

volumen_l = volumen_ml / 1000

# Calcular los moles del soluto

moles = masa_soluto / masa_molar


# Calcular la molaridad (Proceso)
molaridad = moles / volumen_l

# Mostrar el resultado (Salida)
print("\nResultado:")
print(f"La molaridad de la solución es: {molaridad:.4f} M")