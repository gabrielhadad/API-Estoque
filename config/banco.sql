CREATE DATABASE IF NOT EXISTS estoque_ti
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE estoque_ti;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);

INSERT INTO produtos (nome, descricao, tipo, marca, quantidade, valor) VALUES
('Memória RAM 8GB DDR4', 'Memória DDR4 3200MHz para desktop', 'Memória', 'Kingston', 12, 149.90),
('SSD 480GB SATA', 'SSD SATA de 2.5 polegadas com 480GB', 'Armazenamento', 'Kingston', 8, 219.90),
('Cabo HDMI 2m', 'Cabo HDMI para conexão de monitores e TVs', 'Cabo', 'Elgin', 25, 29.90),
('Monitor 24 Polegadas', 'Monitor Full HD 24 polegadas com entrada HDMI', 'Monitor', 'LG', 5, 749.90),
('Teclado USB', 'Teclado padrão ABNT2 com conexão USB', 'Periférico', 'Logitech', 10, 89.90),
('Mouse USB', 'Mouse óptico com conexão USB', 'Periférico', 'Logitech', 15, 59.90),
('Fonte 500W', 'Fonte ATX 500W para computadores desktop', 'Fonte', 'Corsair', 6, 299.90),
('Placa de Vídeo RX 6600', 'Placa de vídeo com 8GB de memória GDDR6', 'Placa de Vídeo', 'ASRock', 3, 1299.90),
('Cabo de Rede Cat6 3m', 'Cabo de rede Ethernet categoria 6 com 3 metros', 'Cabo', 'Intelbras', 20, 24.90),
('Cooler para Processador', 'Cooler compatível com processadores Intel e AMD', 'Refrigeração', 'Cooler Master', 7, 119.90);
