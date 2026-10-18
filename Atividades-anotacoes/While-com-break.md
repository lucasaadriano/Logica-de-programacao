- O `break` **interrompe o laço imediatamente**, mesmo que a condição do `while` ainda seja verdadeira. O programa continua na primeira linha depois do laço.
- Normalmente o `break` fica dentro de um `if`, que define **quando** parar.
- Sem `break`, o laço termina apenas quando a condição vira falsa. Com `break`, ele pode terminar por dois motivos: a condição ficou falsa ou o `break` foi executado.
- O `while True:` cria um laço que, por si só, nunca termina. Só o `break` o encerra. É usado quando não se sabe quantas voltas serão necessárias.
- Cuidado: em `while True`, o `break` precisa ser alcançável, senão o laço é infinito.

Ex:

```python
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1
```

- A ordem das linhas dentro do laço importa. No exemplo acima, o `print` vem antes do `if`, então o 5 é impresso antes de parar.
- A **flag** é uma variável booleana que registra se algo aconteceu durante o laço. Depois do laço, ela permite saber por qual motivo ele terminou.
- Em uma busca, o `break` evita percorrer o resto da lista depois que o item foi encontrado. `len(lista)` retorna a quantidade de itens e evita acessar uma posição que não existe.

Ex:

```python
nomes = ["Ana", "Bruno", "Carlos", "Daniela"]
alvo = "Carlos"
i = 0
encontrado = False
while i < len(nomes):
    if nomes[i] == alvo:
        print("Encontrado na posição", i)
        encontrado = True
        break
    i += 1
if not encontrado:
    print("Não encontrado")
```

- Para limitar tentativas, a condição do `while` impõe o máximo e o `break` encerra antes se a tentativa der certo.

Ex:

```python
senha_correta = "1234"
tentativas = ["0000", "1111", "1234", "9999"]
limite = 3
i = 0
acesso = False
while i < limite:
    if tentativas[i] == senha_correta:
        print("Senha correta na tentativa", i + 1)
        acesso = True
        break
    print("Senha incorreta")
    i += 1
if not acesso:
    print("Acesso bloqueado")
```

- Para procurar o primeiro valor que atende uma condição, `while True` com `break` é o padrão mais simples.

Ex:

```python
n = 101
while True:
    if n % 3 == 0 and n % 5 == 0:
        print("Encontrado:", n)
        break
    n += 1
```

- O **valor sentinela** é um valor especial que sinaliza o fim dos dados (por exemplo, o `0`). A verificação dele vem **antes** do processamento, para que ele não seja tratado como dado comum.

Ex:

```python
valores = [5, 10, 3, 0, 8]
soma = 0
i = 0
while i < len(valores):
    if valores[i] == 0:
        break
    soma += valores[i]
    i += 1
print("Soma:", soma)
```

- Um número é primo se for maior que 1 e divisível apenas por 1 e por ele mesmo. Um único divisor já basta para concluir que não é primo, então o `break` encerra a busca.

Ex:

```python
numero = 29
primo = True
if numero < 2:
    primo = False
else:
    i = 2
    while i < numero:
        if numero % i == 0:
            primo = False
            break
        i += 1

if primo:
    print(numero, "é primo")
else:
    print(numero, "não é primo")
```

- Em um menu, o laço repete até o usuário escolher a opção de sair. Aqui as opções são simuladas por uma lista; em um programa real viriam de `input()`.

Ex:

```python
opcoes = [1, 2, 1, 3, 2]
i = 0
while True:
    opcao = opcoes[i]
    if opcao == 1:
        print("Opção 1: cadastrar")
    elif opcao == 2:
        print("Opção 2: listar")
    elif opcao == 3:
        print("Saindo do menu")
        break
    i += 1
```
