def inverter_string(s):
    string_invertida = ""
    for caractere in s:
        string_invertida = caractere + string_invertida
    return string_invertida

entrada_usuario = input("Digite uma string para inverter: ")

resultado = inverter_string(entrada_usuario)

print(f"String original: {entrada_usuario}")
print(f"String invertida: {resultado}")
