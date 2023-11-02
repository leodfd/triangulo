from PIL import Image

def abrir_imagem(caminho):
    # Abre a imagem no caminho especificado
    imagem = Image.open(caminho)
    return imagem

# Substitua 'caminho/para/sua/imagem.jpg' pelo caminho absoluto ou relativo da sua imagem
caminho_da_imagem = '"C:/Users/lleod/Desktop/vs/triangulo-equilatero.jpg"'
imagem_retornada = abrir_imagem(caminho_da_imagem)

# Agora você pode fazer o que quiser com a imagem retornada, como exibi-la ou processá-la
imagem_retornada.show()  # Isso abrirá a imagem no visualizador de imagens padrão do seu sistema
