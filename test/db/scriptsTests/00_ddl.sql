--- Tablas para Testing
-- (debieron quitarse algunas caracteristicas como indexes, collation, etc)

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
`id` int NOT NULL,
`dni` int NOT NULL,
`legajo` varchar(10) NOT NULL,
PRIMARY KEY (`id`)
);


---Table usuario_carreras
DROP TABLE IF EXISTS `usuario_carreras`;

CREATE TABLE `usuario_carreras` (
`idUsuario` int NOT NULL,
`idCarrera` int NOT NULL
);


---Table usuario_mcursadas
DROP TABLE IF EXISTS `usuario_mcursadas`;
CREATE TABLE `usuario_mcursadas` (
`idUsuario` int NOT NULL,
`idMateria` int NOT NULL
);



---Table carrera
DROP TABLE IF EXISTS `carrera`;
CREATE TABLE `carrera` (
`id` int NOT NULL,
`nombre` varchar(255) NOT NULL,
`depto` varchar(255) NOT NULL,
PRIMARY KEY (`id`)
);



---Table carrera_materias
DROP TABLE IF EXISTS `carrera_materias`;
CREATE TABLE `carrera_materias` (
`idCarrera` int NOT NULL,
`idMateria` int NOT NULL,
PRIMARY KEY (`idCarrera`,`idMateria`)
);


---Table cursada
DROP TABLE IF EXISTS `cursada`;
CREATE TABLE `cursada` (
`id` int NOT NULL,
`idMateria` int NOT NULL,
`emailGrupo` varchar(255) NULL,
`horarios` varchar(255) NULL,
`docentes` varchar(255) NULL,
`periodo` varchar(20) NULL,
`activa` bit(1) DEFAULT NULL,
`aulas` varchar(255) DEFAULT NULL,
PRIMARY KEY (`id`)
);


---Table materia
DROP TABLE IF EXISTS `materia`;
CREATE TABLE `materia` (
`id` int NOT NULL,
`nombre` varchar(255) NOT NULL,
PRIMARY KEY (`id`)
);


---Table materias_correlativas
DROP TABLE IF EXISTS `materias_correlativas`;
CREATE TABLE `materias_correlativas` (
`idCarrera` int NOT NULL,
`idMateria` int NOT NULL,
`idCorrelativa` int NOT NULL
);