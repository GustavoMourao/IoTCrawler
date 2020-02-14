CREATE DATABASE IoTData;
\connect IoTData

CREATE TABLE IF NOT EXISTS "Cidades" (
  "Id"              SERIAL PRIMARY KEY,
  "Nome"            text,
  "Latitude"        real,
  "Longitude"       real
);

CREATE TABLE IF NOT EXISTS "Meteorologia" (
  "Id"              SERIAL PRIMARY KEY,
  "CidadeId"        bigint,
  "DataLeitura"     timestamp without time zone, 
  "Nebulosidade"    real,
  "Umidade"         real,
  "Pressao"         real,
  "Temperatura"     real,
  "Sensacao"        real,
  "DirecaoVento"    real,
  "VelocidadeVento" real,
  FOREIGN KEY ("CidadeId") REFERENCES "Cidades"("Id")
);
