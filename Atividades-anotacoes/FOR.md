- O `for` percorre os elementos de uma sequência, um de cada vez, executando o bloco para cada elemento.
- Sintaxe: `for variavel in sequencia:`. A variável recebe o elemento atual a cada volta.
- O `for` não precisa de contador manual: o Python avança sozinho, então não há risco de laço infinito por esquecer a atualização.
- Use `for` quando a quantidade de repetições é conhecida ou quando há uma sequência para percorrer (lista, texto, intervalo). Use `while` quando a repetição depende de uma condição que muda.
- A função `range()` gera uma sequência de números:
  - `range(fim)`: vai de 0 até `fim - 1`.
  - `range(inicio, fim)`: vai de `inicio` até `fim - 1`.
  - `range(inicio, fim, passo)`: avança de `passo` em `passo`.
- O valor final do `range` **nunca é incluído**.

Ex:

```python
for i in range(5):
    print(i)
```

Ex:

```python
for i in range(1, 6):
    print(i)
```

- Com passo negativo, o `range` faz contagem regressiva.

Ex:

```python
for n in range(2, 21, 2):
    print(n)

for n in range(10, 0, -1):
    print(n)
```

- O `for` também percorre listas. A cada volta, a variável recebe um elemento da lista.
- `len(lista)` retorna a quantidade de elementos, e evita escrever o tamanho manualmente.

Ex:

```python
notas = [7, 8.5, 6, 9]
soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)
print("Média:", media)
```

- Um texto (string) é uma sequência de caracteres, então o `for` percorre **letra por letra**, incluindo espaços.
- O operador `in` verifica se um item está dentro de uma sequência.

Ex:

```python
frase = "Banco de Dados"
vogais = "aeiouAEIOU"
quantidade = 0
for letra in frase:
    if letra in vogais:
        quantidade += 1
print("Quantidade de vogais:", quantidade)
```

- Para achar o maior e o menor valor de uma lista, comece com o **primeiro elemento** (posição 0) e compare com os demais. Começar com `0` daria erro em listas só com números negativos.
- Python já tem as funções `max()` e `min()`; fazer na mão serve para entender a lógica.

Ex:

```python
numeros = [14, 3, 27, 8, 19]
maior = numeros[0]
menor = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print("Maior:", maior)
print("Menor:", menor)
```

- O `enumerate()` entrega a **posição e o elemento** ao mesmo tempo. A contagem começa em 0; o argumento `start=1` muda o início.

Ex:

```python
nomes = ["Ana", "Bruno", "Carlos"]
for posicao, nome in enumerate(nomes, start=1):
    print(f"{posicao}. {nome}")
```

- O `break` também funciona no `for`, com o mesmo efeito do `while`: encerra o laço imediatamente.

Ex:

```python
valores = [4, 8, 15, -3, 16, -7]
achou = False
for valor in valores:
    if valor < 0:
        print("Primeiro negativo:", valor)
        achou = True
        break
if not achou:
    print("Não há números negativos")
```

- O `append()` adiciona um elemento ao final de uma lista. É comum começar com uma lista vazia (`[]`) e preenchê-la dentro do `for`.

Ex:

```python
quadrados = []
for i in range(1, 6):
    quadrados.append(i * i)
print(quadrados)
```

- O `for` aninhado é um `for` dentro de outro. Para **cada** volta do laço externo, o laço interno roda completo. O total de voltas é a multiplicação das quantidades (3 x 3 = 9).

Ex:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()
```
