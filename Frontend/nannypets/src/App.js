
import './App.css';
import HelloWorld from './components/HelloWorld'
import Filtro from './components/Filtro'
import Menu from './components/Menu'
import Card from './components/Card'
import ListaCuidadores from './components/ListaCuidadores';

function App() {
  
  return (
    <div className="App">
      <Menu />
      <Filtro />
      <HelloWorld /> 
      <Card />
      <ListaCuidadores />	
    </div>
    
  
  );
}

export default App;


