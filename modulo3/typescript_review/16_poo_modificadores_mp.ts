class EmpleadoPuerto {
    public nombre: string;
    private idCredencial: string;

    constructor(nombre: string, idCredencial: string) {
        this.nombre = nombre;
        this.idCredencial = idCredencial;
    }

    public mostrarIdentificacion(): void {
        console.log(`Empleado: ${this.nombre}, Credencial terminación: ***${this.idCredencial.slice(-2)}`);
    }

    private verificarAccesoRestringido(): boolean {
        return this.idCredencial.startsWith("ADMIN");
    }
}

const guarda = new EmpleadoPuerto("Jorge", "EMP-9021");
guarda.mostrarIdentificacion();
