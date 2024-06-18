-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-06-2024 a las 22:51:23
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mundo_deporte`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id`, `nombre`) VALUES
(1, 'voley'),
(2, 'Pelotas'),
(3, 'Rodilleras'),
(4, 'Botines'),
(5, 'Camisetas'),
(6, 'Pantalones Cortos'),
(7, 'Calcetines'),
(8, 'Guantes'),
(9, 'Gorras'),
(10, 'Mochilas'),
(11, 'Cascos'),
(12, 'Protecciones'),
(13, 'Raquetas'),
(14, 'Bicicletas'),
(15, 'Chanclas'),
(16, 'Chalecos Salvavidas'),
(17, 'Toallas'),
(18, 'Botellas de Agua'),
(19, 'Pesas'),
(20, 'Barras de Ejercicio'),
(21, 'Colchonetas de Yoga'),
(22, 'Voley'),
(23, 'Fútbol'),
(24, 'Baloncesto'),
(25, 'Tenis'),
(26, 'Ciclismo'),
(27, 'Natación'),
(28, 'Atletismo'),
(29, 'Golf'),
(30, 'Béisbol'),
(31, 'Rugby'),
(32, 'Críquet'),
(33, 'Boxeo'),
(34, 'Artes Marciales'),
(35, 'Levantamiento de Pesas'),
(36, 'Escalada'),
(37, 'Deportes de Invierno'),
(38, 'Skateboarding'),
(39, 'Surf'),
(40, 'Equitación'),
(41, 'Senderismo'),
(42, 'Caza y Pesca');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `cat_id` int(11) DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `cat_id`, `nombre`, `descripcion`, `imagen`, `precio`, `stock`) VALUES
(1, 1, 'pelota', 'de voley', 'pelota.jpg', 15000, 1000),
(6, 1, 'Pelota de Voleibol', 'Pelota oficial de voleibol de tamaño estándar', 'pelota_voleibol.jpg', 25, 100),
(7, 2, 'Pelota de Fútbol', 'Pelota oficial de fútbol de tamaño estándar', 'pelota_futbol.jpg', 30, 100),
(8, 3, 'Rodilleras de Voleibol', 'Rodilleras acolchadas para protección en el voleibol', 'rodilleras_voleibol.jpg', 16, 150),
(9, 4, 'Botines de Fútbol', 'Botines con tacos para un mejor agarre en el campo', 'botines_futbol.jpg', 50, 75),
(10, 5, 'Camiseta de Tenis', 'Camiseta ligera y transpirable para tenis', 'camiseta_tenis.jpg', 20, 200),
(11, 6, 'Pantalones Cortos de Ciclismo', 'Pantalones cortos acolchados para ciclismo', 'pantalones_ciclismo.jpg', 35, 50),
(12, 7, 'Calcetines de Natación', 'Calcetines antideslizantes para natación', 'calcetines_natacion.jpg', 10, 300),
(13, 8, 'Guantes de Golf', 'Guantes de golf para un mejor agarre', 'guantes_golf.jpg', 25, 120),
(14, 9, 'Gorra de Béisbol', 'Gorra ajustable para béisbol', 'gorra_beisbol.jpg', 13, 180),
(15, 10, 'Mochila Deportiva', 'Mochila espaciosa y resistente para deportes', 'mochila_deportiva.jpg', 40, 60),
(16, 11, 'Casco de Rugby', 'Casco de protección para rugby', 'casco_rugby.jpg', 30, 80),
(17, 12, 'Protección de Críquet', 'Equipamiento de protección para críquet', 'proteccion_criquet.jpg', 46, 40),
(18, 13, 'Raqueta de Tenis', 'Raqueta ligera y resistente para tenis', 'raqueta_tenis.jpg', 80, 120),
(19, 14, 'Bicicleta de Montaña', 'Bicicleta resistente para terrenos difíciles', 'bicicleta_montana.jpg', 500, 30),
(20, 15, 'Chanclas de Natación', 'Chanclas antideslizantes para piscina', 'chanclas_natacion.jpg', 15, 200),
(22, 17, 'Toalla Deportiva', 'Toalla absorbente y ligera para deportes', 'toalla_deportiva.jpg', 20, 150),
(23, 18, 'Botella de Agua Deportiva', 'Botella reutilizable para hidratación', 'botella_agua.jpg', 10, 300),
(24, 19, 'Pesas de Entrenamiento', 'Pesas ajustables para entrenamiento', 'pesas_entrenamiento.jpg', 80, 70),
(25, 20, 'Barra de Ejercicio', 'Barra resistente para ejercicios de fuerza', 'barra_ejercicio.jpg', 90, 50),
(26, 21, 'Colchoneta de Yoga', 'Colchoneta antideslizante para yoga', 'colchoneta_yoga.jpg', 30, 200),
(27, 22, 'Red de Voleibol', 'Red oficial para canchas de voleibol', 'red_voleibol.jpg', 150, 20),
(28, 23, 'Balón de Fútbol', 'Balón de fútbol de entrenamiento', 'balon_futbol.jpg', 20, 150),
(29, 24, 'Zapatillas de Baloncesto', 'Zapatillas con buen agarre para baloncesto', 'zapatillas_baloncesto.jpg', 100, 100),
(30, 25, 'Raqueta de Tenis', 'Raqueta profesional para tenis', 'raqueta_profesional_tenis.jpg', 90, 50),
(31, 26, 'Casco de Ciclismo', 'Casco aerodinámico para ciclismo', 'casco_ciclismo.jpg', 60, 150),
(32, 27, 'Gafas de Natación', 'Gafas con protección UV para natación', 'gafas_natacion.jpg', 15, 250),
(33, 28, 'Zapatos de Atletismo', 'Zapatos ligeros para correr en pista', 'zapatos_atletismo.jpg', 75, 100),
(34, 29, 'Pelotas de Golf', 'Pelotas de golf de alta calidad', 'pelotas_golf.jpg', 30, 300),
(35, 30, 'Guante de Béisbol', 'Guante de cuero para béisbol', 'guante_beisbol.jpg', 50, 80),
(36, 31, 'Zapatos de Rugby', 'Zapatos con tacos para rugby', 'zapatos_rugby.jpg', 70, 90),
(37, 32, 'Bate de Críquet', 'Bate de críquet de madera', 'bate_criquet.jpg', 60, 70),
(38, 33, 'Saco de Boxeo', 'Saco de boxeo resistente', 'saco_boxeo.jpg', 90, 50),
(39, 34, 'Cinturón de Artes Marciales', 'Cinturón de diferentes grados para artes marciales', 'cinturon_artes_marciales.jpg', 10, 200),
(40, 35, 'Mancuernas', 'Set de mancuernas ajustables', 'mancuernas.jpg', 50, 100),
(41, 36, 'Mosquetón de Escalada', 'Mosquetón seguro para escalada', 'mosqueton_escalada.jpg', 15, 250),
(42, 37, 'Guantes de Snowboard', 'Guantes térmicos para snowboard', 'guantes_snowboard.jpg', 25, 150),
(43, 38, 'Casco de Skateboarding', 'Casco protector para skateboarding', 'casco_skateboarding.jpg', 40, 120),
(44, 39, 'Tabla de Surf', 'Tabla de surf resistente y ligera', 'tabla_surf.jpg', 200, 40),
(45, 40, 'Botas de Equitación', 'Botas duraderas para equitación', 'botas_equitacion.jpg', 100, 60),
(46, 41, 'Botas de Senderismo', 'Botas duraderas y cómodas para senderismo', 'botas_senderismo.jpg', 100, 80),
(47, 42, 'Caña de Pescar', 'Caña de pescar telescópica', 'cana_pescar.jpg', 60, 100);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `admin` tinyint(1) DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `contasenia` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `admin`, `nombre`, `email`, `contasenia`) VALUES
(1, 1, 'admin', 'admin@mail.com', 'admin1234');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `productos_ibfk_1` (`cat_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`cat_id`) REFERENCES `categorias` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
