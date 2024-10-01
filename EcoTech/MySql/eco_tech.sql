-- MySQL Script generated by MySQL Workbench
-- Tue Oct  1 15:51:17 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema EcoTech
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema EcoTech
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `EcoTech` DEFAULT CHARACTER SET utf8 ;
USE `EcoTech` ;

-- -----------------------------------------------------
-- Table `EcoTech`.`departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EcoTech`.`departamento` (
  `id_departamento` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL,
  `gerente` INT NOT NULL,
  PRIMARY KEY (`id_departamento`),
  INDEX `fk_departamento_empleado1_idx` (`gerente` ASC) VISIBLE,
  CONSTRAINT `fk_departamento_empleado1`
    FOREIGN KEY (`gerente`)
    REFERENCES `EcoTech`.`empleado` (`id_empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EcoTech`.`empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EcoTech`.`empleado` (
  `id_empleado` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL,
  `direccion` VARCHAR(100) NULL,
  `telefono` VARCHAR(15) NULL,
  `correo` VARCHAR(50) NULL,
  `inicio_contrato` DATE NULL,
  `salario` INT NULL,
  `departamento_id_departamento` INT NOT NULL,
  PRIMARY KEY (`id_empleado`),
  INDEX `fk_empleado_departamento1_idx` (`departamento_id_departamento` ASC) VISIBLE,
  CONSTRAINT `fk_empleado_departamento1`
    FOREIGN KEY (`departamento_id_departamento`)
    REFERENCES `EcoTech`.`departamento` (`id_departamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EcoTech`.`proyecto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EcoTech`.`proyecto` (
  `id_proyecto` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL,
  `descripcion` VARCHAR(200) NULL,
  `fecha_inicio` DATE NULL,
  PRIMARY KEY (`id_proyecto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EcoTech`.`registro_tiempo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EcoTech`.`registro_tiempo` (
  `id_registro_tiempo` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NULL,
  `cantidad_horas` INT NULL,
  `descripcion` VARCHAR(200) NULL,
  `empleado_id_empleado` INT NOT NULL,
  `proyecto_id_proyecto` INT NOT NULL,
  PRIMARY KEY (`id_registro_tiempo`),
  INDEX `fk_registro_tiempo_empleado1_idx` (`empleado_id_empleado` ASC) VISIBLE,
  INDEX `fk_registro_tiempo_proyecto1_idx` (`proyecto_id_proyecto` ASC) VISIBLE,
  CONSTRAINT `fk_registro_tiempo_empleado1`
    FOREIGN KEY (`empleado_id_empleado`)
    REFERENCES `EcoTech`.`empleado` (`id_empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_registro_tiempo_proyecto1`
    FOREIGN KEY (`proyecto_id_proyecto`)
    REFERENCES `EcoTech`.`proyecto` (`id_proyecto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EcoTech`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EcoTech`.`usuario` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL,
  `contraseña` VARCHAR(20) NULL,
  `permiso` VARCHAR(20) NULL,
  `id_empleado` INT NOT NULL,
  PRIMARY KEY (`id_usuario`),
  INDEX `fk_usuario_empleado1_idx` (`id_empleado` ASC) VISIBLE,
  CONSTRAINT `fk_usuario_empleado1`
    FOREIGN KEY (`id_empleado`)
    REFERENCES `EcoTech`.`empleado` (`id_empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EcoTech`.`proyecto_empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `EcoTech`.`proyecto_empleado` (
  `id_proyecto` INT NOT NULL,
  `id_empleado` INT NOT NULL,
  PRIMARY KEY (`id_proyecto`, `id_empleado`),
  INDEX `fk_proyecto_has_empleado_empleado1_idx` (`id_empleado` ASC) VISIBLE,
  INDEX `fk_proyecto_has_empleado_proyecto1_idx` (`id_proyecto` ASC) VISIBLE,
  CONSTRAINT `fk_proyecto_has_empleado_proyecto1`
    FOREIGN KEY (`id_proyecto`)
    REFERENCES `EcoTech`.`proyecto` (`id_proyecto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_proyecto_has_empleado_empleado1`
    FOREIGN KEY (`id_empleado`)
    REFERENCES `EcoTech`.`empleado` (`id_empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
