import React from 'react';
//import logo from './logo.svg';
//import './App.css';
import { Line, Circle } from 'rc-progress';

import TestPlanBrief from '../elements/TestPlanBrief';
import CircularProgress from '../elements/CircularProgress';

import 'bootstrap/dist/css/bootstrap.css';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';


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

                <h1>List of recent Test Plans</h1>
                    
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
