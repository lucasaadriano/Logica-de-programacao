- O `while` (enquanto) repete um bloco de código **enquanto a condição for verdadeira**. Quando a condição vira falsa, o laço termina sozinho.
- Cada repetição do bloco é chamada de **iteração**.
- Um `while` com contador tem três partes:
  - **Inicialização**: criar a variável de controle antes do laço.
  - **Condição**: testada antes de cada repetição.
  - **Atualização**: alterar a variável dentro do bloco.

Ex:

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

- Se a variável de controle nunca for atualizada, a condição nunca muda e o laço fica **infinito** (o programa trava). Para interromper no terminal, use `Ctrl + C`.
- Se a condição já começa falsa, o bloco não executa nenhuma vez.
- Atalhos de atribuição:
  - `i += 1` equivale a `i = i + 1`
  - `i -= 1` equivale a `i = i - 1`
  - `i *= 2` equivale a `i = i * 2`

Ex:

```python
contador = 5
while contador > 0:
    print(contador)
    contador -= 1
print("Lançar!")
```

- O **acumulador** é uma variável que guarda um resultado construído ao longo das voltas. Na soma ele começa em `0`; na multiplicação começa em `1` (elemento neutro).
- O `print` do resultado fica **fora** do laço (sem indentação), para aparecer só uma vez no final.

Ex:

```python
i = 2
soma = 0
while i <= 10:
    soma += i
    i += 2
print("Soma dos pares de 2 a 10:", soma)
```

Ex (fatorial, acumulador de multiplicação):

```python
n = 5
i = 1
fatorial = 1
while i <= n:
    fatorial *= i
    i += 1
print(f"{n}! = {fatorial}")
```

- Nem sempre a condição depende de um contador de 1 em 1. Ela pode depender de qualquer variável que mude dentro do laço, como um saldo ou um valor que cresce.

Ex:

```python
saldo = 100
saque = 30
while saldo >= saque:
    saldo -= saque
    print("Saque realizado. Saldo atual:", saldo)
print("Saldo insuficiente para novo saque")
```

Ex:

```python
inicial = 1000
valor = inicial
anos = 0
while valor < inicial * 2:
    valor *= 1.10
    anos += 1
print(f"Passaram {anos} anos e o valor chegou a {valor:.2f}")
```

- A divisão inteira (`//`) remove o último dígito de um número e o resto da divisão por 10 (`% 10`) extrai o último dígito. Os dois juntos resolvem vários exercícios com dígitos.

Ex (contar dígitos):

```python
numero = 12345
digitos = 0
while numero > 0:
    numero = numero // 10
    digitos += 1
print("Quantidade de dígitos:", digitos)
```

Ex (inverter número):

```python
numero = 1234
invertido = 0
while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10
print("Invertido:", invertido)
```

- A atribuição múltipla (`a, b = b, a + b`) calcula o lado direito inteiro antes de atribuir, então não precisa de variável auxiliar. Ela é usada na sequência de Fibonacci, em que cada termo é a soma dos dois anteriores.

Ex:

```python
limite = 50
a = 0
b = 1
while a <= limite:
    print(a)
    a, b = b, a + b
```
