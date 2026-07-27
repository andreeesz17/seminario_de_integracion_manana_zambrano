let barcosEnEspera: string[] = ["Nautilus", "Estrella del Sur", "Poseidón", "Mermaid"];
barcosEnEspera.push("Valiente");

barcosEnEspera.forEach((barco, index) => {
    console.log(`Turno ${index + 1}: Buque ${barco}`);
});
