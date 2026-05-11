import json
import os # Vamos usar o os para verificar se o arquivo já existe

ARQUIVO_DIARIO = "diario_cognitivo.json"


from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.theme import Theme

# Customizando as cores do nosso sistema
custom_theme = Theme({
    "info": "italic cyan",
    "warning": "bold yellow",
    "danger": "bold red",
    "success": "bold green"
})

console = Console(theme=custom_theme)

DISTORCOES_COGNITIVAS = {
    "Generalização Excessiva": {
        "gatilhos": ["sempre", "nunca", "todo mundo", "ninguém"],
        "desafio": "Existem exceções a essa regra? Houve alguma vez em que isso não aconteceu?"
    },
    "Pensamento Tudo ou Nada": {
        "gatilhos": ["estraguei tudo", "perfeito", "fracasso", "nada"],
        "desafio": "A situação é realmente 0 ou 100, ou existe um meio-termo (cinza) aqui?"
    },
    "Catastrofização": {
        "gatilhos": ["horrível", "fim do mundo", "não vou aguentar", "pior"],
        "desafio": "Qual é a probabilidade real disso acontecer? Se acontecesse, como você lidaria?"
    }
}

def limpar_texto(texto):
    # Remove pontuação básica para não atrapalhar a busca das palavras
    for pontuacao in [".", ",", "!", "?", "(", ")"]:
        texto = texto.replace(pontuacao, "")
    return texto.lower()


def salvar_no_diario(novo_registro):
    """
    Esta função lê o arquivo existente, adiciona o novo pensamento
    e salva tudo de volta.
    """
    historico = []

    # 1. Se o arquivo já existir, a gente lê o que tem dentro primeiro
    if os.path.exists(ARQUIVO_DIARIO):
        with open(ARQUIVO_DIARIO, "r", encoding="utf-8") as f:
            historico = json.load(f)

    # 2. Adicionamos o novo registro à lista
    historico.append(novo_registro)

    # 3. Salvamos a lista atualizada no arquivo
    with open(ARQUIVO_DIARIO, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=4, ensure_ascii=False)

def analisar_pensamento():
    console.print(Panel.fit("[bold blue]CogniGuard v1.0[/bold blue]\n[italic]Monitor de Saúde Mental Baseado em TCC[/italic]"))
    
    pensamento_bruto = Prompt.ask("\n[info]O que está passando pela sua cabeça agora?[/info]")
    texto = limpar_texto(pensamento_bruto)
    
    encontrou = False
    
    with console.status("[bold green]Analisando padrões cognitivos..."):
        # Simulando um pequeno delay para parecer processamento real
        import time
        time.sleep(1)

        for distorcao, info in DISTORCOES_COGNITIVAS.items():
            for gatilho in info["gatilhos"]:
                if gatilho in texto:
                    console.print(Panel(
                        f"[danger]Distorção Detectada:[/danger] [bold]{distorcao}[/bold]\n"
                        f"[success]Desafio Socrático:[/success] {info['desafio']}",
                        title="[warning]Alerta de Viés[/warning]",
                        border_style="yellow"
                    ))
                    encontrou = True
                    break

    if not encontrou:
        console.print("[success]Nenhum padrão de distorção óbvio detectado. Continue monitorando seus sentimentos![/success]")

if __name__ == "__main__":
    analisar_pensamento()