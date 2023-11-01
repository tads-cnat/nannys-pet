import styles from './Card.module.css'
import perfil from './img/perfil.png'

function Card(){
   return(
    <section className={styles.card}>
            <img src={perfil} alt="imagem" style={{ float: 'right', width: '50px', padding: '1.5em' }} />
            <h3>Nome</h3>
            <a href="">Enviar Mensagem</a>  
    </section>
   ) 
}

export default Card