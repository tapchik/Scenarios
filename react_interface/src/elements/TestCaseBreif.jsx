import React from 'react';

import 'bootstrap/dist/css/bootstrap.css';
import Button from 'react-bootstrap/Button';

import '../css/common.css';
import '../css/TestCaseBrief.css';

function RunButton(button_text){
    var variant
    if (button_text == 'Finished')
        variant = "success"
    else if (button_text == 'Pending')
        variant = "info"
    else 
        variant = "primary"
    return <Button variant={variant}>{button_text}</Button>
}

function TestCaseBrief(props) {
    return (
        <div className='case-brief-container'>
            <div className='case-breif-step'>
                <p style={{marginTop: '18px'}}>{props.testcase.step}</p>
            </div>
            <div className='suite-brief-body'>
                <p>{props.testcase.title}</p>
                <p style={{fontSize: '12px'}}>Idea: {props.testcase.idea}</p>
                <p style={{fontSize: '12px'}}>Expected result: {props.testcase.expected_result}</p>
            </div>
            
            <div className='case-brief-status'>
                {RunButton(props.testcase.finished)}
                <p style={{fontSize: '12px', color: '#74857f', textAlign: 'center'}}>
                    {props.testcase.n_actionable_steps} steps
                </p>
            </div>

        </div>
    )
}

export default TestCaseBrief;