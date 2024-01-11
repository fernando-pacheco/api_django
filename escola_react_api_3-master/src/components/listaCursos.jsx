import React, { Component } from 'react';

class ListaCursos extends Component {
  state = {
    data: [],
    loaded: false
  };

  componentDidMount() {
    fetch("http://localhost:8000/cursos/")
      .then(response => {
        if (response.status > 400) {
          // Código do comportamento em caso de problema na req
        }
        return response.json();
      })
      .then(data => {
        this.setState({ data, loaded: true });
      })
      .catch(error => {
        console.error('Erro ao carregar dados:', error);
      });
  }

  render() {
    const { data, loaded } = this.state;

    if (!loaded) {
      return <p>Carregando...</p>;
    }

    return (
      <div>
        {data.map(curso => (
          <h2 key={curso.id} className='App-table'>
            {curso.descricao}
          </h2>
        ))}
      </div>
    );
  }
}

export default ListaCursos;
