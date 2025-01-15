DELIMITER $$

CREATE TRIGGER actualizar_stock AFTER INSERT ON lineapedido
FOR EACH ROW
BEGIN
    -- Actualizar el stock del producto correspondiente
    UPDATE productos
    SET enAlmacen = enAlmacen - NEW.cantidad
    WHERE codProducto = NEW.codProducto;
END$$

DELIMITER ;

