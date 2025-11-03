# Gerador de Cartelas de Bingo | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Este projeto Python permite gerar cartelas de bingo tradicionais com números de 1 a 75, seguindo as regras clássicas do jogo. O script gera n cartelas de bingo 5x5 com números aleatórios distribuídos por colunas (B: 1-15, I: 16-30, N: 31-45, G: 46-60, O: 61-75), uma imagem personalizada no centro, e as salva em um único arquivo PDF.

### Requisitos
- Python 3.x
- Bibliotecas Python necessárias:
    - pandas
    - reportlab

> Você pode instalar as dependências usando
 `pip install -r requirements.txt`

### Tutorial de uso

Para personalizar suas cartelas:
1. Substituir o arquivo [logo.png](conteudo/logo.png) pela imagem desejada a ser acrescentada no centro da cartela. A imagem será redimensionada automaticamente para 50x50 pixels.

Para executar o código e gerar as cartelas, basta digitar no seu terminal:
`python script.py`

O script solicitará a quantidade de cartelas que deseja gerar e criará um arquivo PDF (`cartelas.pdf`) com todas as cartelas organizadas em páginas (3 cartelas por página, 3 por linha).

