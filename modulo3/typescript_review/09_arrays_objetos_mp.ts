type Contenedor = {
    codigo: string;
    pesoKg: number;
    destino: string;
};

let patioContenedores: Contenedor[] = [
    { codigo: "C-001", pesoKg: 2500, destino: "Bodega A" },
    { codigo: "C-002", pesoKg: 3100, destino: "Bodega B" },
    { codigo: "C-003", pesoKg: 1800, destino: "Tren de Carga" }
];

console.log(patioContenedores[1].destino);
