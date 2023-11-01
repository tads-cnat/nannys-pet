
import './App.css';
import HelloWorld from './components/HelloWorld'
import Filtro from './components/Filtro'
import Menu from './components/Menu'
import Card from './components/Card'


function App() {
  
  return (
    <div className="App">
      <Menu />
      <Filtro />
      <HelloWorld /> 
    </div>
  );
}

export default App;


