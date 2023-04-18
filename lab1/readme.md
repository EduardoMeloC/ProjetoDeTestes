# Tarefa Prática 1 - Testes de Triângulos

Nesta tarefa, serão dados os códigos de três funções diferentes que, dados os lados de um triângulo a, b, c, retorna se o triângulo é escaleno, isósceles, equilátero ou inválido.

A proposta é que, em sala de aula, os alunos pensem em seus próprios casos de testes para avaliar a execução. Em seguida, eles deverão avaliar se os casos de teste pensados cobrem todos os possíveis casos:

1. Você possui um caso de teste que representa um triângulo escaleno válido? (Note que casos de teste como 1, 2, 3 e 2, 5, 10 não são válidos por conta da desigualdade triangular).
2. Você possui um caso de teste que representa um triângulo equilátero válido?
3. Você possui um caso de teste que representa um triângulo isósceles válido?
4. Você possui ao menos três casos de testes que representam triângulos isósceles válidos tal que você tenha testado todas as três permutações de dois lados iguais? (e.g. 3, 3, 4; 3, 4, 3; e 4, 3, 3)
5. Você possui um caso de teste em que um lado possui o valor zero?
6. Você possui um caso de teste em que um lado possui um valor negativo?
7. Você possui um caso de teste com três inteiros maiores que zero tal que a soma de dois números é igual ao terceiro? (Isso é, se o programa diz que 1, 2, 3 representa um triângulo escaleno, ele conteria um bug)
8. Você possui ao menos três casos de testes na categoria 7 tal que você tenha tentado todas as permutações onde o tamanho de um lado é igual à soma dos outros dois lados? (e.g. 1, 2, 3; 1, 3, 2; e 3, 1, 2)
9. Você possui um caso de teste que contém três inteiros maiores que zero tal que a soma de dois números é menor do que o terceiro? (e.g. 1, 2, 4; ou 12, 15, 30)
10. Você possui ao menos três casos de teste na categoria 9 tal que você tenha testado todas as três permutações? (e.g. 1, 2, 4; 1, 4, 2; e 4, 1, 2)?
11. Você possui um caso de teste em que todos os três lados são zero? (0, 0, 0)
12. Você possui ao menos um caso de teste especificando valores não inteiros? (e.g. 2.5, 3.5, 5.5)
13. Você possui ao menos um caso de teste especificando o número incorreto de valores? (como, por exemplo, dois valores inteiros no lugar de três)
14. Para cada caso de teste, você especificou a saída esperada do programa, além dos valores de entrada?

Em seguida, deverá ser implementado em laboratório os casos de teste em python - sem utilizar uma framework de teste.

Após isso, deve ser feita uma implementação dos testes utilizando unittest ou pytest.

Por fim, deverá ser feito um comentário final de um ou dois parágrafos sobre o processo.
