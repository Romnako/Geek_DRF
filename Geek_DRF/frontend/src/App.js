import React from 'react';
import './App.css';
import axios from 'axios';
import AuthorList from './components/Author.js';
import MainMenu from './components/Menu.js';
import Footer from './components/Footer.js';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': []
    }
  }

//  componentDidMount() {
//  const authors = [
//        {
//            'first_name': 'Genry',
//            'last_name': 'Ford',
//            'birthday_year': '1863',
//            'email': '@Genry',
//        },
//        {
//            'first_name': 'Enzo',
//            'last_name': 'Ferrari',
//            'birthday_year': '1898',
//            'email': '@Enzo',
//        },
//    ]
//     this.setState(
//            {
//            'authors': authors
//        }
//     )
//  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/authors')
      .then(response => {
        const authors = response.data
        this.setState(
          {
            'authors': authors
          }
        )
      }).catch(error => console.log(error))
  }
  render() {
    return (
      <body>
        <nav>
          <MainMenu />
        </nav>
        <div>
          <AuthorList authors={this.state.authors} />
        </div>
        <footer>
          <Footer />
        </footer>
      </body>
    )
  }


}

export default App;