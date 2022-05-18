

class CoffeeLady:

    def __init__(self):
        pass


    def helpme(self):
        print("Olá! No que posso ajudar?")
        print("Vamos lá!")
        print("A primeira coisa que você precisa saber é se os seus dados seguem, ou não, a distribuição Normal")
        print("Os seus dados são Normais?")
        print("Sim", "Não", "Não sei")
        if "Sim":
            print("Ok!")
            print("Agora eu preciso saber quantas amostras você deseja comparar")
            print("Uma", "Duas", "Mais de duas")
            if "Uma":
                print("Ok!")
                print("Com uma amostra que segue a distribuição Normal, é possível apenas comparar a média desta amostra com um valor determinado.")
                print("O teste mais adequado para fazer esta comparação é o teste t de Student")
                print("O PyCafee já tem este teste programado!")
                print("Você pode utilizar a classe Sample para fazer este teste, atravé do método t_student(), passando o valor determinado como parâmetro.")
                print("É importante lembra-lo que é preciso aplicar o método fit previamente, que é o momento onde os dados experimentais são passados para o programa")
                print("Se você tiver dúvias sobre como proceder, pode visualizar o notebook de exemplo, neste link")
                print("Dica: basta apenas substituir os dados utilizados pelos seus dados")
                print("Não esqueça de dar uma olhada da documentação! Você vai encontrar mais detalhes por lá, inclusive como referenciar o método")
            elif "Duas":
                print("Ah, duas amostras!")
                print("Eu preciso saber algumas informações sobre estas duas amostras")
                print("Qual é a relação entre elas? Elas foram obtidas de forma indepentende ou elas são pareadas?")
                    if "Pareadas":
                        print("Entendi!")
                        print("Então você quer comparar duas amostras que seguem a distribuição Normal e que foram obtidas de forma pareada!")
                        print("Para fazer esta comparação, você pode utilizar o teste t de Student para amostras pareadas!")
                        print("O PyCafee já tem este teste implementado!")
                        print("E você pode aplicalo, utilizando a classe TwoSamples, e aplicando o método pair_t_Student")
                        print("Lembrando que é preciso aplicar o método fit previamente, que é o momento onde você passa os dados para o prgrama")
                        print("Se você tiver dúvias sobre como proceder, pode visualizar o notebook de exemplo, neste link")
                        print("Dica: basta apenas substituir os dados utilizados pelos seus dados")
                        print("Não esqueça de dar uma olhada da documentação! Você vai encontrar mais detalhes por lá, inclusive como referenciar o método")
                    elif "Independentes":
                        print("ok!")
                        print("Para comparar duas amostras que seguem a distribuição Normal e que foram obtidas de forma idependente, eu preciso saber se as variâncias dessas duas amostras são homogêneas")
                        print("Sim", "Não", "Não sei")
                        if "Sim":
                            print("Perfeito")
                            print("O teste recomendado para comparar duas amostras independetes, que seguem a distirbuição Normal e que possuem variãncias homogenas é o teste t de Student para amostras homogeenas")
                        elif "Não":
                            print("Perfeito")
                            print("O teste recomendado para comparar duas amostras independetes, que seguem a distirbuição Normal e que possuem variãncias homogenas é o teste t de Student para amostras não homogeenas")
                        else:
                            print("Tudo bem! Mas precisamos descobrir!")
                            print("Existem alguns testes para fazer esta verificação, como os testes de levene, Bartlett ou o teste F.")
                            print("Mas como você quer comparar duas amostras, o teste recomendado é o teste F")
                            print("O PyCafee já tem este teste implementado! Você pode fazer ele utilizando a classe TwoSamples, aplicando o método homogenetycheck!")
                            print("Por padrão, este método aplica o teste F! Mas você pode alterar para outros testes, passando o nome do teste como parâmetro")
                            print("Lembrando que é preciso aplicar o método fit previamente, que é o momento onde você passa os dados para o prgrama")
                            print("Se você tiver dúvias sobre como proceder, pode visualizar o notebook de exemplo, neste link")
                            print("Dica: basta apenas substituir os dados utilizados pelos seus dados")
                            print("Não esqueça de dar uma olhada da documentação! Você vai encontrar mais detalhes por lá, inclusive como referenciar o método")
                    else:
                        print("Tudo bem!")
                        print("Mas para poder fazer uma boa recomenção, é preciso saber.")
                        print("Não existe, pelo menos até onde eu saiba, um teste para verificar se as amostras são independentes ou pareadas. Isto esta mais no conceito filosófico!")
                        print("Amostras indepentendes são aquelas que são obtidas de forma inpedennte das outras, sendo possível obter estes dados em dias diferentes, por exemplo")
                        print("Já as amostras pareadas, são aquelas que foram obtidas aos pares, e existe um relação intrinsica entre elas. Os conjuntos pareados sempre terão o mesmo número amostral, o que não é sempre verdade para as amostras independentes (embora seja algo recomendado)")
            else:
                print("Mais de duas amostras, ok!")
                print("A comparação entre mais de duas amostras é geralmente feita utilizando o teste de Fisher ou de teste de Tukey. O teste de Dunnnet também é utilizado, mas apenas quando desejamos comparar todas as amostras com uma amostra de referência")
                print("De qualquer forma, todos estes testes exigem que seja feito o teste de ANOVA previamente. Isto é um pressuposto. Também é importante que as variãncias entre os grupos sejam homogeneas. Mas, vamos por partes, como diria o Jack")
                print("O teste de ANOVA nos informa se existem amostras diferentes entre os grupos. Existem?")
                print("Sim", "Não", "Não sei")
                if "Sim":
                    print("Legal!")
                    print("Isto quer dizer que pelo menos uma amostra é diferente das demais!")
                    print("Vamos descobrir qual!")
                    print("Mas antes disso, é preciso verificar se as variâncias são homogeneas")
                    print("As variâncias serem homogeneas é um pressuposto dos testes de comparação múltipla, e são imporantas para garantir que o nível de significância do teste seja mantido constante")
                    print("As variâncias são homogeneas?")
                    print("Sim", "Não", "Não se")
                    if "Sim":
                        print("Perfeito! Podemos seguir com os testes!")
                    elif "Não":
                        print("hum, ok!")
                        print("O fato de que as variãncias das amostras não são iguais indica que pelo menos uma delas varia de forma bastante diferente das demais")
                        print("Infelizmente, não temos testes específicos para estes casos, e a literatura reporta o uso dos testes de comparação múltima mesmo quando este pressuposto é violado")
                        print("Entretanto, a maioria dos livros indica que caso as amostras tenham o mesmo tamanho, ta 'tudo bem'")
                        print("Assim, se todas as amostras tiverem o mesmo tamanho amostral, você pode seguir sem preocupações")
                        print("Mas caso elas sejam diferentes, é uma boa ideia voltar para o laboratório e obter mais amostras de forma que os grupos tenham tamanhos iguais")
                    else:
                        print("Então precisamos descorbrir!")
                        print("Existem alguns testes para fazer esta verificação, como os testes de Levene e o Bartlett e suas variações")
                        print("Em geral, o teste de Levene é o mais utilizado, pois ele não é tão rigído em relação aos dados serem Normais. Ele tem um bom poder de decisão mesmo quando os dados não são exatamente Normais.")
                        print("Já o teste de Bartlett é mais adequado para quando temos dados que realmente são Normais")
                        print("Se cada grupo tiver pelo menos 6 amostras, não exite e aplique o teste de Levene")
                        print("Se os grupos tiverem mais do que seis amostras, talvez o teste de Bartlett seja melhor")
                        print("Mas, todo mundo que passa por aqui sempre usa o teste de Levene. Eu usaria ele")
                        print("O PyCafee já tem este teste implementado! Você pode fazer ele utilizando a classe MultiSamples, aplicando o método homogenetycheck!")
                    print("Agora é preciso escolher um teste. Os mais utilizados são os testes de Tukey e Fisher para comparação múltipla, e o teste de Dunnet para comparação com um controle.")
                    print("Qual você deseja fazer?")
                    print("Comparação múltipla", "Controle")
                    if "Comp Multipla":
                        print("Legal!")
                        print("Agora é preciso esclher entre os testes de Tukey e Fisher")
                        print("Estes testes diferem basicamente na forma de proteger o teste quando ao aumento do nível de sgnificancia na medida em que aumentamos o número de grupos que estão sendo comparados")
                        print("Por exemplo, quando comparamos duas amostras, adotamos um nível de significancia alfa para o teste, que geralmetne é de 5%")
                        print("Assim, admitimos que temos 5% de chance da conclusão do teste estar errada, e 95% de chance da conclusão esta certa, que é a chance de cometer um erro de tipo I")
                        print("Mas quando vamos comparar três ou mais amostras, este nível de significância pode aumentar.")
                        print("Por exemplo, caso temos e grupos sendo comparado, o grupo A, B e C")
                        print("O teste de ANOVA nos disse que pelo menos um entre estes três são diferentes, mas para saber, precisamos compara-los, par a par")
                        print("Assim, temos de fazer um teste comparando A e B")
                        print("Um outro teste comparando A e C")
                        print("E um terceiro teste comparando B e C")
                        print("Em cada uma destas comparações, estamos utilizando um nível de significania, e a cada comparação, temos alfa chance de cometer um erro do tipo I. Ou seja, quando mais comparações fazemos, mais chances de errar!")
                        print("Os testes de Fisher e Tukey nos protegem quanto a este aumento de alfa, adotando formas diferentes")
                        print("Os livros geralmetne dizem que o teste de Fisher é exato para quando estamos comparando 3 grupos. Para mais de 3 grupos, ele não protege tão bem")
                        print("Já o teste de Tukey tende a proteger muito bem para qualquer n, desde que os grupos tenham variâncias iguais e que o tamanho amostra seja igual")
                        print("Assim, caso você esteja comparando 3 grupos, utilize o teste de Fisher ou o teste de Tukey. Caso esteja comparando 4 ou mais grupos, utilize o teste de Tukey.")
                        print("O PyCafee já tem estes doiss testes implementados! Você pode fazer ele utilizando a classe MultiSamples, aplicando o método fisher ou o método tukey!")
                    elif "Controle":
                        print("Legal! Para comparar varios grupos com um grupo controle, geralmente é utilizado o teste de Dunnnet")
                        print("Mas atenção! As comparações neste teste não são feitas entre todos os pares! Elas são feitas entre cada grupo e o grupo controle")
                        print("Por exemplo, se temos 3 grupos, A, B e C, e o grupo controle é o grupo C, iremos fazer uma comparação entre o grupo A e o grupo C, e entre o grupo B e o grupo C.")
                        print("Repare que as médias dos grupos A e B não são comparadas entre si")
                        print("Além disso. no teste de Dunnet temos a possibildiade, e que é algo recomendado na verdade, de que o grupo controle tenha uma quantidade maior de repetições do que os demais grupos")
                        print("No artigo original, que me falta o nome, o Dunnnet traz uma tabela com os valores tabelados corrigidos para o caso onde o grupo controle tem mais observações")
                        print("Além disso, existe um regra para saber quantas repetições o grupo controle deve ter, baseado no número de repetições dos demais grupos")
                        print("O PyCafee já traz isto de forma simplificada! Através da classe MultiSamples, você pode utilizar o método dunnetcheck para fazer esta verificação!")
                        print("E o PyCaffe também aplica o teste! Basta utilizar o método dunnet, que deve indicar qual grupo que é o controle ")
                    else:
                        print("Bom, se você esta em dúvida, muito provavelmente você esta atrás dos testes de comparaão mútipla, e não de um teste de comparação com o controle.")
                elif "Não":
                    print("Então ok!")
                    print("Se o teste de ANOVA informou que todas as médias são iguais, não tem necessidade de aplicar mais testes, você já tem sua resposta!")
                    print("Lembrando que os teste de Tukey, Fisher etc, são testes post-hoc, o que significa que eles devem ser feitos apenas se o teste de ANOVA indicar que existem amostras diferentes")
                    print("Pode acontecer de que o teste de ANOVA indique que não existam diferenças entre as amostras, mas o teste post-hoc indique a difereça entre um ou outro grupo. ")
                    print("Mas, o teste de ANOVA tem precedência, e deve ser respeitado")
                else:
                    print("Então vamos descobrir!")
                    print("Você precisa aplicar o teste de ANOVA fator único, o que é bem tranquilo")
                    print("O PyCafee já tem este teste implementado! Você pode fazer ele utilizando a classe MultiSamples, aplicando o método anovacheck!")















#
