class Barco {
    nombre: string;
    capacidadToneladas: number;

    constructor(nombre: string, capacidadToneladas: number) {
        this.nombre = nombre;
        this.capacidadToneladas = capacidadToneladas;
    }

    anunciarLlegada(): void {
        console.log(`El barco ${this.nombre} ha llegado con capacidad de ${this.capacidadToneladas} toneladas.`);
    }
}

const miBarco = new Barco("Perla Negra", 5000);
miBarco.anunciarLlegada();
