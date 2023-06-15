import React from 'react';
import CircularProgress from '@mui/material/CircularProgress';

import 'bootstrap/dist/css/bootstrap.css';
import Button from 'react-bootstrap/Button';

import '../css/common.css';
import '../css/TestPlanBrief.css';

function TestPlanBrief(props) {
    return (
        <div className='plan-brief-container'>
            <CircularProgress variant="determinate" value={60} />
            <p>{props.testplan.plan_ident}: {props.testplan.title} ({props.testplan.test_suites_finished}/{props.testplan.test_suites_total})</p>
            <Button variant="primary" onClick={() => window.location.assign("/plan?id="+props.testplan.plan_id)}>Visit</Button>
        </div>
    )
}

export default TestPlanBrief;