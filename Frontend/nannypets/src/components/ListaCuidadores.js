import Card from './Card'
import styles from './ListaCuidadores.module.css'

function ListaCuidadores(){
    return(
        <section className={styles.listar}>
            <Card />
            <Card />
            <Card />
        </section>
    )
}

export default ListaCuidadores 