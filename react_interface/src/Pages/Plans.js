import React from 'react';

import TestPlanBrief from '../elements/TestPlanBrief';

import 'bootstrap/dist/css/bootstrap.css';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

import '../css/common.css';

class Plans extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            testplans: [],
        }
    }

    componentDidMount() {
        document.title = "Recent Test Plans";
        this.fetchTestPlans();
    }

    fetchTestPlans() {
        fetch('http://127.0.0.1:8000/api/testplans', {
                method: 'GET',
                credentials: 'include',
            })
            .then(response => response.json())
            .then(data => this.setState({ testplans: data.testplans }))
            .catch(error => console.error('Error: ', error));
    }

    render() {
        return (

            <Container>

                <div className='header'>
                    <h1 style={{'fontSize': '30px'}}>List of recent Test Plans</h1>
                </div>

                <div className='navigation'>
                    <span style={{flexGrow: '2'}}></span>
                    <Button variant='danger'>⌫ Delete plan</Button>
                    <Button variant='success'>+ Add plan</Button>
                </div>
                    
                <div>
                  {this.state.testplans.map((testplan) => (
                        <TestPlanBrief testplan={testplan} key={testplan.plan_ident} />
                  ))}
                </div>

            </Container>
            
        )
    }
}

export default Plans;
