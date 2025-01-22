delimiter //
CREATE PROCEDURE cuenta_por_categoria (IN categoria_a_buscar CHAR(20), OUT cuantos INT)
BEGIN
    SELECT COUNT(*) INTO cuantos FROM lineapedido
    JOIN productos ON lineapedido.codProducto=productos.codProducto
    WHERE categoria = categoria_a_buscar;
END //
delimiter ;
