
from django.shortcuts import render
from django.http import JsonResponse
import telebot
from .bot import bot

def index(request):
    return render(request, 'telegram_bot/index.html')

def send_command(request):
    command = request.GET.get('command')
    address = request.GET.get('address')
    chat_id = '1762721715'  

    message = f"Pedido: {command}\nEndereço: {address}"
    bot.send_message(chat_id, message)

    return JsonResponse({'message': 'Pedido enviado!'})

def produto_detalhe(request, nome):
    produtos = {
        'Duplocheddar': {
            'nome': 'Duplo Cheddar',
            'descricao': 'Pão fofinho com gergelim, 2 hambúrgueres de carne 100% bovina grelhados no fogo como churrasco, o novo molho cremoso sabor queijo cheddar e toda a crocância da cebola crispy. 100% livre de corantes, conservantes e aromatizantes artificiais.',
            'imagem': 'telegram_bot/duplo_cheddar.jpeg',
            'preco': 'R$ 26,00'
        },
        'Especial_da_casa': {
            'nome': 'Especial da Casa',
            'descricao': 'Nosso hambúrguer especial com ingredientes secretos.',
            'imagem': 'telegram_bot/especial_da_casa.png',
            'preco': 'R$ 30,00'
        },
        'Artesanal': {
            'nome': 'Artesanal',
            'descricao': 'Hambúrguer artesanal com ingredientes frescos.',
            'imagem': 'telegram_bot/artesanal.png',
            'preco': 'R$ 28,00'
        },
       'chicken_catupiry': {
            'nome': 'Chicken Catupiry',
            'descricao': 'Hambúrguer artesanal com ingredientes frescos.',
            'imagem': 'telegram_bot/chicken_catupiry.png',
            'preco': 'R$ 28,00'
        },
        'stacker_duplo_bacon': {
            'nome': 'Stacker Duplo Bacon',
            'descricao': 'Dois hambúrgueres grelhados, cheddar fatiado e três fatias de bacon acompanhado do saboroso molho Stacker em um pão macio com gergelim.',
            'imagem': 'telegram_bot/stacker_duplo_bacon.png',
            'preco': 'R$ 28,00'
        },
    }
    produto = produtos.get(nome)
    if not produto:
        return render(request, '404.html')  # Redireciona para uma página 404 se o produto não for encontrado
    return render(request, 'telegram_bot/produto_detalhe.html', {'produto': produto})
