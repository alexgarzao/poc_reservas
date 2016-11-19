# poc_reservas
É uma prova de conceito sobre o que seria necessário para poder realizar a reserva de itens (produtos e/ou serviços).
Por ser uma POC, não serão implementados todos os recursos necessários. Além disso, o foco é o controle para fazer uso ou consumo no local, ou seja, não tem como finalidade controlar entregas para cliente (tele-entrega, por exemplo).

Basicamente, está POC é composta por dois componentes:

* Serviço responsável por realizar as reservas

* Testes de aceitação

O serviço, implementado em Python, expõe uma API Restful para acesso aos seus métodos. Ok, microservice seria bem mais legal do que um macroservice, mas isso é uma POC. Os testes de aceitação foram implementados com um framework de testes, o RobotFramework.

As fucionalidades previstas são:

* Inserir estabelecimento: CNPJ, nome fantasia, número de lugares (opcional) e tempo médio de consumo no local (opcional). Número de lugares e tempo médio de consumo no local servem para calcular o máximo de vendas por turno (no caso de estabelecimentos como restaurantes, lancherias, ...)

* Inserir itens de venda de um estabelecimento: Descrição do item, período/horário em que é ofertado, preço por período/horário, compra mínima por período/horário, limite de vendas por turno, limite máximo de vendas por turno/dia, horário de chegada/saída, ocupação máxima por turno, ...

* Retornar calendário por estabelecimento/item/datas: Data, quantidade disponível, valor por item, ...

* Reservar itens de um estabelecimento: Qual item, data ou data inicial/final, quantidade, ...

Como é uma POC, várias coisas NÃO serão abordadadas. Entre elas:

* Controle de clientes dos estabelecimentos

* CRUD completo dos dado. Por exemplo, eu consigo inserir itens, mas não consigo alterá-los e nem excluí-los


## Para executar este projeto
Para executar este projeto, os seguintes passos são necessários:

* cd <MEUS_PROJETOS>

* git clone https://github.com/alexgarzao/poc_reservas.git

* cd poc_reservas

* virtualenv .env

* source .env/bin/active

* pip install -r requirements.txt

* ...
