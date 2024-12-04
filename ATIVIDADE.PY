# O conjunto de dados contém 28 colunas e inclui informações como Passengerid, Age, Fare, Sex, sibsp 
(número de irmãos/cônjuges a bordo), Pclass, Embarked e a coluna-alvo possivelmente 2urvived (indicando sobrevivência). 
Outras colunas parecem conter valores zeros repetidos, que podem ser descartados.

# Análise básica de dados:

# Dimensão do conjunto de dados.
# Tipos de dados e valores ausentes.
# Estatísticas descritivas.
# Limpeza de dados:

# Verificação de colunas irrelevantes ou redundantes.
# Tratamento de valores ausentes.
# Exploração visual:

# Distribuição de idade e tarifa.
# Proporção de sobreviventes por sexo e classe.
# Vamos começar com a análise básica. ​​

# Análise Inicial dos Dados:
# Dimensão: O conjunto possui 1309 linhas e 28 colunas.
# Tipos de dados:
# Colunas como Age, Fare, e Embarked são float.
# Sex, Pclass, e 2urvived são inteiros (provavelmente categóricos).
# Valores ausentes:
# Apenas a coluna Embarked possui 2 valores ausentes.
# Colunas redundantes:
# Diversas colunas como zero, zero.1, ..., zero.18 contêm apenas zeros e podem ser descartadas.

# Importar as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
file_path = 'train_and_test2.csv'  # Substitua pelo caminho correto
data = pd.read_csv(file_path)

# 1. Remover colunas irrelevantes (contendo apenas zeros)
colunas_irrelevantes = [col for col in data.columns if data[col].nunique() == 1]
data_limpo = data.drop(columns=colunas_irrelevantes)

# 2. Tratar valores ausentes
data_limpo['Embarked'].fillna(data_limpo['Embarked'].mode()[0], inplace=True)

# 3. Estatísticas descritivas
print("Estatísticas descritivas:")
print(data_limpo.describe())

# 4. Distribuição de Idade e Tarifa
plt.figure(figsize=(12, 5))

# Distribuição de Idade
plt.subplot(1, 2, 1)
plt.hist(data_limpo['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')

# Distribuição de Tarifa
plt.subplot(1, 2, 2)
plt.hist(data_limpo['Fare'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribuição de Tarifa')
plt.xlabel('Tarifa')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()

# 5. Proporção de Sobreviventes por Sexo
sobreviventes_por_sexo = data_limpo.groupby('Sex')['2urvived'].mean()
labels = ['Masculino', 'Feminino']
plt.figure(figsize=(6, 6))
plt.bar(labels, sobreviventes_por_sexo, color=['blue', 'pink'], edgecolor='black')
plt.title('Taxa de Sobrevivência por Sexo')
plt.ylabel('Taxa de Sobrevivência')
plt.show()

# 6. Proporção de Sobreviventes por Classe
sobreviventes_por_classe = data_limpo.groupby('Pclass')['2urvived'].mean()
plt.figure(figsize=(6, 6))
plt.bar(sobreviventes_por_classe.index, sobreviventes_por_classe, color='orange', edgecolor='black')
plt.title('Taxa de Sobrevivência por Classe')
plt.xlabel('Classe')
plt.ylabel('Taxa de Sobrevivência')
plt.show()

# 7. Distribuição por Porto de Embarque
portos = ['Cherbourg', 'Queenstown', 'Southampton']  # Assumindo que os valores 0, 1, 2 representam esses portos
data_limpo['Embarked'] = data_limpo['Embarked'].map({0.0: 'Cherbourg', 1.0: 'Queenstown', 2.0: 'Southampton'})
embarked_counts = data_limpo['Embarked'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(embarked_counts, labels=embarked_counts.index, autopct='%1.1f%%', colors=['cyan', 'magenta', 'yellow'])
plt.title('Distribuição de Embarque')
plt.show()
