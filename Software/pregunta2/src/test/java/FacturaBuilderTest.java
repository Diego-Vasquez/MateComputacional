import org.junit.jupiter.api.Test;

import javax.print.DocFlavor;

import static org.junit.jupiter.api.Assertions.*;

class FacturaBuilderTest {

    @Test
    void calculeOfBuilder() {

        // creamos las dos variables a utilizar para crear el builder
        double facturaValue = 1.232;
        double tax=0.1;
        String country = "NY";

        // creamos el builder con las variables anteriores seteadas
        // adicionalmente lo seteamos como compañia y
        // finalmente generamos una factura con
        // esta informacion.
        Factura factura = new FacturaBuilder()
                .asCompany() // se setea el builder como compañia
                .withCountry(country) // se setea la ciudad
                .withAValueOf(facturaValue) // se setea el valor
                .build(); // finalmente se instancia una factura con los datos ingresados

        // luego hacemos el calculo con calculate() de la factura
        double calculatedValue = factura.calculate();

        // finalmente verificamos que el calculo hecho por nosotros y la clase
        // sean identifcos, caso contrario el test fallará.
        double valor_esperado =facturaValue * tax;
        assertEquals(calculatedValue, valor_esperado);
    }
}