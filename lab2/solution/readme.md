### **Atividade 1**
Para a atividade do laboratório de mostrar as diferentes mutações que podem ser aplicadas no teste de triângulos, é possível verificar o arquivo ```Mutacoes_de_Triangulos.ipynb```.

### **Atividade 2** 
A linguagem escolhida para procurar ferramentas de testes de mutação é o **Python**, devido a facilidade de manuseio e a grande disponibilidade de módulos de fácil instalação. Dentre as opções de ferramentas de mutação encontradas, as seguintes opções foram testadas:

- [MutPy](https://github.com/mutpy/mutpy)
- [Cosmic Ray](https://github.com/sixty-north/cosmic-ray)
- [Mutmut](https://github.com/boxed/mutmut)

Apesar de todas essas terem sido exploradas, o MutPy foi descontinuado e o código apresentava erros ao ser executado; e o Cosmic Ray é uma ferramenta muito complexa para o escopo desta disciplina. O mutmut foi, portanto, a framework de mutação de testes escolhida para explorar que tivemos êxito em sua execução.

Na pasta do mutmut, é possível verificar quatro pastas, cada uma com seu respectivo código a ser executado e testado. Para executar o mutmut, basta, no respectivo diretório de cada programa, executar o comando ```mutmut run```.

Ao executar o mutmut no TrianguloDefeituoso3, obtivemos os seguintes resultados:

> Legend for output:
>
> 🎉 Killed mutants.   The goal is for everything to end up in this bucket.
>
> ⏰ Timeout.          Test suite took 10 times as long as the baseline so were killed.
>
> 🤔 Suspicious.       Tests took a long time, but not long enough to be fatal.
>
> 🙁 Survived.         This means your tests need to be expanded.
>
> 🔇 Skipped.          Skipped.
>
> 1. Using cached time for baseline tests, to run baseline again delete the cache file
> 
> 2. Checking mutants
> ⠴ 26/26  🎉 21  ⏰ 0  🤔 0  🙁 5  🔇 0

O que significa que, para os testes executados, 26 mutantes foram gerados, dentre os quais 21 foram eliminados e 5 sobreviveram.

Para visualizar os mutantes que permaneceram vivos, é possível utilizar o comando ```mutmut show```, que mostrará uma lista de ids para cada mutante que sobreviveu, e em seguida ```mutmut show <id>``` para visualizar um mutante específico da lista.

A linha antecedida por "-" indica a linha original em que ocorreu a alteração, e a linha antecedida por "+" indica a linha de código após a alteração.

A seguir, é possível visualizar a saída do ```mutmut show``` para cada um dos mutantes que não foram eliminados do ```TrianguloDefeituoso3```.

<details>
  <summary>Mutações Sobreviventes</summary>

- **Mutação Sobrevivente 1: ROR (Relational Operator Replacement)**

```python
  def tipo_triangulo(a, b, c):
-    if (a <= 0 or b <= 0 or c < 0):
+    if (a < 0 or b <= 0 or c < 0):
         return "invalido"
     if (a+b > c and a+c > b and b+c > a):
         if (a==b and b == c):
```

- **Mutação Sobrevivente 2: ROR (Relational Operator Replacement)**

```python
  def tipo_triangulo(a,b,c):
-    if (a <= 0 or b <= 0 or c < 0):
+    if (a <= 0 or b < 0 or c < 0):
         return "invalido"
     if (a+b > c and a+c > b and b+c > a):
         if (a==b and b == c):
```

- **Mutação Sobrevivente 3: ROR (Relational Operator Replacement)**

```python
  def tipo_triangulo(a,b,c):
-    if (a <= 0 or b <= 0 or c < 0):
+    if (a <= 0 or b <= 0 or c <= 0):
         return "invalido"
     if (a+b > c and a+c > b and b+c > a):
         if (a==b and b == c):
```

- **Mutação Sobrevivente 4: SVR (Scalar Variable Replacement)**
  
```python
  def tipo_triangulo(a,b,c):
-    if (a <= 0 or b <= 0 or c < 0):
+    if (a <= 0 or b <= 0 or c < 1):
         return "invalido"
     if (a+b > c and a+c > b and b+c > a):
         if (a==b and b == c):
```

- **Mutação Sobrevivente 5: COR (Conditional Operator Replacement)**

```python
  def tipo_triangulo(a,b,c):
-    if (a <= 0 or b <= 0 or c < 0):
+    if (a <= 0 and b <= 0 or c < 0):
         return "invalido"
     if (a+b > c and a+c > b and b+c > a):
         if (a==b and b == c):
```
</details>

______________________

### **Conclusão**

Embora seja importante ressaltar que testes de mutação são uma técnica importante para melhorar a qualidade do software e verificar a efetividade dos conjuntos de testes, as frameworks mais famosas de mutação em python ou foram descontinuadas, ou são muito complexas, ou são pobres em documentação. 

A impressão obtida é que esse tipo de ferramenta é difícil de ser aplicada em prática - e talvez isso indique algo sobre como a maioria dos contextos de desenvolvimento de software ainda estão despreparados para entregar código com testes bem escritos e de qualidade - mas isso pode também ser apenas uma especulação inadequada feita simplesmente com base na dificuldade obtida ao experimentar com essas ferramentas de mutação.