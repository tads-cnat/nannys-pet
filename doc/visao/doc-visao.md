# Documento de Visão

## Histórico de Revisões

| Data |  Versão | Descrição |  Autores |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| 25/04/2023 | 1.0 | Versão inicial |  Walber Ranniere |
| 09/05/2023 | 1.1 | Versão revisada |  Anna Carolinne |
| 30/05/2023 | 1.2 | Versão revisada |  Anna Carolinne |
| 19/09/2023 | 2.0 | Revisão Geral |  Anna Carolinne, Renato Bernardino |
</br>

## 1. Objetivo do projeto
Nosso objetivo principal é aprimorar o sistema de hospedagem para cães e gatos "Nanny's Pets", reconhecendo a crescente demanda de proprietários que, eventualmente, precisam se ausentar e desejam encontrar hospedeiros qualificados para cuidar de seus animais de estimação em um ambiente seguro e adequado.   </br></br>

## 2. Descrição do problema
| **Problema** | A necessidade de se ausentar e precisar de alguém qualificado que cuide e atenda as necessidades do seu pet. |   
| :---: | --- |   
| **Afeta** | Todos aqueles que possuem um animal de estimação e em algum momento necessitam se afastar de sua residência. |   
| **Impacta** | Em evitar uma busca desorganizada por cuidadores de pets ou cancelamentos de compromissos motivados pela falta de opção de ter onde deixar seu animal de estimação.|   
| **Solução** | O Nanny's Pets - que junta de maneira eficiente aqueles que podem disponibilizar o serviço de hospedar um pet com aqueles que precisam dessa hospedagem. |   </br></br>

## 3. Descrição dos usuários 
|  Nome               |          Descrição  |  Responsabilidade|
| :-----------------: | :-----------------: | :-----------------: |
|  Administrador              |  Administrador: Responsável pelo gerenciamento e funcionamento correto da aplicação         |  - Aprovação de cadastros para cuidador; -Validar cadastro de usuário; -Validar operações entre usuário e host (finalização do serviço).|
|  Usuário             |  Usuário: São as pessoas que se cadastram no site com objetivo de arranjar local para seus pets durante o período desejado.         |  - Cadastrar pets para hospedagem; - Cadastra pedido de hospedagem.|
| Cuidador | São as pessoas que se cadastram no site, para disponibilizar a hospedagem dos pets dos outros | Realiza auto-cadastro; - Atende pedidos de hospedagem. |
| Visitante | Sem a necessidade de cadastro | Visualiza cuidadores |
</br>

## 4. Descrição do ambiente dos usuários
* Número de pessoas envolvidas na execução da tarefa? Isso está mudando?  
**Para que a tarefa seja executada são necessárias duas pessoas, uma que disponibiliza os serviços de hospedagem e a outra que precisa desse serviço.**  
* Quaisquer restrições ambientais exclusivas: móveis, externas etc?  
**Não há restrições ambientais.** 
* Que plataformas de sistema são utilizadas hoje? Plataformas futuras?  
**Na pesquisa feita anteriormente via-se ideias parecidas, como é o caso do DogHero e da Prontocan: Hotel, Day Care e Clínica Veterinária.** 
* Que outros aplicativos estão em uso? É necessário que o seu aplicativo interaja com eles?  
**Não há aplicativos similares.** 
</br></br>

## 5. Principais necessidades dos usuários
Conseguir encontrar uma pessoa qualificada, de confiança, com um ambiente seguro e adequado as necessidades do animal e disponível para cuidar e hospedar com todo amor e carinho com que você cuidaria, quando precisar se ausentar e não tiver onde deixá-lo. </br></br>

## 6. Alternativas concorrentes
* **DogHero** o principal concorrente da plataforma, contando com serviços de hospedagem, creche, passeio, veterinário e pet sitter (um cuidador vai até a sua casa para ficar com o seu pet) https://www.doghero.com.br/ </br></br>

E a ambito regional, temos algumas opções como:    </br>

* **Prontocan: Hotel, Day Care e Clínica Veterinária** hotel para animais de estimação. R. Dr. Pedro Segundo de Araújo, 1801 - Capim Macio, Natal - RN, 59082-040 https://www.instagram.com/prontocan_/    </br>

* **Lar Dog Lar - Day Care e Hospedagem** hospedagem animal no bairro do Pitimbu - R. Serra do Tombador, 8098 - Pitimbú, Natal - RN, 59068-160 https://hotelzinhopetlardoglar.negocio.site/    </br>

## 7. Visão geral do produto
Uma plataforma que conecta pessoas com tempo, qualificação, um ambiente seguro, disposição, amor e carinho para acolher animais de estimação, com indivíduos em busca de cuidadores de confiança para garantir o bem-estar de seus amados animaizinhos nas horas de necessidade.  </br></br>

## 8. Requisitos funcionais
| Código              |  Nome               |          Descrição  |  Prioridade         |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| F01 | Cadastrar usuário | O usuário geral realiza o cadastro no sistema | Essencial |
| F02 | Cadastrar cuidador | O usuário após se cadastrar pode se tornar cuidador na plataforma, informando valores e preferências | Essencial |
| F03 | Aprovar cadastro de cuidador | O administrador avalia a solicitação e decide se aprova ou rejeita a solicitação de acesso de cuidador ao usuário | Desejável |
| F04 | Login usuário | O usuário (cuidador ou dono do pet), exceto visitante, realiza login no sistema | Essencial |
| F05 | Buscar cuidador | O dono do pet ou visitante busca um cuidador no sistema | Essencial |
| F06 | Solicitar hospedagem | O dono do pet solicita a hospedagem enviando um pedido de hospedagem a um cuidador | Essencial |
| F07 | Confirmar hospedagem | O cuidador confirma a hospedagem | Essencial |
| F08 | Cancelar hospedagem | O cuidador ou dono do pet cancelam a hospedagem | Essencial |
| F09 | Realizar pagamento | O dono do pet realiza o pagamento do valor mediante termos de contrato de serviço | Essencial |
| F10 | Confirmar pagamento | O cuidador confirma o pagamento | Essencial |
| F11 | Finalizar hospedagem | O dono do pet finaliza o processo de hospedagem e confirma a retirada do pet | Essencial |
| F12 | Avaliar cuidador | O dono do pet avalia o cuidador após o fim da hospedagem | Desejável |
| F13 | Avaliar dono do pet | O cuidador avalia o dono do pet após o fim da hospedagem | Desejável | 
</br>

## 9. Requisitos não-funcionais
| Código              |  Nome               |          Descrição  |  Categoria          |  Classificação      |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| NF01 | Segurança dos Dados | Manter os dados pessoais dos usuários privados | Segurança | Essencial |
| NF02 | Responsividade | O Sistema Web deve ser responsivo para o uso em diversos dispositivos | Usabilidade | Desejável |
| NF03 | Funcionamento | O Sistema deve suportar o uso de vários usuários ao mesmo tempo com qualidade e velocidade | Usabilidade | Desejável |
