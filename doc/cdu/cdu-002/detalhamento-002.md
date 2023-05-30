# **Projeto “Nanny's Pets”**
## **Especificação de Caso de Uso**
### **Agendamento de hospedagem**

**Histórico da Revisão**
| **Data** | **Versão** | **Descrição** | **Autor** |
| --- | --- | --- | --- |
| 09/05/2023 | 1.0 | Agendamento de hospedagem | Anna Carolinne |
| 30/05/2023 | 1.1 | Revisão dos detalhamentos para simplificar | Anna Carolinne | </br>

### **1 Resumo**
Usuário acessa “Nanny's Pets” para hospedar seu pet.</br></br>

### **2 Atores**
2.1 Usuário. </br></br>  

### **3 Precondições**  
3.1 Usuário deve estar logado.   
3.2 Usuário deve ter pet cadastrado. </br></br>   

### **4 Pós-condições**  
4.1 A hospedagem do pet foi realizada.   </br></br>

### **5 Fluxos de evento**
**5.1 Fluxo básico**
| **Ações do ator** | **Ações do sistema** | 
| --- | --- |
| 1. Acessar a plataforma |  | 
|   | Carregar página inicial da plataforma Nanny’s Pet | 
| 2. Clicar em "Hospedar meu Pet" |  | 
|   | Carrega página que lista hospedagens | 
| 3. Preencher dados referente a hospedagem desejada e clica em "Hospedar"|  | 
|   | Lista cuidadores disponíveis na data desejada | 
| 4. Seleciona cuidador da lista |  |
|   | Exibe página com “Termo de Ética e Responsabilidade” |
| 5. Usuário concorda com termo e confirma hospedagem |  | 
|   | Registra hospedagem com sucesso! |
</br></br>


**5.2 Fluxo alternativo**
| **Ações do ator** | **Ações do sistema** | 
| --- | --- |
| 1. Seleciona cuidador da lista |  |
|   | Exibe página com “Termo de Ética e Responsabilidade” |
| 2. Usuário NÃO concorda com “Termo de Ética e Responsabilidade” |  | 
|   | Impossibilita o usuário de finalizar a hospedagem |
</br></br>

**5.3 Fluxo de exceção**
| **Ações do ator** | **Ações do sistema** | 
| --- | --- |
| 1. Preencher dados referente a hospedagem desejada, sem ter Pet cadastrado e clica em "Hospedar"|  | 
|   | Redireciona para página "Cadastrar Pet" | 
</br></br>
-----------------------------------