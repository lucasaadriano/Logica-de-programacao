# If, elif e else

- O `if` (se) executa um bloco de código somente se a condição for verdadeira (`True`). Se for falsa (`False`), o bloco é ignorado.
- Depois da condição vem sempre dois pontos (`:`) e o bloco seguinte precisa estar **indentado** (4 espaços). É a indentação que mostra o que pertence ao `if`.

Ex:

```python
idade = 20

if idade >= 18:
    print("Maior de idade")
```

- O `else` (senão) executa quando a condição do `if` é falsa. Ele não tem condição própria e é sempre o último bloco da cadeia.

Ex:

```python
idade = 17

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

- O `elif` (senão se) permite testar mais condições. Ele só é testado se todas as anteriores foram falsas. Pode haver quantos `elif` forem necessários.
- Em uma cadeia `if/elif/else`, **apenas um bloco é executado**: o primeiro cuja condição for verdadeira. Depois disso, o Python ignora o resto.

Ex:

```python
nota = 8.2

if nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
else:
    print("Conceito D")
```

- A **ordem das condições importa**, pois elas são testadas de cima para baixo. No exemplo abaixo, com a ordem invertida, a nota 9 cai no primeiro `if` e recebe o conceito errado.

Ex:

```python
nota = 9

if nota >= 5:
    print("Conceito C")
elif nota >= 7:
    print("Conceito B")
elif nota >= 9:
    print("Conceito A")
```

- Operadores de comparação, que resultam em `True` ou `False`:
  - `==` igual
  - `!=` diferente
  - `>` maior
  - `<` menor
  - `>=` maior ou igual
  - `<=` menor ou igual
- Atenção: `=` **atribui** um valor a uma variável, enquanto `==` **compara** dois valores. Usar `=` dentro do `if` gera erro.

Ex:

```python
senha = "1234"

if senha == "1234":
    print("Senha correta")
```

- Os operadores lógicos combinam condições:
  - `and`: verdadeiro somente se as **duas** condições forem verdadeiras.
  - `or`: verdadeiro se **pelo menos uma** for verdadeira.
  - `not`: inverte o resultado (`True` vira `False` e vice-versa).

Ex:

```python
idade = 65
estudante = False
tem_documento = True

if idade >= 60 or estudante:
    print("Tem direito a meia-entrada")

if idade >= 18 and tem_documento:
    print("Entrada liberada")

if not estudante:
    print("Não é estudante")
```

- O operador `%` retorna o **resto da divisão**. É muito usado para verificar se um número é par (resto 0 na divisão por 2) ou divisível por outro.

Ex:

```python
numero = 8

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
```

- O `if` aninhado é um `if` dentro de outro. O bloco interno só é verificado se a condição do bloco externo for verdadeira. Cada `else` pertence ao `if` que está na mesma indentação.

Ex:

```python
usuario = "lucas"
senha = "1234"

if usuario == "lucas":
    if senha == "1234":
        print("Login realizado")
    else:
        print("Senha incorreta")
else:
    print("Usuário não encontrado")
```

- Comparar textos (strings) diferencia maiúsculas de minúsculas: `"Lucas"` é diferente de `"lucas"`.
- Quando a decisão vira um valor que será usado depois, é possível guardar o resultado em uma variável dentro de cada ramo da cadeia.

Ex:

```python
valor_compra = 150

if valor_compra >= 200:
    frete = 0
elif valor_compra >= 100:
    frete = 10
else:
    frete = 20

print("Frete:", frete)
print("Total:", valor_compra + frete)
```

- Parênteses agrupam condições e deixam clara a ordem de avaliação. Exemplo clássico: ano bissexto, que é divisível por 4 e não por 100, ou divisível por 400.

Ex:

```python
ano = 2024

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(ano, "é bissexto")
else:
    print(ano, "não é bissexto")
```
