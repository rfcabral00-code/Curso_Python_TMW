# Curso Python TMW

Repositório criado para acompanhar minha evolução no aprendizado de **Python**, registrando aulas, exercícios práticos e conceitos fundamentais da linguagem.

---

## Aula 1 — Preparação do Ambiente

Nesta etapa foi realizada a configuração do ambiente de desenvolvimento:

* Instalação do **Anaconda** (distribuição Python para ciência de dados).
* Utilização do **VS Code** como editor de código (já instalado anteriormente por conta dos estudos em SQL).
* Organização inicial do projeto.

---

## Aula 2 — Primeiros Conceitos em Python

### Revisão do "Olá, Mundo"

Primeiro contato com a execução de scripts Python e entendimento da função:

```python
print("Olá, mundo!")
```

---

### Uso de `# %%` no VS Code

Aprendemos a utilizar o marcador:

```python
# %%
```

Ele permite executar **partes específicas do código** de forma isolada, funcionando como células interativas (semelhante ao Jupyter Notebook).

Isso facilita:

* Testes rápidos
* Organização do raciocínio
* Execução por etapas

---

### Operações Matemáticas

Exploramos os operadores básicos do Python construindo uma pequena "calculadora":

```python
# %%
# SOMA
print("1 + 1 =", 1 + 1)

# SUBTRAÇÃO
print("10 - 5 =", 10 - 5)

# %%
# MULTIPLICAÇÃO
print("10 x 5 =", 10 * 5)

# DIVISÃO
print("10 / 3 =", 10 / 3)

# DIVISÃO INTEIRA (descarta as casas decimais)
print("10 // 3 =", 10 // 3)

# RESTO DA DIVISÃO (módulo)
print("10 % 4 =", 10 % 4)

# %%
# POTENCIAÇÃO
print("3 ** 4 =", 3 ** 4)
```
 Conceitos aprendidos:

| Operador | Função |
| -------- | ------ |

* | Soma

- | Subtração

* | Multiplicação
  / | Divisão com resultado decimal
  // | Divisão inteira
  % | Resto da divisão
  ** | Potência

---

### Variáveis

Variáveis funcionam como **"post-its" na memória do programa**: guardam valores para serem reutilizados posteriormente.

Elas representam um **estado armazenado**, que pode ser alterado ao longo da execução.

#### Exemplo:

```python
nome = "Rafael Cabral"
print(nome)

nome = "Garrafa de água Levity"
print(nome)
```

➡ O valor da variável pode ser sobrescrito.
➡ O Python sempre considera **o último valor atribuído**.

---

### Variáveis com Operações

Também vimos como armazenar resultados matemáticos:

```python
soma = 1 + 1
print("1 + 1 =", soma)
```

---

### Atualização de Estado da Variável

Uma variável pode ser reutilizada e modificada:

```python
resultado = 10 - 5
print(resultado)

resultado = 10 * 2
print(resultado)

resultado = resultado + 10
print(resultado)
```
 Aqui aprendemos que:

* Variáveis podem ser recalculadas.
* Podemos usar o valor anterior para gerar um novo.
* Isso é muito utilizado em cálculos acumulativos e análise de dados.

Aula 3 — Entrada de Dados e Interação com o Usuário

Nesta aula começamos a desenvolver programas interativos utilizando o método input().

Até então, os programas apenas exibiam informações na tela.
Agora eles passam a receber dados digitados pelo usuário e reagir a essas informações.

O método input()

O input() permite capturar dados digitados pelo usuário durante a execução do programa.

Exemplo:

nome = input("Qual é o seu nome? ")
print("Prazer,", nome)

Aprendizados:

input() sempre retorna uma string (texto).

O valor pode ser armazenado em uma variável.

A variável pode ser reutilizada posteriormente.

Conversão de Tipos

Como o input() retorna texto, aprendemos a converter para número quando necessário:

numero = int(input("Digite um número: "))

Conceito reforçado:

Diferença entre texto e número

Uso de int() para conversão

Exercício — Dobro de um Número

Programa que recebe um número e exibe o dobro:

numero = int(input("Entre com um número: "))
dobro = numero * 2
print("O dobro é", dobro)

Conceitos aplicados:

Entrada de dados

Conversão de tipo

Operações matemáticas

Exercício — Raiz Quadrada

Programa que calcula a raiz quadrada de um número inteiro:

numero = int(input("Entre com um número inteiro para calcular a sua raiz quadrada: "))
raiz = numero ** (1/2)
print("Raiz quadrada de", numero, "é:", raiz)

Conceitos aplicados:

Exponenciação

Cálculo matemático com dados fornecidos pelo usuário

Exercício — História Interativa

Foi criado um pequeno programa narrativo onde a cada parte da história o usuário deve pressionar Enter para continuar.

Exemplo simplificado:

p1 = "Era uma vez um velho e cansado cachorro no velho oeste em busca do seu dono."
p2 = "Ao longe, ele vê uma pequena vila com poucas pessoas e muitos cavalos."
p3 = "Ao chegar na vila, ele vai até a hospedaria local."

print(p1)
input("Pressione Enter para continuar...")

print(p2)
input("Pressione Enter para continuar...")

print(p3)
input("Pressione Enter para continuar...")

Além da narrativa, a história também incluiu interação com o usuário por meio de perguntas e respostas.

Conceitos aplicados:

Organização de texto em variáveis

Uso do input() para pausar execução

Construção de narrativa interativa

Estrutura sequencial de execução

---


## Objetivo do Repositório

Construir base sólida em Python para aplicação futura em:

* Análise de Dados
* Automação de tarefas
* Manipulação de informações
* Desenvolvimento de scripts analíticos

---

## Próximos Passos
Estruturas de Controle:

Estruturas condicionais (if, else, elif)

Estruturas de repetição (while, for, break, continue)

Tratamento de exceções (try, except)

Listas e Tuplas:

Introdução às listas e suas operações (criação, acesso e modificação)

Funções e métodos de lista (len(), append(), remove(), sort())

Introdução às tuplas e suas características

Dicionários:

Criação de dicionários

Acesso a valores

Modificação de dados

Funções:

Definindo funções em Python

Parâmetros e argumentos

Retorno de valores

Módulos e Bibliotecas

Importando e utilizando módulos em Python

Explorando bibliotecas populares:

math

random

datetime

Manipulação de Arquivos

Leitura e escrita de arquivos em Python

Trabalhando com arquivos CSV

 Tópicos Especiais

Streamlit

Consumo de APIs

---

