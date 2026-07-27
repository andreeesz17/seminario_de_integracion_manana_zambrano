abstract class OperacionPortuaria {
    idOperacion: number;

    constructor(idOperacion: number) {
        this.idOperacion = idOperacion;
    }

    abstract ejecutar(): void;

    iniciarProtocoloSeguridad(): void {
        console.log(`Protocolo de seguridad iniciado para la operación ${this.idOperacion}`);
    }
}

class DescargaContenedores extends OperacionPortuaria {
    cantidad: number;

    constructor(idOperacion: number, cantidad: number) {
        super(idOperacion);
        this.cantidad = cantidad;
    }

    ejecutar(): void {
        console.log(`Iniciando descarga de ${this.cantidad} contenedores.`);
    }
}

const opDescarga = new DescargaContenedores(101, 45);
opDescarga.iniciarProtocoloSeguridad();
opDescarga.ejecutar();
