import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;

import static org.junit.jupiter.api.Assertions.assertEquals;

class FacturaTest {

    @DisplayName("Probando calculate")
    @Test
    public void testCalculate(){
        // Prueba que crea una factura con un value fijo y verifica si el valor entregado por
        // calculate() es el esperado (esto se verifica usando el asserEquals)

        Factura factura = new Factura(0.834334, "NY", CustomerType.PERSON);
        assertEquals(0.834334*0.1, factura.calculate());
    }
}