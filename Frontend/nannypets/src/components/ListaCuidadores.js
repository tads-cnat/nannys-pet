import Card from "./Card"
import styles from "./ListaCuidadores.module.css"

function ListaCuidadores(){
  return(
    <section className={styles.listacuidadores}>
      <h2>Exibindo Resultados</h2>
      <section className={styles.lista}>
        <Card />
        <Card />
        <Card />
        <Card />  
      </section>
    </section>    
  )
}

export default ListaCuidadores
