# Titulo:
# Botã0 de iniciar chat
# clicou no botão aparece um popup(Janela/modal)
# Titulo: Bem vindo
# Campo: Escreve seu no
# Botaã: Entrar no chat
# Carregar chat
# Embaixo do chat
# Campo: digite seu menssagem
# Botão: Enviar
# Flet: Framework do python(conjunto de ferramentoas construida para resolver um objetico exclusivo/ cria um aplicativo e um site)
# django
# flask
# Instalar flet: pip install flet
# 3 passos para criar site e aplicativo
# 1º Importar o flet
import flet as ft

# 2º Criar uma função(criar o código inteiro dentro da função)


def main(pagina):
    texto = ft.Text('ChatZapp')
    # Adicionar algo a pagina

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        print(mensagem)

        # Add a mensagem o chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    # Tunel de comunicação
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print('Enviar mensagem')
        pagina.pubsub.send_all(f'{nome_usuario.value}: {campo_mensagem.value}')
        # Limpe o campo mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(
        label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    def entrar_chat(evento):
        print('Entrar chat')
        # Fechar popup
        popup.open = False
        # tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        # Tirar o titulo "ChatZapp"
        pagina.remove(texto)
        # Criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f'{nome_usuario.value} entrou no chat')
        # append função que permite você adicionar itens em uma lista
        # chat.controls.append(texto_entrada)
        # Colocar o campo de digitar a mensagem
        # Criar botaão d enviar
        pagina.add(linha_enviar)
        pagina.update()

    # Botão de iniciar chat
    # Titulo do Popup
    titulo_popup = ft.Text('Bem vindo ao ChatZapp')
    # Campo para escrever o e-mail
    nome_usuario = ft.TextField(
        label='Escreva seu nome', on_submit=entrar_chat)
    # Button
    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )
# toda função atribuida co buttão, tem que receber como parametro um evento

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        # Sempre que editar a pagina depois que a pagína ja estiver carregada, você tem que autualizar o vizual da página
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup)
    # clicou no botão aparece um popup(Janela/modal)
    # Titulo: Bem vindo
    # Campo: Escreve seu no
    # Botaã: Entrar no chat
    pagina.add(texto)
    pagina.add(botao_iniciar)


# 3º Rodar o aplicativo
# Criar o app chamando a função principal
ft.app(target=main, view=ft.WEB_BROWSER)
