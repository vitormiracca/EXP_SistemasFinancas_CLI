CREATE TABLE Contas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) NOT NULL
);

CREATE TABLE Categorias (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(255) NOT NULL,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE Lancamentos (
    id SERIAL PRIMARY KEY,
    data_lancamento DATE NOT NULL,
    tipo_lancamento VARCHAR(255) NOT NULL,
    conta_id INT NOT NULL,
    categoria_id INT NOT NULL,
    valor NUMERIC(10, 2) NOT NULL,
    descricao TEXT,
    CONSTRAINT fk_conta
      FOREIGN KEY(conta_id) 
	    REFERENCES Contas(id),
    CONSTRAINT fk_categoria
      FOREIGN KEY(categoria_id) 
	    REFERENCES Categorias(id)
);