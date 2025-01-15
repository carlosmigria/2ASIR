DELIMITER $$

CREATE TRIGGER actualizar_importe_pedido AFTER INSERT ON lineapedido
FOR EACH ROW
BEGIN
    DECLARE nuevo_importe DECIMAL(10,2);

    -- Calcular el importe de la nueva línea de pedido
    SET nuevo_importe = NEW.cantidad * NEW.precio;

    -- Actualizar el importe total del pedido correspondiente
    UPDATE pedidos
    SET importeTotal = IFNULL(importeTotal, 0) + nuevo_importe
    WHERE numeroPedido = NEW.numeroPedido;
END$$

DELIMITER ;

