### **1. Solução do [problema do Banco](https://olimpiada.ic.unicamp.br/pratique/p2/2012/f2/banco/)**

A solução do Problema do Banco foi indicada no arquivo `Banco.py`. É possível executá-la com inputs utilizando o arquivo `main.py`.
Essa solução foi submetida e aceita como válida pelo validador automático da OBI, e uma explicação do algoritmo e do código pode ser obtida [aqui](https://www.youtube.com/watch?v=loitd1Lt0Vo&feature=youtu.be&ab_channel=Rafah).

### **2. Aplicar a ferramenta de mutação com um caso de teste qualquer (sem isso as ferramentas não geram mutantes).**

Os nossos casos de teste qualquer foram os mesmos que estão na página do problema do banco da OBI. No arquivo `test_Banco.py`, são as funções `test_saida_correta_banco1` e `test_saida_correta_banco2`.

Foram gerados **32 mutantes**, dentre os quais **9 sobreviveram**. São eles:


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
  **Mutação Sobrevivente 8**
  ```python
      #print(f"cashiers = {cashier}")
      argwaited = argmin(cashier)
      waited = cashier[argwaited]
-   if(waited<=0):
+   if(waited<0):
        #print(f"{t} got served")
        cashier[argwaited]=service[t]
  ```
  **Mutação Sobrevivente 9**
  ```python
      #print(f"cashiers = {cashier}")
      argwaited = argmin(cashier)
      waited = cashier[argwaited]
-   if(waited<=0):
+   if(waited<=1):
          #print(f"{t} got served")
          cashier[argwaited]=service[t]
  ```
</details>
<br/>


### **3. Projetar testes para matar os mutantes sobreviventes, usando o modelo RIP.**

Com a finalidade de criar o nosso projeto de testes para eliminar os mutantes sobreviventes, precisamos de pensar em como alcançar um trecho de código que apresenta falhas, para em seguida infectar e propagar o erro.


### **4. No caso de haver mutantes equivalentes, procurem mostrar que são equivalentes com uma argumentação rigorosa (vamos trabalhar um pouco mais sobre isso, mas tentem fazer algo).**

<details>
  <summary><b>Mutação Sobrevivente 1</b></summary>

  **Mutação Sobrevivente 1**
  ```python
    def banco(C, arrival, service):
      #perhaps sort arrival and service by arrival
  -   last_arrival = 0
  +   last_arrival = 1
      cashier = [0]*C
      waited = 0
      argwaited = 0
  ```
</details>
Para a **Mutação Sobrevivente 1**, não existe um caso de teste que é capaz de matar o mutantex, configurando esta como uma mutação equivalente. 

### **5. Documentar todo o processo de projeto de testes.**