class TrabajadorPuerto {
    nombre: string;

    constructor(nombre: string) {
        this.nombre = nombre;
    }

    realizarTarea(): void {
        console.log(`${this.nombre} está realizando una tarea general en el puerto.`);
    }
}

class Estibador extends TrabajadorPuerto {
    realizarTarea(): void {
        console.log(`${this.nombre} está asegurando la carga en el buque.`);
    }
}

class ControladorTrafico extends TrabajadorPuerto {
    realizarTarea(): void {
        console.log(`${this.nombre} está autorizando la entrada de un barco al canal.`);
    }
}

function iniciarJornada(trabajadores: TrabajadorPuerto[]) {
    trabajadores.forEach(t => t.realizarTarea());
}

const equipo: TrabajadorPuerto[] = [
    new Estibador("Carlos"),
    new ControladorTrafico("Ana")
];

iniciarJornada(equipo);
