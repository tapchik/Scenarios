import React from 'react';

import 'bootstrap/dist/css/bootstrap.css';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

import TestSuiteBrief from '../elements/TestSuiteBrief';

import '../css/common.css';

class Plan extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            testplan: {
              plan_ident: "yes",
              testsuites: [],
            },
        }
    }

    componentDidMount() {
      let plan_id = this.extractParamFromURL("id")
      this.fetchTestPlan(plan_id)
      document.title = this.state.testplan.title;
    }

    componentDidUpdate(prevProps, prevState) {
      let new_doc_title = this.state.testplan.plan_ident + ": " + this.state.testplan.title
      document.title = new_doc_title
    }

    extractParamFromURL(param) {
      const queryParameters = new URLSearchParams(window.location.search)
      const value = queryParameters.get(param)
      return value
    }

    fetchTestPlan(plan_id) {
        fetch('http://127.0.0.1:8000/api/testplan?id='+plan_id, {
                method: 'GET',
                credentials: 'include',
            })
            .then(response => response.json())
            .then(data => this.setState({ testplan: data.testplan }))
            .catch(error => console.error('Error: ', error));
    }

    render() {
        return (

            <Container>

                <div className='header'>
                  <p>{this.state.testplan.plan_ident}</p>
                  <h1 style={{'fontSize': '30px'}}>{this.state.testplan.title}</h1>
                </div>

                <div className='navigation'>
                  <Button href="/plans">〈 All plans</Button>
                  <span style={{flexGrow: '2'}}></span>
                  <Button variant='danger'>⌫ Delete suite</Button>
                  <Button variant='success'>+ Add suite</Button>
                </div>

                <div>
                  {this.state.testplan.testsuites.map((testsuite) => (
                        <TestSuiteBrief plan_id={this.state.testplan.plan_id} testsuite={testsuite} key={testsuite.suite_ident} />
                  ))}
                </div>

            </Container>
            
        )
    }
}

export default Plan;
