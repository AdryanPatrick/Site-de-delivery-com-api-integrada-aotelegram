# telegram_bot/bot.py
import telebot

CHAVE_API = "7162157086:AAHdBjaW_Oi1r3fk2Xbepb3xpwzfz7bgeGQ"
bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["Duplocheddar"])
def duplo_cheddar(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza pra sua casa: Tempo de espera em 20min")

@bot.message_handler(commands=["Especial_da_casa"])
def Especial_da_casa(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo: em 10min chega ai")

@bot.message_handler(commands=["Artesanal"])
def Artesanal(mensagem):
    bot.send_message(mensagem.chat.id, "Não tem salada não, clique aqui para iniciar: /iniciar")

@bot.message_handler(commands=["chicken_catupiry"])
def chicken_catupiry(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo: em 10min chega ai")

@bot.message_handler(commands=["stacker_duplo_bacon"])
def stacker_duplo_bacon(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo: em 10min chega ai")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /duplo_cheddar Duplocheddar
    /especial_da_casa Especial_da_casa
    /chicken_catupiry chicken_catupiry
    /stacker_duplo_bacon stacker_duplo_bacon
    /artesanal Artesanal"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamacao@balbalba.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! Patrick mandou um abraço de volta")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um abraço pro Patrick
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

def iniciar_bot():
    bot.polling()

