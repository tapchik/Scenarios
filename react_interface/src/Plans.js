import React from 'react';
//import logo from './logo.svg';
//import './App.css';

function Ttt() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          List of plans. 
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

class Plans extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            plans: [],
            testsuites: [],
        }
    }

    componentDidMount() {
        this.refreshListOfProducts();
    }

    refreshListOfProducts() {
        fetch('http://localhost:8000/api/testplan?id=1', {
                method: 'GET',
                credentials: 'include',
            })
            .then(response => response.json())
            .then(data => this.setState({ testsuites: data.testplan.testsuites }))
            .catch(error => console.error('Error: ', error));
    }

    render() {
        return (
            <div>
                <h1>Hello World!</h1>
                <p>{this.state.plans}</p>
                    
                <div className='list-of-products-container'>
                {this.state.testsuites.map((suite) => (
                    <div>
                        <a>{suite.suite_ident}</a>
                    </div>
                ))}
                </div>
            </div>
            
        )
    }
}

export default Plans;
