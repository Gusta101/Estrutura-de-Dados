class Item:
    def __init__(self, dados):
        self.estado = False
        self.dados = dados # Tupla chave valor "(chave, valor)", sendo valor, o endereço do objeto na memória (Funcionario ou Projeto)
        self.next = None # Próximo item "(ponteiro)"

class ListaEncadeada:
    def __init__(self):
        self.head = None
    
    def inserir(self, dados):
        novo_item = Item(dados)
        if not self.head:
            novo_item.estado = True
            self.head = novo_item
            return
        atual = self.head
        while atual.next:
            atual = atual.next
        novo_item.estado = True
        atual.next = novo_item