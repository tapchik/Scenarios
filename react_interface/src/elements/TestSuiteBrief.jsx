import React from 'react';

import 'bootstrap/dist/css/bootstrap.css';
import ProgressBar from 'react-bootstrap/ProgressBar';
import Button from 'react-bootstrap/Button';

import '../css/common.css';
import '../css/TestSuiteBrief.css';

function Percentage(finished, total) {
    var percent
    if (total == 0)
        percent = 100
    else
         percent = Math.floor((finished / total) * 100)
    return percent
  }

function TestSuiteBrief(props) {
    return (
        <div className='suite-brief-container'>
            <div className='suite-breif-step'>
                <p style={{marginTop: '30px'}}>{props.testsuite.step}</p>
            </div>
            <div className='suite-brief-body'>
                <p style={{fontSize: '12px'}}>{props.testsuite.suite_ident}</p>
                <p>{props.testsuite.title}</p>
                <p style={{fontSize: '12px'}}>{props.testsuite.description}</p>
            </div>
            <div className='suite-brief-status'>
                <Button variant="primary" href={'/suite?id='+props.testsuite.suite_id + '&ver='+props.testsuite.version + '&plan_id='+props.plan_id}>Visit</Button>
                <ProgressBar style={{backgroundColor: 'rgb(190 198 195)'}} now={Percentage(props.testsuite.test_cases_finished, props.testsuite.test_cases_total)} />
                <p style={{fontSize: '12px', color: '#74857f'}}>
                    {props.testsuite.test_cases_finished}/{props.testsuite.test_cases_total} cases passed
                </p>
            </div>
        </div>
    )
}

export default TestSuiteBrief;