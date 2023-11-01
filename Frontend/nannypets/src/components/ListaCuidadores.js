import Card from "./Card"
import styles from "./ListaCuidadores.module.css"

function ListaCuidadores(){
  return(
    <section className={styles.listacuidadores}>
      <br/>
      <br/>
      <br/>
      <br/>
      <h2>Exibindo Resultados</h2><br/>
      <br />
      <br/>
      <section className={styles.lista}>
        <div>
        <Card />
        <Card />
        <Card /> 
        </div> 
      </section>
    </section>    
  )
}

export default ListaCuidadores
