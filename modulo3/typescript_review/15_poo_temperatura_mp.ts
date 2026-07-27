class ContenedorRefrigerado {
    private temperaturaActual: number;

    constructor(temperaturaInicial: number) {
        this.temperaturaActual = temperaturaInicial;
    }

    ajustarTemperatura(nuevaTemp: number): void {
        this.temperaturaActual = nuevaTemp;
        console.log(`Temperatura ajustada a ${this.temperaturaActual}°C`);
    }

    obtenerTemperatura(): number {
        return this.temperaturaActual;
    }
}

const contenedorCarne = new ContenedorRefrigerado(-10);
contenedorCarne.ajustarTemperatura(-15);
