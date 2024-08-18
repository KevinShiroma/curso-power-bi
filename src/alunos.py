import pandas as pd
import numpy as np
from faker import Faker

# Inicializar o gerador de dados fictícios
fake = Faker('pt_BR')

# Definir o número de registros
num_records = 3000

# Dicionário de nomes com gêneros
nomes_generos = {
    # Nomes Masculinos
    "José": "Masculino", "Carlos": "Masculino", "Lucas": "Masculino", "Pedro": "Masculino", "Rafael": "Masculino",
    "Felipe": "Masculino", "Gabriel": "Masculino", "Daniel": "Masculino", "João": "Masculino", "Mateus": "Masculino",
    
    # Nomes Femininos
    "Maria": "Feminino", "Ana": "Feminino", "Juliana": "Feminino", "Fernanda": "Feminino", "Camila": "Feminino",
    "Patrícia": "Feminino", "Luciana": "Feminino", "Claudia": "Feminino", "Vanessa": "Feminino", "Beatriz": "Feminino"
}

# Lista dos 10 municípios mais populosos do estado de São Paulo
municipios = [
    "São Paulo", "Guarulhos", "Campinas", "São Bernardo do Campo", "Santo André",
    "São José dos Campos", "Sorocaba", "Ribeirão Preto", "Osasco", "Mauá"
]

# Tipos de logradouro
tipos_logradouro = ["Rua", "Avenida", "Alameda", "Estrada", "Viela"]

# Listas de cursos possíveis
cursos = [
    "Administração", "Ciências Econômicas", "Publicidade e Propaganda", 
    "Análise e Desenvolvimento de Sistemas", "Ciência da Computação", 
    "Ciência de Dados e Inteligência Artificial", "Ciências Contábeis", 
    "Relações Públicas", "Relações Internacionais", "Secretariado"
]

# Lista de valores de mensalidade possíveis
valores_mensalidade = [
    2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 
    3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000
]

# Função para gerar dados fictícios
def generate_data():
    data = []
    nomes = list(nomes_generos.keys())
    for _ in range(num_records):
        nome = np.random.choice(nomes)
        genero = nomes_generos[nome]
        sobrenome = fake.last_name()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=60)
        idade = (pd.Timestamp.now() - pd.Timestamp(data_nascimento)).days // 365
        curso = np.random.choice(cursos)
        tipo_logradouro = np.random.choice(tipos_logradouro)
        logradouro = fake.street_name()
        numero = fake.building_number()
        cidade = np.random.choice(municipios)
        ra = ''.join([str(np.random.randint(0, 10)) for _ in range(8)])
        nota_final = np.random.randint(0, 11)
        valor_mensalidade = np.random.choice(valores_mensalidade)
        
        data.append([nome, sobrenome, data_nascimento.strftime('%d/%m/%Y'), idade, genero, curso, tipo_logradouro, logradouro, numero, cidade, ra, nota_final, valor_mensalidade])
    
    return data

# Gerar os dados
data = generate_data()

# Criar DataFrame
columns = [
    "Nome", "Sobrenome", "Data de Nascimento", "Idade", "Gênero", "Curso", 
    "Tipo de Logradouro", "Logradouro", "Número", "Cidade", "RA", "Nota Final", "Valor Mensalidade"
]
df = pd.DataFrame(data, columns=columns)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('dados_ficcionais.csv', index=False, encoding='utf-8')

print("Arquivo CSV gerado com sucesso!")
