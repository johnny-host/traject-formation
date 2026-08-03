def calculadora():
    print("=== Calculadora Simples ===")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

    opcao = input("Escolha a operação (1/2/3/4): ")

    if opcao not in ("1", "2", "3", "4"):
        print("Opção inválida.")
        return

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Digite apenas números válidos.")
        return

    if opcao == "1":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcao == "2":
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcao == "3":
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif opcao == "4":
        if num2 == 0:
            print("Erro: Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")


if __name__ == "__main__":
    calculadora()