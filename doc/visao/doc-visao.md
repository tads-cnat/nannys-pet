# Documento de Visão

## Histórico de Revisões

| Data                |  Versão             |          Descrição  |  Autores            |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| 25/04/2023 | 1.0 | Versão inicial |  Walber Ranniere |
| 09/05/2023 | 1.1 | Versão revisada |  Anna Carolinne |
| - | - | - |  - |

## 1. Objetivo do projeto

Objetivo é desenvolver o sistema para o serviço de hospedagem de cachorros e gatos pela necessidade de eventual compromisso dos seus donos, deixando assim seu(s) pet(s) nas casas de hospedeiros que sejam capacitados para realizar o serviço.

## 2. Descrição do problema

|     |      |
| --- | --- |
| **Problema**            | A necessidade de estar fora do lar sem ter ninguém que cuide do seu pet. |
| **Afeta**               | Todos aqueles que possuem um pet de estimação e em algum momento necessitam se afastar de sua residência. |  
| **Impacta**             | Em evitar uma busca desorganizada por cuidadores de pets ou cancelamentos de compromissos motivados pela não possibilidade de ter onde deixar seu pet.|
| **Solução**             | Uma plataforma web que junte aquele que pode disponibilizar o serviço de hospedar um pet com aquele que precisa dessa hospedagem para o seu pet. | 

## 3. Descrição dos usuários 

|  Nome               |          Descrição  |  Responsabilidade|
| :-----------------: | :-----------------: | :-----------------: |
|  Administrador              |  Administrador: Responsável pelo gerenciamento e funcionamento correto da aplicação         |  - Aprovação de cadastros para cuidador; -Validar cadastro de usuário; -Validar operações entre usuário e host(finalização do serviço).|
|  Usuário             |  Usuário: São as pessoas que se cadastram no site com objetivo de arranjar local para seus pets durante o período desejado.         |  - Cadastrar pets para hospedagem; - Cadastra pedido de hospedagem.|
| Cuidador | São as pessoas que se cadastram no site, para disponibilizar a hospedagem dos pets dos outros | Realiza auto-cadastro; - Atende pedidos de hospedagem. |
| Visitante | Sem a necessidade de cadastro | Visualiza cuidadores |



## 4. Descrição do ambiente dos usuários

* Número de pessoas envolvidas na execução da tarefa? Isso está mudando?  
**Para que a tarefa seja executada são necessárias duas pessoas, uma que disponibiliza os serviços de hospedagem e a outra que precisa desse serviço.**  
* Quaisquer restrições ambientais exclusivas: móveis, externas etc?  
**Não há restrições ambientais.** 
* Que plataformas de sistema são utilizadas hoje? Plataformas futuras?  
**Na pesquisa feita anteriormente via-se ideias parecidas, como é o caso do DogHero e da Prontocan: Hotel, Day Care e Clínica Veterinária.** 
* Que outros aplicativos estão em uso? É necessário que o seu aplicativo interaja com eles?  
**Não há aplicativos similares.** 

## 5. Principais necessidades dos usuários

Conseguir encontrar uma pessoa de confiança disponível para cuidar do seu pet, com todo amor carinho com que você cuidaria, quando precisar sair e não tiver onde deixá-lo. 

## 6. Alternativas concorrentes

* **DogHero** o principal concorrente da plataforma, contando com serviços de hospedagem, creche, passeio, veterinário e pet sitter (um cuidador vai até a sua casa para ficar com o seu pet) https://www.doghero.com.br/

* **Prontocan: Hotel, Day Care e Clínica Veterinária** hotel para animais de estimação. R. Dr. Pedro Segundo de Araújo, 1801 - Capim Macio, Natal - RN, 59082-040 https://www.instagram.com/prontocan_/ 

* **Lar Dog Lar - Day Care e Hospedagem** hospedagem animal no bairro do Pitimbu - R. Serra do Tombador, 8098 - Pitimbú, Natal - RN, 59068-160 https://hotelzinhopetlardoglar.negocio.site/

## 7. Visão geral do produto

Plataforma que intermedia e organiza o contato entre pessoas que tem tempo, amor, disposição e carinho para receber os pets e pessoas que buscam alguém de confiança para deixar seu animalzinho na hora da necessidade.

## 8. Requisitos funcionais

| Código              |  Nome               |          Descrição  |  Prioridade         |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| F01 | Cadastrar usuário | O usuário geral realiza o cadastro no sistema | Essencial |
| F02 | Cadastrar cuidador | O usuário após se cadastrar pode se tornar cuidador na plataforma, informando valores e preferências | Essencial |
| F03 | Aprovar cadastro de cuidador | O administrador avalia a solicitação e decide se aprova ou rejeita a solicitação de acesso de cuidador ao usuário | Desejável |
| F04 | Login usuário | O usuário (cuidador ou dono do pet), exceto visitante, realiza login no sistema | Essencial |
| F05 | Adicionar pet | O dono do pet adiciona seu pet e as demais informações | Essencial |
| F06 | Buscar cuidador | O dono do pet ou visitante busca um cuidador no sistema | Essencial |
| F07 | Solicitar hospedagem | O dono do pet solicita a hospedagem enviando um pedido de hospedagem a um cuidador | Essencial |
| F08 | Confirmar hospedagem | O cuidador confirma a hospedagem | Essencial |
| F09 | Cancelar hospedagem | O cuidador ou dono do pet cancelam a hospedagem | Essencial |
| F10 | Realizar pagamento | O dono do pet realiza o pagamento do valor mediante termos de contrato de serviço | Essencial |
| F11 | Confirmar pagamento | O cuidador confirma o pagamento | Essencial |
| F12 | Finalizar hospedagem | O dono do pet finaliza o processo de hospedagem e confirma a retirada do pet | Essencial |
| F13 | Avaliar cuidador | O dono do pet avalia o cuidador após o fim da hospedagem | Desejável |
| F14 | Avaliar dono do pet | O cuidador avalia o dono do pet após o fim da hospedagem | Desejável |

## 9. Requisitos não-funcionais

| Código              |  Nome               |          Descrição  |  Categoria          |  Classificação      |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| NF01 | Segurança dos Dados | Manter os dados pessoais dos usuários privados | Segurança | Essencial |
| NF02 | Responsividade | O Sistema Web deve ser responsivo para o uso em diversos dispositivos | Usabilidade | Desejável |
| NF03 | Funcionamento | O Sistema deve suportar o uso de vários usuários ao mesmo tempo com qualidade e velocidade | Usabilidade | Desejável |
