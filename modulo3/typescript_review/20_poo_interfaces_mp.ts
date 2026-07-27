interface IRegistroAduanero {
    codigoDeclaracion: string;
    validarInspeccion(): boolean;
}

class CargaVehiculos implements IRegistroAduanero {
    codigoDeclaracion: string;
    numeroAutos: number;

    constructor(codigoDeclaracion: string, numeroAutos: number) {
        this.codigoDeclaracion = codigoDeclaracion;
        this.numeroAutos = numeroAutos;
    }

    validarInspeccion(): boolean {
        console.log(`Validando ${this.numeroAutos} autos con declaración ${this.codigoDeclaracion}`);
        return true;
    }
}

const importacionAutos = new CargaVehiculos("DECL-8899", 120);
importacionAutos.validarInspeccion();
