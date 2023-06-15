import React from 'react';

import 'bootstrap/dist/css/bootstrap.css';
import Button from 'react-bootstrap/Button';

import '../css/common.css';
import '../css/TestSuiteBrief.css';

function TestCaseBrief(props) {
    return (
        <div className='suite-brief-container'>
            <p>{props.testcase.step}</p>
            <p>{props.testcase.title} (11 steps)</p>
            <p>{props.testcase.idea}</p>
            <p>Not passed</p>
            <Button variant="primary" onClick={() => window.location.assign('/show_test_case_to_pass')}>Run</Button>
        </div>
    )
}

export default TestCaseBrief;