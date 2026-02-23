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

### 🔹 Revisão do "Olá, Mundo"

Primeiro contato com a execução de scripts Python e entendimento da função:

```python
print("Olá, mundo!")
```

---

### 🔹 Uso de `# %%` no VS Code

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

---

## Conceitos Fundamentais Aprendidos Até Agora

✔ Execução de scripts Python
✔ Uso de células interativas no VS Code
✔ Operações matemáticas básicas
✔ Criação e reatribuição de variáveis
✔ Armazenamento e atualização de estados
✔ Organização inicial de código

---

## Objetivo do Repositório

Construir base sólida em Python para aplicação futura em:

* Análise de Dados
* Automação de tarefas
* Manipulação de informações
* Desenvolvimento de scripts analíticos

---

## Próximos Passos
Estruturas de Controle

Estruturas condicionais (if, else, elif)

Estruturas de repetição (while, for, break, continue)

Tratamento de exceções (try, except)

Listas e Tuplas

Introdução às listas e suas operações (criação, acesso e modificação)

Funções e métodos de lista (len(), append(), remove(), sort())

Introdução às tuplas e suas características

Dicionários

Criação de dicionários

Acesso a valores

Modificação de dados

Funções

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

 Repositório em constante evolução conforme avanço no curso.
