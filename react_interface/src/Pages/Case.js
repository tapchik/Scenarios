import React from 'react';

import 'bootstrap/dist/css/bootstrap.css';
import Container from 'react-bootstrap/Container';

class Case extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            testcase: {},
        }
    }

    render() {
        return (

            <Container>

                <div className='header'>
                  <p>This is a case</p>
                  <h1>Placeholder for test case</h1>
                </div>

            </Container>
            
        )
    }
}

export default Case;
