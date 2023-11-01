import Menu from "./components/Menu"
import ListaCuidadores from './components/ListaCuidadores';


function PaginaLista() {
  
    return (
      <><div className="paginalista">
            <Menu />
        </div><div className="listacuidador">
                <ListaCuidadores />
            </div></>
    );
  }
  
  export default PaginaLista;