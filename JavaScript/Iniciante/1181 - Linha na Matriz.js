const L = parseInt(lines.shift());
const T = String(lines.shift());

let matriz = Array();
let linha = Array();
let item;

for (let i = 0; i<12; i++) {
    for (let l = 0; l<12; l++) {
        item = parseFloat(lines.shift());
        linha.push(item);
    }
    matriz.push(linha);
    linha = Array();
}

let soma = 0;

for (let s = 0; s<12; s++) {
    soma += matriz[L][s];
}

soma = soma.toFixed(1);

if (T === 'S') {
    console.log(soma);
} else if (T === 'M') {
    let media = soma/12;
    media = media.toFixed(1);
    console.log(media);
} else {

}
