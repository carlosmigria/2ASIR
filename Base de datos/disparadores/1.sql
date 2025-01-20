DELIMITER $$

CREATE TRIGGER verificar_stock BEFORE INSERT ON lineapedido
FOR EACH ROW
BEGIN
    DECLARE stock_disponible SMALLINT;

    -- Obtener el stock disponible del producto
    SELECT enAlmacen INTO stock_disponible
    FROM productos
    WHERE codProducto = NEW.codProducto;

    -- Verificar si la cantidad a vender supera el stock disponible
    IF NEW.cantidad > stock_disponible THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: La cantidad solicitada supera el stock disponible.';
    END IF;
END$$

DELIMITER ;

