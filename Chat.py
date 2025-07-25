import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()
    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        ("curiosidades", "curiosidade"): 'Sabias que os polvos têm três corações?',
        ('uma piada', 'faz-me rir'): 'Por que o livro de matemática se suicidou? Porque tinha muitos problemas!',
        ("obrigado", "obrigada"): 'De nada! Estou aqui para ajudar.',
        ('voce é um bot?', 'tu és um bot?'): 'Sim, sou um bot criado para conversar contigo.',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',}
    
    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta
        
    if comando == 'como te chamas?':
        return 'O meu nome é: Bot :)'
    
    if comando == 'tempo':
        return 'Está um dia de sol!'
    
    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'
    
    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    return f'Desculpa, não entendi a questão! {texto}\n'

def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()