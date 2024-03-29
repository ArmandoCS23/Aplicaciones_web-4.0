DROP TABLE IF EXISTS productos;

CREATE TABLE IF NOT EXISTS productos (
    id_productos INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT NOT NULL,
    imagen BLOB NOT NULL,
    extension VARCHAR(10) NOT NULL,
    precio REAL NOT NULL CHECK (precio >= 0), 
    existencias INTEGER NOT NULL CHECK (existencias >= 0) 
);

