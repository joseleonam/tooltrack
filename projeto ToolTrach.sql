-- CRIAÇÃO DAS TABELAS

CREATE TABLE Usuario (
    id_usuario INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    tipo VARCHAR(50)
);

CREATE TABLE Ferramenta (
    id_ferramenta INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    categoria VARCHAR(50),
    status VARCHAR(20)
);

CREATE TABLE Emprestimo (
    id_emprestimo INT PRIMARY KEY,
    id_usuario INT REFERENCES Usuario(id_usuario),
    data_emprestimo DATE,
    data_prevista_devolucao DATE,
    data_devolucao DATE
);

CREATE TABLE ItemEmprestado (
    id_emprestimo INT REFERENCES Emprestimo(id_emprestimo),
    id_ferramenta INT REFERENCES Ferramenta(id_ferramenta),
    quantidade INT,
    PRIMARY KEY (id_emprestimo, id_ferramenta)
);

CREATE TABLE Manutencao (
    id_manutencao INT PRIMARY KEY,
    id_ferramenta INT REFERENCES Ferramenta(id_ferramenta),
    tipo VARCHAR(50),
    data_manutencao DATE,
    descricao TEXT
);

CREATE TABLE Localizacao (
    id_ferramenta INT PRIMARY KEY REFERENCES Ferramenta(id_ferramenta),
    sala VARCHAR(20),
    armario VARCHAR(20),
    prateleira VARCHAR(20)
);

-- INSERSÃO DE DADOS

INSERT INTO Usuario VALUES
(1, 'Ana Silva', 'ana.silva@email.com', 'aluno'),
(2, 'Carlos Souza', 'carlos.souza@email.com', 'tecnico'),
(3, 'Mariana Lima', 'mariana.lima@email.com', 'professor'),
(4, 'João Mendes', 'joao.mendes@email.com', 'aluno'),
(5, 'Fernanda Alves', 'fernanda.alves@email.com', 'tecnico'),
(6, 'Lucas Pereira', 'lucas.pereira@email.com', 'aluno'),
(7, 'Rafael Costa', 'rafael.costa@email.com', 'professor'),
(8, 'Patricia Gomes', 'patricia.gomes@email.com', 'aluno'),
(9, 'Juliana Rocha', 'juliana.rocha@email.com', 'tecnico'),
(10, 'Thiago Martins', 'thiago.martins@email.com', 'aluno');

INSERT INTO Ferramenta VALUES
(1, 'Furadeira', 'Furadeira de impacto', 'Elétrica', 'disponível'),
(2, 'Martelo', 'Martelo de aço', 'Manual', 'disponível'),
(3, 'Alicate', 'Alicate universal', 'Manual', 'manutenção'),
(4, 'Parafusadeira', 'Parafusadeira elétrica', 'Elétrica', 'emprestada'),
(5, 'Multímetro', 'Multímetro digital', 'Medição', 'disponível'),
(6, 'Serra Tico-Tico', 'Serra elétrica', 'Elétrica', 'disponível'),
(7, 'Chave de Fenda', 'Chave fenda média', 'Manual', 'disponível'),
(8, 'Trena', 'Trena 5m', 'Medição', 'disponível'),
(9, 'Lixadeira', 'Lixadeira orbital', 'Elétrica', 'disponível'),
(10, 'Broca', 'Broca 8mm aço rápido', 'Acessório', 'disponível');

INSERT INTO Emprestimo VALUES
(1, 1, '2025-06-01', '2025-06-10', '2025-06-09'),
(2, 2, '2025-06-02', '2025-06-11', '2025-06-10'),
(3, 3, '2025-06-03', '2025-06-12', '2025-06-12'),
(4, 4, '2025-06-04', '2025-06-13', '2025-06-12'),
(5, 5, '2025-06-05', '2025-06-14', NULL),
(6, 6, '2025-06-06', '2025-06-15', NULL),
(7, 7, '2025-06-07', '2025-06-16', '2025-06-15'),
(8, 8, '2025-06-08', '2025-06-17', '2025-06-16'),
(9, 9, '2025-06-09', '2025-06-18', NULL),
(10, 10, '2025-06-10', '2025-06-19', NULL);

