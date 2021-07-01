import './App.css';
import React, {useState, createContext, useContext} from 'react';


function Beast(props) {
  
  return (
    <div className='beast'>
      <img className='beast-image' src={props.image}/>
      <div className='total-health-bar'>
        <div className='current-health-bar'></div>
      </div>
    </div>
  )
}


function Display() {
  const rainbow = 'rainbow.png'
  const lava = 'lava.png'

  return (
  <div className='display' style={{backgroundImage: `url("https://i.redd.it/ulisszd010r41.png")`}}>
    <Beast image={rainbow} />
    <Beast image={lava} />
  </div>
  )
}

function Attack(props) {

  return (
    <button className='attack'>
      {props.name}
    </button>
  )

}

function Menu() {
  

  return (
    <div className='menu'>
      <Attack name='Sparkle Strike' />
      <Attack name='Strut'/>
      <Attack name='Flippy Flap' />
      <Attack name='Heckin Chomp' />
    </div>
  )
}

const BeastContext = createContext()

const BeastProvider = props => {
  
  const sparkleStrike = () => {
    //deal 5 damage
  }
  const flippyFlap = () => {
    //avoid the next attack
  }
  const heckinChomp = () => {
    //deal 3 damage, lower the enemy's attack
  }
  const strut = () => {
    //raise your attack
  }

  const [beasts, setBeasts] = useState([
    {
      name: 'Rainbow',
      health: 25,
      attack: 3,
      defense: 4,
      moveset: [sparkleStrike(),strut(),flippyFlap(),heckinChomp()]
    },
    {
      name: 'Lava',
      health: 25,
      attack: 4,
      defense: 3,
      moveset: []
    }
  ])
  return(
    <BeastContext.Provider>
      {props.children}
    </BeastContext.Provider>
  )
}




function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Beasts in your Purse Aw Geeze!</h1>
      </header>
      <main>
        <BeastProvider>
          <Display />
          <Menu />
        </BeastProvider>
      </main>

    </div>
  );
}

export default App;
