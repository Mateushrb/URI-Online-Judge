const C = parseInt(lines.shift());
const T = String(lines.shift());

let matriz = Array();
let linha = Array();

for (let i = 0; i<12; i++) {
    for (let l = 0; l<12; l++) {
        let elemento = parseFloat(lines.shift());
        linha.push(elemento);
    }
    matriz.push(linha);
    linha = [];
}

let soma = 0;

for (let s = 0; s<12; s++) {
    soma += matriz[s][C];
}

soma = soma.toFixed(1);

if (T === 'S') {
    console.log(soma);
} else if (T === 'M') {
    let media = (soma/12).toFixed(1);
    console.log(media);
} else {

}
