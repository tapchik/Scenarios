import React from 'react';

import 'bootstrap/dist/css/bootstrap.css';
import ProgressBar from 'react-bootstrap/ProgressBar';
import Button from 'react-bootstrap/Button';

import '../css/common.css';
import '../css/TestPlanBrief.css';

function Percentage(finished, total) {
    var percent
    if (total == 0)
        percent = 100
    else
         percent = Math.floor((finished / total) * 100)
    return percent
}

function TestPlanBrief(props) {
    return (
        <div className='plan-brief-container'>
            <div className='plan-brief-body'>
                <p style={{fontSize: '12px'}}>{props.testplan.plan_ident}</p>
                <p>{props.testplan.title}</p>
                <p style={{fontSize: '12px'}}>Date created: {props.testplan.date_created}</p>
            </div>
            <div className='plan-brief-status'>
                <Button variant="primary" href={"/plan?id="+props.testplan.plan_id}>Visit</Button>
                <ProgressBar style={{backgroundColor: 'rgb(190 198 195)'}} now={Percentage(props.testplan.test_suites_finished, props.testplan.test_suites_total)} />
                <p style={{fontSize: '12px', color: '#74857f'}}>
                    {props.testplan.test_suites_finished}/{props.testplan.test_suites_total} suites passed
                </p>
            </div>
        </div>
    )
}

export default TestPlanBrief;