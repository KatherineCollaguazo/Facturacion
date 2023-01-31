package facturacion.bffweb.customer;

import java.sql.Date;

import lombok.Data;

@Data
public class CustomerDTO {
    
    private Long id;
    private String razon_social;
    private String nro_identificacion;
    private Date fecha_nacimiento;
    private double monto_primera_compra;
    private String email;
    private String phone;
    private Long tipo;
}
