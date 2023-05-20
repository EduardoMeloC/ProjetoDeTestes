### **1. Solução do [problema do Banco](https://olimpiada.ic.unicamp.br/pratique/p2/2012/f2/banco/)**

A solução do Problema do Banco foi indicada no arquivo `Banco.py`. É possível executá-la com inputs utilizando o arquivo `main.py`.
Essa solução foi submetida e aceita como válida pelo validador automático da OBI, e uma explicação do algoritmo e do código pode ser obtida [aqui](https://www.youtube.com/watch?v=loitd1Lt0Vo&feature=youtu.be&ab_channel=Rafah).

### **2. Aplicar a ferramenta de mutação com um caso de teste qualquer (sem isso as ferramentas não geram mutantes).**

Os nossos casos de teste qualquer foram os mesmos que estão na página do problema do banco da OBI. No arquivo `test_Banco.py`, são as funções `test_saida_correta_banco1` e `test_saida_correta_banco2`.

Foram gerados **29 mutantes**, dentre os quais **7 sobreviveram** e ficou **1 sob suspeita**. São eles:


<details>
  <summary><b>Mutantes Sobreviventes</b></summary>

  **Mutação Sobrevivente 1**
  ```python
    def banco(C, arrival, service):
      #perhaps sort arrival and service by arrival
  -   last_arrival = 0
  +   last_arrival = 1
      cashier = [0]*C
      waited = 0
      argwaited = 0
      count = 0
  ```
  **Mutação Sobrevivente 2**
  ```python
    def banco(C, arrival, service):
      #perhaps sort arrival and service by arrival
      last_arrival = 0
      cashier = [0]*C
  -   waited = 0
  +   waited = 1
      argwaited = 0
      count = 0
  ```
  **Mutação Sobrevivente 3**
  ```python
    def banco(C, arrival, service):
      #perhaps sort arrival and service by arrival
      last_arrival = 0
      cashier = [0]*C
  -   waited = 0
  +   waited = None
      argwaited = 0
      count = 0
  ```
  **Mutação Sobrevivente 4**
  ```python
    def banco(C, arrival, service):
      #perhaps sort arrival and service by arrival
      last_arrival = 0
      cashier = [0]*C
      waited = 0
  -   argwaited = 0
  +   argwaited = 1
      count = 0
  ```
  **Mutação Sobrevivente 5**
  ```python
    def banco(C, arrival, service):
      #perhaps sort arrival and service by arrival
      last_arrival = 0
      cashier = [0]*C
      waited = 0
  -   argwaited = 0
  +   argwaited = None
      count = 0
  ```
  **Mutação Sobrevivente 6**
  ```python
    for t in range(len(arrival)):
      diff = arrival[t]-last_arrival
      #print(f"{t} arrived {diff}s after {t-1}")
      last_arrival = arrival[t]
  -   if(diff>0):
  +   if(diff>=0):
        cashier = [max(x - diff,0) for x in cashier]
      #print(f"cashiers = {cashier}")
      argwaited = argmin(cashier)
      waited = cashier[argwaited]
  ```
  **Mutação Sobrevivente 7**
  ```python
    for t in range(len(arrival)):
      diff = arrival[t]-last_arrival
      #print(f"{t} arrived {diff}s after {t-1}")
      last_arrival = arrival[t]
      if(diff>0):
  -     cashier = [max(x - diff,0) for x in cashier]
  +     cashier = [max(x - diff,1) for x in cashier]
      #print(f"cashiers = {cashier}")
      argwaited = argmin(cashier)
      waited = cashier[argwaited]
  ```
  **Mutação Suspeita**
  ```python
    def argmin(a):
  -    return min(range(len(a)), key=lambda x : a[x])
  +    return min(range(len(a)), key=lambda x : None)
  
    def banco(C, arrival, service):
      #perhaps sort arrival and service by arrival
  ```
</details>
<br/>


### **3. Projetar testes para matar os mutantes sobreviventes, usando o modelo RIP.**

**Mutação Sobrevivente 7**
  ```python
    for t in range(len(arrival)):
      diff = arrival[t]-last_arrival
      #print(f"{t} arrived {diff}s after {t-1}")
      last_arrival = arrival[t]
      if(diff>0):
  -     cashier = [max(x - diff,0) for x in cashier]
  +     cashier = [max(x - diff,1) for x in cashier]
      #print(f"cashiers = {cashier}")
      argwaited = argmin(cashier)
      waited = cashier[argwaited]
  ```

Com a finalidade de criar o nosso projeto de testes para eliminar os mutantes sobreviventes, precisamos de pensar em como alcançar um trecho de código que apresenta falhas, para em seguida infectar e propagar o erro.

Para alcançar, é necessária ao menos uma entrada cujo tempo de chegada é maior que zero, para diff ser maior que 0 e entrar no if.
Em termos matemáticos: T>0

Para infectar, é necessário um caso que ```x - diff < 1```. Ou seja, qualquer caso em que o tratamento de um cliente imediatamente depois (mesma iteração) que o caixa que vai atendê-lo vagar, ou estar a menos de 1 segundo. Isso fará com que o valor de cashier não seja o esperado, e sim 1 a mais.

Para propagar, esse valor 1 adicionado ao cashier, onde deveria ser 0, deve causar ao menos um cliente a esperar mais que 20 min. O inverso é impossível, visto que é uma adição.
Ou seja, é preciso mudar o valor de waited em alguma iteração de ```19 < x <= 20``` para ```20 < x```. Note que de 21 para 22 ou 19 para 20 não causaria o erro, mas 19.1 para 20.1, sim.

Podemos, com essas informações, projetar um caso de teste simples em que:
* Ao menos uma entrada cujo tempo de chegada é maior que zero;
* O tratamento de um cliente imediatamente depois (mesma iteração) que o caixa que vai atendê-lo vagar, ou estar a menos de 1 segundo.
* É mudado o valor de waited em alguma iteração de ```19 < x <= 20``` para ```20 < x```, por conta do erro.

Exemlos:
C = 1
T = [0,5,5]
D = [5,20,1]

C = 1
T = [0,5,6]
D = [5,21,1]

O resultado esperado de ambos é 0, mas a mutação propagará 1.

### **4. No caso de haver mutantes equivalentes, procurem mostrar que são equivalentes com uma argumentação rigorosa (vamos trabalhar um pouco mais sobre isso, mas tentem fazer algo).**

<br/>
<details>
  <summary><b>Mutação Sobrevivente 1</b></summary>

  ```python
    def banco(C, arrival, service):
      #perhaps sort arrival and service by arrival
  -   last_arrival = 0
  +   last_arrival = 1
      cashier = [0]*C
      waited = 0
      argwaited = 0
  ```

  O único ponto do código que utilizar o valor mudado é a linha \`\`\`python diff = arrival\[t\] - last\_arrival\`\`\` , pois na linha imediatamente abaixo, o valor de last\_arrival é atribuído novamente, dessa vez a um valor da entrada. Logo, apenas na primeira iteração do for é executado o diff com last\_arrival modificado. Já que diff serve para decrementar cashier, e todos os seus valores já são zero nesse ponto, nada nunca acontece de diferente.
</details>
<br/>

<details>
  <summary><b>Mutações Sobreviventes 2-5</b></summary>

  ```python
    def banco(C, arrival, service):
      #perhaps sort arrival and service by arrival
      last_arrival = 0
      cashier = [0]*C
  -   waited = 0
  +   waited = 1
  +   waited = None
  -   argwaited = 0
  +   argwaited = 1
  +   argwaited = None
      count = 0
  ```

  Antes de serem usados, nas linhas abaixo, eles já são atribuídos a valores corretos nas duas linhas logo acima, e portanto nenhuma saída nunca será afetada.
  ```python
  if(waited>20):
      count += 1
  cashier[argwaited]+=(service[t])
  ```
  </details>
  </br>

<details>
  <summary><b>Mutação Sobrevivente 6</b></summary>

  ```python
    for t in range(len(arrival)):
      diff = arrival[t]-last_arrival
      #print(f"{t} arrived {diff}s after {t-1}")
      last_arrival = arrival[t]
  -   if(diff>0):
  +   if(diff>=0):
        cashier = [max(x - diff,0) for x in cashier]
      #print(f"cashiers = {cashier}")
      argwaited = argmin(cashier)
      waited = cashier[argwaited]
  ```

  Adiciono apenas o caso em que diff é 0. Porém, tudo que é feito dentro do if é subtrair diff de campos. Se ele for 0, nenhuma diferença aparecerá.
</details>
<br/>

### **5. Documentar todo o processo de projeto de testes.**

O processo de projeto de testes utilizando o modelo RIP tornou-se iterativo. Inicialmente, foram construídos apenas os testes básicos que já foram obtidos através do enunciado da OBI. Mesmo com o código sendo aceito pelo validador automático da competição, tivemos mutações sobreviventes. Utilizando o modelo RIP, foi possível verificar que apenas uma das mutações seriam capazes de propagar um erro, e, com isso, foi adicionado um caso de teste para eliminar a mutação.