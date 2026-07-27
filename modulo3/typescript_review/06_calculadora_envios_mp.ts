function calcularTarifaPortuaria(toneladas: number, tarifaPorTonelada: number): number {
    return toneladas * tarifaPorTonelada;
}

const totalAPagar = calcularTarifaPortuaria(500, 15.5);
console.log(`El total a pagar por uso de puerto es: $${totalAPagar}`);
