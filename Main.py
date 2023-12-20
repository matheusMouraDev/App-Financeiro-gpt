import openai
import matplotlib.pyplot as plt

# Configurar a chave da API da OpenAI
openai.api_key = 'SUA_CHAVE_DA_API_AQUI'

# Obter entrada do usuário
entrada_usuario = input("Digite sua entrada de texto: ")

# Fazer chamada à API da OpenAI
resposta_openai = openai.Completion.create(
    engine="text-davinci-002",
    prompt=entrada_usuario,
    max_tokens=50
)

# Extrair informações da resposta da OpenAI
informacoes = resposta_openai['choices'][0]['text']

# Criar um gráfico com as informações
# (Aqui você precisa adaptar conforme suas necessidades)

# Exemplo de gráfico de barras
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3']
valores = [10, 20, 15]

plt.bar(categorias, valores)
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Controle Financeiro')
plt.show()
