import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiIgfyemYOEAxVelJUCHU3EAw4QFnoECAkQAQ&url=https%3A%2F%2Fwww.cursoemvideo.com%2F&usg=AOvVaw1ETkzlG-Uwl0E4x4eqbyQV&opi=89978449')
except:
    print('Erro ao tentar acessar o site do Curso em Vídeo!')
else:
    print('Site do Curso em Vídeo acessado com sucesso!')
