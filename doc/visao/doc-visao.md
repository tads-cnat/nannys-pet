# Documento de Visão

## Histórico de Revisões

|    Data    | Versão |    Descrição    |                           Autores                            |
| :--------: | :----: | :-------------: | :----------------------------------------------------------: |
| 25/04/2023 |  1.0   | Versão inicial  |                       Walber Ranniere                        |
| 09/05/2023 |  1.1   | Versão revisada |                        Anna Carolinne                        |
| 30/05/2023 |  1.2   | Versão revisada |                        Anna Carolinne                        |
| 19/09/2023 |  2.0   |  Revisão Geral  |              Anna Carolinne, Renato Bernardino               |
| 27/09/2023 |  2.1   |  Revisão Geral  | Anna Carolinne, Renato Bernardino, Virginia Claudia, Gabriel Ricardo |
|   </br>    |        |                 |                                                              |

## 1. Objetivo do projeto

Nosso objetivo principal é aprimorar o sistema de hospedagem para cães e gatos "Nanny's Pets", reconhecendo a crescente demanda de proprietários que, eventualmente, precisam se ausentar e desejam encontrar hospedeiros qualificados para cuidar de seus animais de estimação em um ambiente seguro e adequado.   </br></br>

## 2. Descrição do problema

| **Problema** | A necessidade de se ausentar e precisar de alguém qualificado que cuide e atenda as necessidades do seu pet. |
| :----------: | ------------------------------------------------------------ |
|  **Afeta**   | Todos aqueles que possuem um animal de estimação e em algum momento necessitam se afastar de sua residência. |
| **Impacta**  | Em evitar uma busca desorganizada por cuidadores de pets ou cancelamentos de compromissos motivados pela falta de opção de ter onde deixar seu animal de estimação. |
| **Solução**  | O Nanny's Pets - que junta de maneira eficiente aqueles que podem disponibilizar o serviço de hospedar um pet com aqueles que precisam dessa hospedagem. |

## 3. Descrição dos usuários 

|     Nome      |                          Descrição                           |                    Responsabilidade                    |
| :-----------: | :----------------------------------------------------------: | :----------------------------------------------------: |
| Administrador | Administrador: Responsável pelo gerenciamento e funcionamento correto da aplicação |                                                        |
|     Tutor     | Usuário: São as pessoas que se cadastram no site com objetivo de arranjar local para seus pets durante o período desejado. |   Realiza auto-cadastro; - Pesquisa por cuidadores.    |
|   Cuidador    | São as pessoas que se cadastram no site, para disponibilizar a hospedagem dos pets dos outros | Realiza auto-cadastro; - Atende pedidos de hospedagem. |
|   Visitante   |                Sem a necessidade de cadastro                 |                  Visualiza cuidadores                  |
|     </br>     |                                                              |                                                        |

## 4. Descrição do ambiente dos usuários

* Número de pessoas envolvidas na execução da tarefa? Isso está mudando?  
  **Para que a tarefa seja executada são necessárias duas pessoas, uma que disponibiliza os serviços de hospedagem e a outra que precisa desse serviço.**  
* Quaisquer restrições ambientais exclusivas: móveis, externas etc?  
  **Não há restrições ambientais.** 
* Que plataformas de sistema são utilizadas hoje? Plataformas futuras?  
  **Sistema de de plataforma web. Futuramente será desenvolvido sistema mobile** 
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

| Código |        Nome         |                          Descrição                           | Prioridade |
| :----: | :-----------------: | :----------------------------------------------------------: | :--------: |
|  F01   |   Cadastrar tutor   |        O usuário geral realiza o cadastro no sistema         | Essencial  |
|  F02   | Cadastrar cuidador  | O usuário ao realizar o cadastro como cuidador informará dados pessoais (nome completo, endereço e contato de WhatsApp), e dados específicos de cuidador: aceita animais que necessitam de cuidados especiais, porte do animal, características gerais do animal (temperamento, sexo, espécie) tipo de instalações, valores do serviço | Essencial  |
|        |                     |                                                              |            |
|  F03   |    Login usuário    |   O usuário (cuidador ou tutor), realiza login no sistema    | Essencial  |
|  F04   |   Buscar cuidador   |   O dono do pet ou visitante busca um cuidador no sistema    | Essencial  |
|  F05   |  Avaliar cuidador   | O dono do pet avalia o cuidador após o fim da hospedagem, usando um sistema de 1 a 5 estrelas. | Desejável  |
|  F06   | Avaliar dono do pet | O cuidador avalia o dono do pet após o fim da hospedagem, usando um sistema de 1 a 5 estrelas. | Desejável  |
| </br>  |                     |                                                              |            |

## 9. Requisitos não-funcionais

| Código |        Nome         |                          Descrição                           |  Categoria  | Classificação |
| :----: | :-----------------: | :----------------------------------------------------------: | :---------: | :-----------: |
|  NF01  | Segurança dos Dados |        Manter os dados pessoais dos usuários privados        |  Segurança  |   Essencial   |
|  NF02  |   Responsividade    | O Sistema Web deve ser responsivo para o uso em diversos dispositivos | Usabilidade |   Desejável   |
|  NF03  |    Funcionamento    | O Sistema deve suportar o uso de vários usuários ao mesmo tempo com qualidade e velocidade | Usabilidade |               |
