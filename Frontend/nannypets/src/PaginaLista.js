import Menu from "./components/Menu"
import ListaCuidadores from './components/ListaCuidadores';


function PaginaLista() {
  
    return (
      <div className="paginalista">
          <header>
            <Menu />
          </header>
          <body>
            <ListaCuidadores />
          </body>
      </div>
          
        
    );
  }
  
  export default PaginaLista;