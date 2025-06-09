import os
import time
from dataclasses import dataclass

os.system("cls || clear")

def limpar():
    os.system("cls || clear")

# Abrindo lista.
estoque = [
    {'nome': 'Arroz', 'codigo': '001', 'quantidade': 50, 'preco': 5.50},
    {'nome': 'Feijão', 'codigo': '002', 'quantidade': 30, 'preco': 7.00},
    {'nome': 'Leite', 'codigo': '003', 'quantidade': 100, 'preco': 7.00},
    {'nome': 'Pão', 'codigo': '004', 'quantidade': 200, 'preco': 0.50},
    {'nome': 'Óleo', 'codigo': '005', 'quantidade': 25, 'preco': 6.99},
    {'nome': 'Açúcar', 'codigo': '006', 'quantidade': 40, 'preco': 4.00},
    {'nome': 'Café', 'codigo': '007', 'quantidade': 15, 'preco': 7.99},
    {'nome': 'Macarrão', 'codigo': '008', 'quantidade': 60, 'preco': 3.29},
    {'nome': 'Sabão em pó', 'codigo': '009', 'quantidade': 20, 'preco': 4.79},
    {'nome': 'Detergente', 'codigo': '010', 'quantidade': 50, 'preco': 1.99}
]

lista_novos = []

# Criando uma classe
@dataclass
class Produto:
    nome: str
    codigo: int
    quantidade: int
    preco: float

def adicionando_produto(lista_novos):       # Criando uma função para adicionar um produto.
    nome = input("\nDigite o nome do produto que deseja adicionar: ")
    codigo = int(input("Digite o código do produto que deseja adicionar: "))
    quantidade = int(input("Informe o quantidade de produtos: "))  # Corrigido para inteiro
    preco = float(input("Digite o preço unitário do produto: "))  # Corrigido para float
    
    produto = Produto( 
        nome=nome,
        codigo=codigo,
        quantidade=quantidade,
        preco=preco
    )
    
    print(f"\nProduto '{produto.nome}' adicionado.")
    lista_novos.append(produto)
    time.sleep(3)
import time

def mostrar_produtos(estoque):          # Função para mostrar os produtos que já existiam no estoque.
    if not estoque:  # Verificar se o estoque está vazio
        print("\nEstoque vazio.") 
        return  # Se estiver vazio, sai da função

    for produto in estoque:
        print(f"Nome: {produto['nome']}")
        print(f"Código: {produto['codigo']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço unitário: {produto['preco']:.2f}")  # Formatação de preço com 2 casas decimais
        print("-" * 30)
    
    time.sleep(10)  # Pausa após mostrar todos os produtos


def listar_produtos(lista_novos):           # Criando uma função para listar os produtos que irão ser adicionados. 
    if not lista_novos:
        print("\nNão há produtos em lista_novos.")
    else:
        print(f"\n- Lista de Produtos -")
        for produto in lista_novos:
         print(f"\nNome: {produto.nome}\nCódigo: {produto.codigo}\nQuantidade: {produto.quantidade}\nPreço: {produto.preco}\n")

def excluir_produto(lista_novos):           # Função para listar os produtos.
    listar_produtos(lista_novos)
    nome_remove = input(f"\nDigite o nome do produto: ")
    for produto in lista_novos:
        if produto.nome == nome_remove:  
            lista_novos.remove(produto)
            print(f"O produto '{nome_remove}' foi removido com sucesso.")
            return
    print(f"O produto {nome_remove} não foi encontrado.")

def atualizar_estoque(lista_novos):         # Função para atualizar os produtos do lista_novos.
    listar_produtos(lista_novos)
    nome_antigo = input(f"\nDigite o nome do produto que deseja atualizar dentro do lista_novos: ")
    for produto in lista_novos:
        if produto.nome == nome_antigo:
            novo_nome = input(f"\nDigite o novo nome para o produto '{nome_antigo}': ")
            produto.nome = novo_nome
            produto.codigo = int(input(f"Digite o novo código para '{novo_nome}': "))
            produto.quantidade = int(input(f"Digite a nova quantidade para '{novo_nome}': "))
            produto.preco = float(input(f"Digite o novo preço para '{novo_nome}': "))
            print(f"\nO produto '{nome_antigo}' foi atualizado com sucesso para '{novo_nome}'.")
            return
    print(f"\nO produto '{nome_antigo}' não foi encontrado.")

def adicionar_ao_estoque(estoque, lista_novos):
    if not lista_novos:
        print("\nNão há produtos para adicionar ao estoque.")
        return
    
    for produto in lista_novos:
        encontrado = False
        for item in estoque:
            if item['codigo'] == str(produto.codigo): 
                item['quantidade'] += produto.quantidade  # Atualizando a quantidade
                print(f"Produto '{produto.nome}' já existe no estoque. Quantidade atualizada.")
                encontrado = True
                break
        
        if not encontrado:
            estoque.append({
                'nome': produto.nome,
                'codigo': str(produto.codigo),  # Convertendo para string se necessário
                'quantidade': produto.quantidade,
                'preco': produto.preco
            })
            print(f"\nO produto {produto.nome} foi adicionado ao estoque.")
    
    lista_novos.clear()  # Limpa a lista de novos produtos após adicionar ao estoque
    time.sleep(3)

# Mostrando menu
while True:
    print("""
- Menu do Estoque -
1- Mostrar os produtos em estoque
2- Adicionar produto ao lista_novos 
3- Listar produtos a serem adicionados
4- Atualizar a lista
5- Excluir produto
6- Adicionar produto ao estoque
7- Fechar o programa
""")
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            mostrar_produtos(lista_novos)
        case 2:
            limpar()            
            adicionando_produto(lista_novos)
        case 3:
            limpar()
            listar_produtos(lista_novos)
        case 4:
            limpar()
            atualizar_estoque(lista_novos)
        case 5:
            limpar()
            excluir_produto(lista_novos)
        case 6:
            adicionar_ao_estoque(estoque, lista_novos)
        case 7:
            os.system("cls || clear")
            break
        case _:
            print("Opção inválida.")
    
    if opcao != 1:
        time.sleep(3.2)
    os.system("cls || clear")