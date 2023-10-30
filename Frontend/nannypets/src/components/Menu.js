import logo from './img/logo.png'
import perfil from './img/perfil.png'

function Menu(){
    return(
        <div className="menu">
            <header>
            <img src={logo} alt="imagem" style={{ float: 'left', width: '200px', padding: '1em' }} />
            <img src={perfil} alt="imagem" style={{ float: 'right', width: '50px', padding: '1.5em' }} />

            </header>
        </div>    
    )
}

export default Menu