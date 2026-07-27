class VehiculoPortuario {
    marca: string;
    
    constructor(marca: string) {
        this.marca = marca;
    }

    encender(): void {
        console.log(`El vehículo ${this.marca} está encendido.`);
    }
}

class Montacargas extends VehiculoPortuario {
    capacidadKg: number;

    constructor(marca: string, capacidadKg: number) {
        super(marca);
        this.capacidadKg = capacidadKg;
    }

    levantarPalet(): void {
        console.log(`Montacargas ${this.marca} levantando un palet de hasta ${this.capacidadKg} kg.`);
    }
}

const miMontacargas = new Montacargas("Toyota", 3500);
miMontacargas.encender();
miMontacargas.levantarPalet();
