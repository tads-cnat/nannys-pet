function Filtro(){
    return(
        <div class="container">
            
            <body>
                <header className="header">
                    <p><strong>Encontre o cuidador mais perto de você</strong></p>

                    <input type="text" id="txtBusca" placeholder="Adicionar Local"/>

                    <p>Selecione filtros </p>
                
                    
                </header>

                <input class="botao" type="button" value="Adestrador"/>
                <input class="botao" type="button" value="Pet até 5kg"/>
                <input class="botao" type="button" value= "Múltiplos Animais"/>
                <button class="botao">Pet de 20 a 40 kg</button>
                <button class="botao">Médico veterinário</button>
                <button class="botao">Pet de 5kg até 10kg</button>
                <button class="botao">Pet castrado</button>
                <button class="botao">Pet de 40kg+</button>
                <button class="botao">Estudante veterinário</button>
                <button class="botao">Pet de 10kg até 20 kg</button>
                <button class="botao">Pet não castrado</button>
                <button class="botao">Pet macho</button>
                <button class="botao">Medicação injetável</button>
                <button class="botao">Pet fêmea</button>
                <button class="botao">Dificuldade de locomoção</button>
                <button class="botao">Somente gatos</button>
                <button class="botao">Medicação oral</button>
                <button class="botao">Somente cães</button>
            </body>
        </div>
    )
}

export default Filtro