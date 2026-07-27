type TipoCarga = "PELIGROSA" | "REFRIGERADA" | "GENERAL";

function procesarCarga(tipo: TipoCarga) {
    if (tipo === "PELIGROSA") {
        console.log("Precaución: Manejo especial requerido.");
    } else {
        console.log(`Procesando carga de tipo: ${tipo}`);
    }
}

procesarCarga("REFRIGERADA");
