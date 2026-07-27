enum EstadoBarco {
    EN_ESPERA,
    ATRACADO,
    DESCARGANDO,
    ZARPADO
}

let estadoActual: EstadoBarco = EstadoBarco.ATRACADO;

if (estadoActual === EstadoBarco.ATRACADO) {
    console.log("El barco está listo para descargar.");
}
