# **Projeto “Nanny's Pets”**
## **Especificação de Caso de Uso**
### **Agendamento de hospedagem**
**Histórico da Revisão**
| **Data** | **Versão** | **Descrição** | **Autor** |
| --- | --- | --- | --- |
| 09/05/2023 | 1.0 | Agendamento de hospedagem | Anna Carolinne |
### **1 Resumo**
O usuário que deseja utilizar o “Nanny's Pets” para hospedar seu pet.

### **2 Atores**
2.1 Usuário  

### **3 Precondições**  
3.1 Usuário deve estar logado   
3.2 Usuário deve ter pet cadastrado   

### **4 Pós-condições**  
4.1 A hospedagem do pet está realizada e é exibida uma página de confirmação.   

### **5 Fluxos de evento**
**5.1 Fluxo básico**
1 Usuário clica no link “hospedar meu pet” disponível no dashboard da página.   
2 O sistema apresenta a página de hospedagem.    
3 Usuário preenche os dados referentes a hospedagem do pert, data e informações do animal a ser hospedado.       
4 Sistema lista os cuidadores disponiveis na data informada.   
5 Usuário seleciona cuidador da lista.   
6 É exibido o “Termo de Ética e Responsabilidade” com os direitos e deveres dos usuários sobre os serviços de hospedagem na plataforma “Nanny's Pets”, após ler e concordar com o Termo de Ética da Empresa o usuário clica em “Realizar hospedagem”.   


**5.2 Fluxo alternativo**
1. ...

**5.3 Fluxo de exceção**
1. Caso o usuário não tenha Pet cadastrado, ele é redirecionado a página de "Cadastrar Pet"


-----------------------------------

![Diagrama do CDU2](https://github.com/tads-cnat/receber-pets/blob/documentar-cdus/doc/cdu/diagramas-cdu/CDU02.png?raw=true)
