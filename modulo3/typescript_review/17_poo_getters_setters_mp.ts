class GruaPortuaria {
    private _capacidadLevantamiento: number = 0;

    get capacidad(): number {
        return this._capacidadLevantamiento;
    }

    set capacidad(valor: number) {
        if (valor > 100) {
            console.log("Error: La grúa no puede levantar más de 100 toneladas.");
            return;
        }
        this._capacidadLevantamiento = valor;
    }
}

const grua1 = new GruaPortuaria();
grua1.capacidad = 150;
grua1.capacidad = 80;
console.log(`Capacidad actual: ${grua1.capacidad} toneladas.`);
