
---Table usuario
DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dni` int NOT NULL,
  `legajo` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;


---Table usuario_carreras
DROP TABLE IF EXISTS `usuario_carreras`;

CREATE TABLE `usuario_carreras` (
  `idUsuario` int NOT NULL,
  `idCarrera` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


---Table usuario_mcursadas
DROP TABLE IF EXISTS `usuario_mcursadas`;
CREATE TABLE `usuario_mcursadas` (
  `idUsuario` int NOT NULL,
  `idMateria` int NOT NULL,
  `notaFinal` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



---Table carrera
DROP TABLE IF EXISTS `carrera`;
CREATE TABLE `carrera` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE latin1_spanish_ci NOT NULL,
  `depto` varchar(255) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_carrera_nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;



---Table carrera_materias
DROP TABLE IF EXISTS `carrera_materias`;
CREATE TABLE `carrera_materias` (
  `idCarrera` int NOT NULL,
  `idMateria` int NOT NULL,
  PRIMARY KEY (`idCarrera`,`idMateria`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


---Table cursada
DROP TABLE IF EXISTS `cursada`;
CREATE TABLE `cursada` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idMateria` int NOT NULL,
  `emailGrupo` varchar(255) CHARACTER SET latin1 COLLATE latin1_spanish_ci DEFAULT NULL,
  `horarios` varchar(255) CHARACTER SET latin1 COLLATE latin1_spanish_ci DEFAULT NULL,
  `docentes` varchar(255) CHARACTER SET latin1 COLLATE latin1_spanish_ci DEFAULT NULL,
  `periodo` varchar(20) CHARACTER SET latin1 COLLATE latin1_spanish_ci DEFAULT NULL,
  `activa` bit(1) DEFAULT NULL,
  `aulas` varchar(255) COLLATE latin1_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_cursada_idMateria` (`idMateria`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;


---Table materia
DROP TABLE IF EXISTS `materia`;
CREATE TABLE `materia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_materia_nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;


---Table materias_correlativas
DROP TABLE IF EXISTS `materias_correlativas`;
CREATE TABLE `materias_correlativas` (
  `idCarrera` int NOT NULL,
  `idMateria` int NOT NULL,
  `idCorrelativa` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
