import React from 'react';
import './App.css';
import axios from 'axios';
import AuthorList from './components/Author.js';
import MainMenu from './components/Menu.js';
import Footer from './components/Footer.js';
import { BrowserRouter as Router, Route, Routes< Navigate, Link, Switch } from 'react-router-dom'
import ToDoList from './components/ToDo';
import ProjectList from '/components/Project';
import BookList from '/components/Book';


const NotFound404 = ({ location }) => {
    return(
        <div>
            <hi>Page not found from address '{location.pathname}'</hi>
        </div>
    )
}


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': [],
      'books' : [],
      'todos': [],
      'projects': []
    }
  }


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
    axios.get('http://127.0.0.1:8000/api/todos')
      .then(response => {
        const todos = response.data.results
        this.setState(
          {
            'todos': todos
          }
        )
      }).catch(error => console.log(error))
  }
  render() {
    return (
      <div className="App">
        <Router>
          <div>
            <nav>
              <ul>
                  <li>
                    <Link to='/author'>Authors</Link>
                  </li>
                  <li>
                    <Link to='/book'>Books</Link>
                  </li>
              </ul>
            </nav>
            <Switch>
                <Routes>
                  <Route path='/authors' element={<UserList authors={this.state.authors} />} />
                  <Route path='/books' element={<BookList books={this.state.books} />} />
                  <Route path='/todos' element={<ToDoList todos={this.state.todos} />} />
                  <Route path='/projects' element={<ProjectList projects={this.state.projects} />} />
                  <Route path='/' element={<Navigate replace to="/authors" />} />
                  <Route component={NotFound404} />
                </Routes>
            </Switch>
          </div>
          <footer>
            <Footer />
          </footer>
        </Router>
      </div>
    )
  }


}

export default App;
