import React from 'react';

import 'bootstrap/dist/css/bootstrap.css';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import TestCaseBrief from '../elements/TestCaseBreif';

class Suite extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            testplan: {},
            testsuite: {
                title: "",
                suite_ident: 'None',
                title: 'Empty',
                testcases: [],
            },
        }
    }

    componentDidMount() {
        let suite_id = this.extractParamFromURL('id')
        let ver = this.extractParamFromURL('ver')
        document.title = this.state.testplan.title
        this.fetchTestSuite(suite_id, ver)
    }

    extractParamFromURL(param) {
        const queryParameters = new URLSearchParams(window.location.search)
        const value = queryParameters.get(param)
        return value
    }

    fetchTestSuite(suite_id, ver) {
        fetch('http://127.0.0.1:8000/api/testsuite?id='+suite_id+'&ver='+ver, {
                method: 'GET',
                credentials: 'include',
            })
            .then(response => response.json())
            .then(data => this.setState({ testsuite: data.testsuite }))
            .catch(error => console.error('Error: ', error));
    }

    render() {
        return (

            <Container>

                <h1>{this.state.testsuite.suite_ident}: {this.state.testsuite.title}</h1>

                <div>
                  {this.state.testsuite.testcases.map((testcase) => (
                        <TestCaseBrief parent_suite_id={this.state.testsuite.suite_id} testcase={testcase} key={testcase.step} />
                  ))}
                </div>

            </Container>
            
        )
    }
}

export default Suite;
