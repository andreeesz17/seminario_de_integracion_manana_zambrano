type ManifiestoCarga = {
    idRegistro: number;
    origen: string;
    pesoTotal: number;
    esPeligrosa: boolean;
};

const manifiesto: ManifiestoCarga = {
    idRegistro: 10459,
    origen: "Shanghái",
    pesoTotal: 8500.5,
    esPeligrosa: true
};

console.log(manifiesto);
