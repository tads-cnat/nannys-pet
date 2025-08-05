#  Matriz de Interação de Requisitos – Projeto Nanny’s Pets

|       | RF01 | RF02 | RF03 | RF04 | RF05 | NF01 | NF02 | NF03 |
|-------|------|------|------|------|------|------|------|------|
| RF01 |  –   | 1000 |  0   |  0   |  0   | 1000 |  0   |  0   |
| RF02 | 1000 |  –   |  0   |  0   |  0   | 1000 |  0   |  0   |
| RF03 |  0   |  0   |  –   | 1000 |  0   |  1   | 1000 | 1000 |
| RF04 |  0   |  0   | 1000 |  –   |  0   |  1   | 1000 | 1000 |
| RF05 |  0   |  0   |  0   |  0   |  –   | 1000 |  0   |  0   |
| NF01 |1000  |1000  |  1   |  1   | 1000 |  –   |  0   |  0   |
| NF02 |  0   |  0   |1000  |1000  |  0   |  0   |  –   |  0   |
| NF03 |  0   |  0   |1000  |1000  |  0   |  0   |  0   |  –   |



#  Documento de Negociação de Conflitos – Projeto Nanny’s Pets

## Conflito 1: RF03 (Encontrar cuidadores) vs NF01 (Segurança dos dados)

- **Tipo de conflito:** Privacidade vs Funcionalidade
- **Descrição:** A funcionalidade de busca por endereço completo pode comprometer dados sensíveis dos cuidadores.
- **Resolução:** Aplicação de técnica de **comprometimento (trade-off)** com **anonimização parcial**.
- **Decisão:** A busca será realizada com base em bairro ou raio geográfico. O endereço exato só será revelado após aceite da solicitação de hospedagem.
- **Justificativa:** Garante a funcionalidade desejada, respeitando a privacidade dos usuários.

## Conflito 2: RF04 (Ranking de cuidadores) vs NF01 (Segurança dos dados)

- **Tipo de conflito:** Exposição de dados sensíveis
- **Descrição:** Exibir ranking com avaliações detalhadas pode revelar dados indesejados dos cuidadores.
- **Resolução:** Técnica de **reformulação colaborativa**.
- **Decisão:** Será exibida apenas a média geral da avaliação e o número de hospedagens; avaliações individuais e comentários não serão públicos.
- **Justificativa:** Preserva a privacidade dos cuidadores mantendo os diferenciais da plataforma para os tutores.
