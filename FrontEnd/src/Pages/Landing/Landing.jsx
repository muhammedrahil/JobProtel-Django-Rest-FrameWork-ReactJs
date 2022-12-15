import React from 'react'
import NavBar from '../../Componence/NavBar/NavBar'
import Search from '../../Componence/Search/Search'
import Tabs from '../../Componence/Tabs/Tabs'


const Landing = () => {
  return (
    <div>
      <div className="container-fluid">
        <div className="row">
          <NavBar/>
          <Search/>
          <Tabs/>
        </div>
      </div>
      
    </div>
  )
}

export default Landing
