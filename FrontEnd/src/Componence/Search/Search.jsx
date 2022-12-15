import React, { useState } from 'react'
import Form from 'react-bootstrap/Form';
// import Button from 'react-bootstrap/Button';
import "./Search.css";
import { ReactSearchAutocomplete } from 'react-search-autocomplete'
import axios from "../../Utils/Axios";

const Search = () => {
  const [What, SetWhat] = useState([])
  const [Where, SetWhere] = useState([])


 // what section 
  const handleOnSelectWhat = (item) => {
    console.log(item)
  }
  const handleOnWhat = () => {
    console.log('Focused');
    jobtypes();
  }

  const jobtypes = async () => {
    const res = await axios.get('api/jobtypes/').then((responce) => {
      if (responce.status === 200) {
        SetWhat(responce.data);
        console.log('countries get successfully');
      }
    })
  }


  // where section 
  const handleOnSelectWhere = (item) => {
    console.log(item)
  }
  const handleOnWhere = () => {
    console.log('Focused')
    countries();
  }
  const countries = async () => {
    const res = await axios.get('api/countries/').then((responce) => {
      if (responce.status === 200) {
        SetWhere(responce.data);
        console.log('countries get successfully');
      }
    })
  }


  return (
    <Form className='row mt-3'>
      <div className="col-lg-2 col-12 "></div>
      <div className="col-lg-4 p-2">
        <ReactSearchAutocomplete placeholder="What Job title, Keywords" items={What} autoFocus
          onSelect={handleOnSelectWhat}
          onFocus={handleOnWhat}
        />
      </div>
      <div className="col-lg-4 p-2">
        <ReactSearchAutocomplete placeholder="Where State, Countrie" items={Where} autoFocus
          onSelect={handleOnSelectWhere}
          onFocus={handleOnWhere}
        />
      </div>
      <div className="col-lg-2 p-2">
      </div>
    </Form>
  )
}

export default Search
