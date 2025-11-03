import random

from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet



"""Returns number ranges for each BINGO column following traditional rules"""
def gerar_numeros_bingo():
    # Define number ranges for each column
    faixas = {
        'B': list(range(1, 16)),    # 1-15
        'I': list(range(16, 31)),  # 16-30
        'N': list(range(31, 46)),  # 31-45
        'G': list(range(46, 61)),  # 46-60
        'O': list(range(61, 76))   # 61-75
    }
    return faixas


"""Generates a 5x5 BINGO card with numbers following traditional rules"""
def gerar_cartela():
    faixas = gerar_numeros_bingo()
    
    # Create the first row of the card (header)
    cartela = [["B", "I", "N", "G", "O"]]  # First row with BINGO
    
    # Generate 5 unique numbers for each column
    colunas = []
    for coluna in ['B', 'I', 'N', 'G', 'O']:
        numeros_coluna = random.sample(faixas[coluna], 5)
        colunas.append(numeros_coluna)
    
    # Transpose columns to form card rows
    for linha in range(5):
        linha_cartela = []
        for coluna in range(5):
            linha_cartela.append(colunas[coluna][linha])
        cartela.append(linha_cartela)
    
    # Mark the center as free (row index 3, column index 2)
    cartela[3][2] = "LIVRE"
    
    return cartela


"""Generates n BINGO cards and saves them all in a single PDF"""
def salvar_cartelas_pdf(num_cartelas, imagem, nome_arquivo="cartelas.pdf"):
    pdf = canvas.Canvas(nome_arquivo, pagesize=landscape(letter))
    largura, altura = landscape(letter)
    
    # Text styles for automatic line breaks
    estilos = getSampleStyleSheet()
    estilo_celula = estilos["Normal"]
    estilo_celula.fontName = "Helvetica-Bold"  # Using bold
    estilo_celula.fontSize = 18
    estilo_celula.alignment = 1
    
    # Layout configuration: margins and cards per page
    cartelas_por_pagina = 3
    espacamento_x = 260
    margem_x = 10
    margem_y = altura - 320
    x_pos, y_pos = margem_x, margem_y
    
    for i in range(num_cartelas):
        cartela = gerar_cartela()  # Generate card numbers

        # Convert text to Paragraphs for automatic line breaks
        for linha in range(1,6):
            for coluna in range(5):
                if cartela[linha][coluna]:  # If cell has content
                    cartela[linha][coluna] = Paragraph(str(cartela[linha][coluna]), estilo_celula)
        
        # Create a table with the card data
        tabela = Table(cartela, colWidths=50, rowHeights=[40] + [50]*5) 
        estilo = TableStyle([
            # Colored "BINGO" header
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2a193f")),  # Dark purple header
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # White text in header
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold in header
            ('FONTSIZE', (0, 0), (-1, 0), 20),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),

            # Table body (all other cells)
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),

            # Table styling
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROUND', (0, 0), (4, 4), 50),
        ])
        
        tabela.setStyle(estilo)
        tabela.wrapOn(pdf, largura, altura)
        tabela.drawOn(pdf, x_pos, y_pos)
        
        # Insert image at the center of the card
        # x and y positions correspond to the middle row and column
        img_x = x_pos + 100
        img_y = y_pos + 100
        pdf.drawImage(imagem, img_x, img_y, width=50, height=50)
        
        # Move to next position in PDF to place next card
        x_pos += espacamento_x  

        # If 3 cards are on the page, create a new page
        if (i + 1) % cartelas_por_pagina == 0:
            pdf.showPage()
            x_pos, y_pos = margem_x, margem_y
 
    pdf.save()
    print(f"{num_cartelas} cartelas salvas em {nome_arquivo}")



'''SCRIPT EXECUTION'''

logo = "conteudo/logo.png"

n = int(input("Quantas cartelas deseja gerar? "))
salvar_cartelas_pdf(n, logo)