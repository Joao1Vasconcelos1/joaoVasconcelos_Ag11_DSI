# Programa em Python que tem como objetivo exibir mensagens de alerta 
# com cores diferentes, conforme o nível de água do reservatório.
# Autor: JV


# -------------------------------------
# Processamento (definição da situação)
# -------------------------------------

# Verifica a situação do nível do reservatório em litros.
# Retorna None se algum valor for inválido (não está entre 0 e 1000).

def verificar_nivel(litros_reservatorio):

    if litros_reservatorio is None:
        return None

    elif litros_reservatorio < 0 or litros_reservatorio > 1000:
        return None

    elif 0 <= litros_reservatorio <= 200:
        situacao = "Nível 1"

    elif 201 <= litros_reservatorio <= 400:
        situacao = "Nível 2"

    elif 401 <= litros_reservatorio <= 600:
        situacao = "Nível 3"

    elif 601 <= litros_reservatorio <= 800:
        situacao = "Nível 4"

    elif 801 <= litros_reservatorio <= 1000:
        situacao = "Nível 5"

    return situacao

# Aqui está sendo importados apenas os recursos necessários para 
# controlar a cor do texto exibido no terminal

from colorama import Fore, Style

# Exibe apenas um relatório simples (não retorna nenhum valor).

def exibir_relatorio(litros_reservatorio):
    situacao = verificar_nivel(litros_reservatorio)

    if situacao is None:
        print(Fore.WHITE + "Erro ao gerar relatório do nível de água no reservatório.")
    elif situacao == "Nível 1":
        print(Fore.RED + "Nível 1 - Situação: muito baixa (crítico)")
    elif situacao == "Nível 2":
        print(Fore.YELLOW + "Nível 2 - Situação: baixa")
    elif situacao == "Nível 3":
        print(Fore.GREEN + "Nível 3 - Situação: média")
    elif situacao == "Nível 4":
        print(Fore.CYAN + "Nível 4 - Situação: alta")
    elif situacao == "Nível 5":
        print(Fore.BLUE + "Nível 5 - Situação: muito alta (alerta)")

# Aqui restaura o estilo padrão, evitando que as configurações de cor 
# permaneçam ativas após a execução do programa.

print(Style.RESET_ALL)


# --------------------------------
# Saída - Exibição das informações
# --------------------------------

# ---------------- Simulação ----------------

exibir_relatorio(litros_reservatorio = 830.02)
exibir_relatorio(litros_reservatorio = 1100)
exibir_relatorio(litros_reservatorio = 520)