INSERT INTO ItemEmprestado VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 1),
(4, 4, 1),
(5, 5, 3),
(6, 6, 1),
(7, 7, 2),
(8, 8, 1),
(9, 9, 1),
(10, 10, 2);

INSERT INTO Manutencao VALUES
(1, 3, 'corretiva', '2025-06-05', 'Troca de mola'),
(2, 6, 'preventiva', '2025-06-06', 'Lubrificação geral'),
(3, 4, 'corretiva', '2025-06-07', 'Substituição do motor'),
(4, 2, 'preventiva', '2025-06-08', 'Inspeção de cabo'),
(5, 5, 'preventiva', '2025-06-09', 'Verificação de bateria'),
(6, 8, 'preventiva', '2025-06-10', 'Calibração'),
(7, 9, 'corretiva', '2025-06-11', 'Troca de disco'),
(8, 10, 'preventiva', '2025-06-12', 'Inspeção de corte'),
(9, 1, 'corretiva', '2025-06-13', 'Reposição de peças'),
(10, 7, 'preventiva', '2025-06-14', 'Ajuste de ponta');

INSERT INTO Localizacao VALUES
(1, 'Lab A', 'Armário 1', 'Prateleira 2'),
(2, 'Lab A', 'Armário 2', 'Prateleira 1'),
(3, 'Lab A', 'Armário 3', 'Prateleira 2'),
(4, 'Lab A', 'Armário 1', 'Prateleira 3'),
(5, 'Lab B', 'Armário 2', 'Prateleira 2'),
(6, 'Lab B', 'Armário 3', 'Prateleira 1'),
(7, 'Lab B', 'Armário 1', 'Prateleira 1'),
(8, 'Lab B', 'Armário 2', 'Prateleira 3'),
(9, 'Lab B', 'Armário 3', 'Prateleira 3'),
(10, 'Lab A', 'Armário 1', 'Prateleira 4');

-- CONSULTAS SQL

-- 1. Listar todas as ferramentas atualmente emprestadas e quem pegou
SELECT f.id_ferramenta, f.nome AS nome_ferramenta, u.nome AS nome_usuario, e.data_emprestimo
FROM Ferramenta f
JOIN ItemEmprestado ie ON f.id_ferramenta = ie.id_ferramenta
JOIN Emprestimo e ON ie.id_emprestimo = e.id_emprestimo
JOIN Usuario u ON e.id_usuario = u.id_usuario;

-- 2. Mostrar o histórico de manutenções de cada ferramenta
SELECT f.nome, m.tipo AS tipo_manutencao, m.data_manutencao, m.descricao
FROM Ferramenta f
JOIN Manutencao m ON f.id_ferramenta = m.id_ferramenta;

-- 3. Localização atual de todas as ferramentas
SELECT f.nome, l.sala, l.armario, l.prateleira
FROM Ferramenta f
JOIN Localizacao l ON f.id_ferramenta = l.id_ferramenta;

-- 4. Usuários que mais realizaram empréstimos (TOP 3)
SELECT u.nome, COUNT(e.id_emprestimo) AS total_emprestimos
FROM Usuario u
JOIN Emprestimo e ON u.id_usuario = e.id_usuario
GROUP BY u.nome
ORDER BY total_emprestimos DESC
--LIMIT 3; -- da erro no vscode

-- 5. Ferramentas emprestadas que ainda não foram devolvidas
SELECT f.id_ferramenta, f.nome AS ferramenta, e.data_prevista_devolucao, u.nome AS usuario
FROM Ferramenta f
JOIN ItemEmprestado ie ON f.id_ferramenta = ie.id_ferramenta
JOIN Emprestimo e ON e.id_emprestimo = ie.id_emprestimo
JOIN Usuario u ON e.id_usuario = u.id_usuario
WHERE e.data_devolucao IS NULL;
