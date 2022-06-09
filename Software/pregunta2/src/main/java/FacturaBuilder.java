public class FacturaBuilder {
    private String country = "NL";
    private CustomerType customerType = CustomerType.PERSON;
    private double value = 500;

    public FacturaBuilder withCountry(String country) {
        this.country = country;
        return this;
    }

    public FacturaBuilder asCompany() {
        this.customerType = CustomerType.COMPANY;
        return this;
    }

    public FacturaBuilder withAValueOf(double value) {
        this.value = value;
        return this;
    }

    public Factura build() {
        return new Factura(value, country, customerType);
    }

    public Factura anyCompany() {
        return new Factura (value, country, CustomerType.COMPANY);
    }

    public Factura fromTheUS() {
        return new Factura(value,"US", customerType);
    }
}
