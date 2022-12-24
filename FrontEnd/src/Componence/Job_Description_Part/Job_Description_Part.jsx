import React, { useEffect, useState } from 'react'
import { ImPriceTags } from 'react-icons/im';
import { HiShoppingBag } from 'react-icons/hi';
import { AiFillClockCircle } from 'react-icons/ai';
import Button from 'react-bootstrap/Button';
import { useParams } from "react-router-dom";
import axios from "../../Utils/Axios";

const Job_Description_Part = () => {
  let { id } = useParams();
  const [singlesjob, setsinglejob] = useState(null)

  useEffect(() => {
    singlejob();
  }, [id])

  const singlejob = async () => {
    const res = await axios.get(`api/jobs/${id}/`).then((responce) => {
      if (responce.status === 200) {
        setsinglejob(responce.data);
        console.log('job get successfully');
      }
    })
  }

  return (
    <div className='sticky-lg-top col-lg-10 col-0  m-1 shadow border-primary p-3 border rounded ' style={{ "zIndex": "-1" }} >
      <div className='sticky-top' style={{ "backgroundColor": "white", "lineHeight": "8px" }}>
        <h5 className='fw-bold'>{singlesjob ? singlesjob.job_name.name : ''}</h5>
        <p><a href={singlesjob ? singlesjob.company_name.website_link : ''} >{singlesjob ? singlesjob.company_name.name : ''}</a></p>
        <p>{singlesjob ? singlesjob.company_city.name : ''}, {singlesjob ? singlesjob.company_state.name : ''}, {singlesjob ? singlesjob.company_contry.name : ''}</p>
        <p class="text-dark "> ₹{singlesjob ? singlesjob.start_month_salary : ''} - ₹{singlesjob ? singlesjob.end_month_salary : ''} a month</p>
        <Button className='col-lg-3 fw-bold shadow' >Apply Now </Button>
        <hr />
      </div>
      <div >
        <div className='mt-3' style={{ "lineHeight": "4px" }}>
          <div className='p-1 m-1' style={{ "lineHeight": "1px" }}>
            <p><span className='fw-bold'><ImPriceTags /> Salary</span></p>
            <p class="badge bg-light shadow-sm text-dark "> ₹{singlesjob ? singlesjob.start_month_salary : ''} - ₹{singlesjob ? singlesjob.end_month_salary : ''} a month</p>
          </div>
          <div className='p-1 m-1'>
            <p><span className='fw-bold'><HiShoppingBag /> Job type</span></p>
            <p class="badge bg-light shadow-sm text-dark "> Fresher</p>
            <p class="badge bg-light shadow-sm text-dark ms-1"> Expericed</p>
          </div>
          <div className='p-1 m-1'>
            <p><span className='fw-bold'><AiFillClockCircle /> Shift and schedule</span></p>
            <p class="badge bg-light shadow-sm text-dark">Day shift</p>
            <p class="badge bg-light shadow-sm text-dark ms-1"> Night shift</p>
          </div>
        </div>
        <div style={{ "lineHeight": "8px" }}>
          <h5 className='fw-bold'>Qualifications</h5>
          <ul>
            <li><p>Bachelor's (Preferred)</p></li>
            <li><p>Python: 2 years (Preferred)</p></li>
            <li><p>total work: 3 years (Preferred)</p></li>
          </ul>
        </div>
        <div style={{ "lineHeight": "8px" }}>
          <h5 className='fw-bold'>Full Job Description</h5>
          <div className='p-2'>
            <p>Position - Python Developer</p>
            <p>Framework- Django</p>
            <p>Exp- 2-4 years</p>
            <p>Job Type- Permanent</p>
          </div>
        </div>
        <div style={{ "lineHeight": "18px" }}>
          <h5 className='fw-bold'>Job Description</h5>
          <div className='p-1'>
            <li>Responsibilities include writing and testing code,Responsibilities include writing and testing code, </li>
            <li>Write effective, scalable code</li>
          </div>
        </div>
        <div>
          <h6 className='fw-bold'>Speak with the employer</h6>
          <small><a href="" className='text-decoration-none fs-6'>+91 XXXXXXXXXX</a></small>
        </div>
      </div>
    </div>
  )
}

export default Job_Description_Part
