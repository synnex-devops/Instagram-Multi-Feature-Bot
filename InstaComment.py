
import time
from selenium import webdriver

driver = webdriver.Edge()  # Optional argument, if not specified will search path.







#import requests
#import json

# # Insira suas credenciais do Instagram
# username = "karttiodavis"
# password = "Thd@282526"

# # Obtenha o ID do post
# post_id = "3228029968349165110"

# # Crie um comentário
# comment = "@karttiodavis @garagemtiodavis"

# # Faça o comentário
# url = "https://api.instagram.com/v1/media/{}/comments".format(post_id)
# headers = {
#     "Authorization": "Basic {}:{}".format(username, password),
#     "Content-Type": "application/json",
# }
# data = {
#     "text": comment,
# }
# response = requests.post(url, headers=headers, data=json.dumps(data))

# if response.status_code == 200:
#     print("Comentário enviado com sucesso!")
# else:
#     print("Erro ao enviar o comentário: {}".format(response.status_code))









##############################################
# import requests
# import json
# import time

# # Defina as variáveis de entrada
# user_id = "karttiodavis"
# password = "Thd@282526"
# post_id = "3228029968349165110"
# comment = "@karttiodavis @garagemtiodavis"

# # Crie uma sessão com o Instagram
# session = requests.Session()

# # Faça login no Instagram
# login_data = {"username": user_id, "password": password}
# login_url = "https://www.instagram.com/accounts/login/ajax/"
# response = session.post(login_url, data=login_data)

# # Verifique se o login foi bem-sucedido
# if response.status_code == 200:

#     # Crie a solicitação para fazer o comentário
#     comment_url = "https://www.instagram.com/p/{}/comments/".format(post_id)
#     comment_data = {"comment_text": comment}

#     # Faça o comentário
#     response = session.post(comment_url, data=comment_data)

#     # Verifique se o comentário foi publicado com sucesso
#     if response.status_code == 200:
#         print("O comentário foi publicado com sucesso!")
#     else:
#         print("Ocorreu um erro ao publicar o comentário.")
# else:
#     print("O login falhou.")

# Aguarde 1 minuto antes de repetir
#time.sleep(60)



##############################################








#import time
#import instapy

# Crie uma conta do Instagram e conecte-a à biblioteca
# instapy.login("karttiodavis", "Thd@282526")

# # Obtenha o ID do post no qual deseja fazer o comentário
# post_id = "3228029968349165110"

# # Crie o comentário que deseja publicar
# comment = "@garagemtiodavis"


# instapy.comment(post_id, comment)


# Defina o tempo de atraso para a publicação do comentário
#delay = 3600

# Execute o código
#instapy.comment(post_id, comment, delay=delay)

# Crie um loop infinito
# while True:

#     # Faça o comentário no post
#     instapy.comment(post_id, comment)

#     # Aguarde 60 minutos
#     time.sleep(60 * 60)
#
#     # Aguarde 1 minuto
#     time.sleep(60)