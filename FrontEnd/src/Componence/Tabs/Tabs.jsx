import React from 'react'
import Container from 'react-bootstrap/Container';
import "./Tabs.css"
const Tabs = () => {
  return (
    <Container >
      <div className="row mt-4 border p-2">
        <div className="col-lg-3"></div>
        <div className="col-lg-3">
          <div className='text-center'><h1>Job Feed</h1></div>
          <div className='active-tab'></div>
        </div>
        <div className="col-lg-3">
          <div className='text-center'><h1>Recent search</h1></div>
          <div className='active-tab'></div>
        </div>
        <div className="col-lg-3"></div>
      </div>
    </Container>
  )
}

export default Tabs
