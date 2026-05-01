from steampy import (
    carregar_jogos,
    listar_jogos,
    buscar_jogo_por_nome,
    filtrar_por_genero,
    filtrar_por_console,
    filtrar_por_nota,
    filtrar_por_vendas,
    filtrar_por_publisher,
    ordenar_jogos,
    adicionar_ao_backlog,
    mostrar_backlog,
    jogar_proximo,
    mostrar_recentes,
    retomar_ultimo_jogo,
    mostrar_historico,
    carregar_backlog,
    carregar_historico,
    carregar_recentes,
    salvar_backlog,
    salvar_recentes,
    indice_jogos,
)

DATA_FILE = 'dataset.csv'


def mostrar_menu():
    print('\n=== SteamPy - Projeto 3 ===')
    print('1. Listar jogos')
    print('2. Buscar jogo por nome')
    print('3. Filtrar por gênero')
    print('4. Filtrar por console')
    print('5. Filtrar por nota mínima')
    print('6. Filtrar por vendas mínimas')
    print('7. Filtrar por publisher')
    print('8. Ordenar jogos')
    print('9. Mostrar backlog')
    print('10. Jogar próximo do backlog')
    print('11. Mostrar jogos recentes')
    print('12. Retomar último jogo')
    print('13. Mostrar histórico')
    print('14. Adicionar jogo ao backlog')
    print('15. Salvar e sair')


def ler_opcao():
    return input('Escolha uma opção: ').strip()


def carregar_dados():
    carregar_jogos(DATA_FILE)
    carregar_backlog()
    carregar_historico()
    carregar_recentes()


def opcao_buscar():
    termo = input('Digite o nome ou parte do nome: ').strip()
    buscar_jogo_por_nome(termo)


def opcao_filtrar_genero():
    genero = input('Digite o gênero: ').strip()
    filtrar_por_genero(genero)


def opcao_filtrar_console():
    console = input('Digite o console: ').strip()
    filtrar_por_console(console)


def opcao_filtrar_nota():
    try:
        nota = float(input('Digite a nota mínima: ').strip())
    except ValueError:
        print('Valor inválido.')
        return
    filtrar_por_nota(nota)


def opcao_filtrar_vendas():
    try:
        vendas = float(input('Digite o mínimo de vendas: ').strip())
    except ValueError:
        print('Valor inválido.')
        return
    filtrar_por_vendas(vendas)


def opcao_filtrar_publisher():
    publisher = input('Digite a publisher: ').strip()
    filtrar_por_publisher(publisher)


def opcao_ordenar():
    print('Critérios: titulo, nota, vendas, data, console, genero')
    criterio = input('Digite o critério de ordenação: ').strip().lower()
    ordenar_jogos(criterio)


def opcao_adicionar_backlog():
    try:
        id_jogo = int(input('Digite o ID do jogo: ').strip())
    except ValueError:
        print('ID inválido.')
        return
    jogo = indice_jogos.get(id_jogo)
    if jogo is None:
        print('Jogo não encontrado.')
        return
    adicionar_ao_backlog(jogo)


def main():
    carregar_dados()

    while True:
        mostrar_menu()
        opcao = ler_opcao()

        if opcao == '1':
            listar_jogos()
        elif opcao == '2':
            opcao_buscar()
        elif opcao == '3':
            opcao_filtrar_genero()
        elif opcao == '4':
            opcao_filtrar_console()
        elif opcao == '5':
            opcao_filtrar_nota()
        elif opcao == '6':
            opcao_filtrar_vendas()
        elif opcao == '7':
            opcao_filtrar_publisher()
        elif opcao == '8':
            opcao_ordenar()
        elif opcao == '9':
            mostrar_backlog()
        elif opcao == '10':
            jogar_proximo()
        elif opcao == '11':
            mostrar_recentes()
        elif opcao == '12':
            retomar_ultimo_jogo()
        elif opcao == '13':
            mostrar_historico()
        elif opcao == '14':
            opcao_adicionar_backlog()
        elif opcao == '15':
            salvar_backlog()
            salvar_recentes()
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
