const O = String(lines.shift());

let matriz = Array();
let linha = Array();

for (let i = 0; i<12; i++) {
    for (let j = 0; j<12; j++) {
        let elemento = parseFloat(lines.shift());
        linha.push(elemento);
    }
    matriz.push(linha);
    linha = [];
}

let soma = 0;
let divisor = 0;
let limite = 10;

for (let m = 1; m<11; m++) {
    for (let n = 11; n>limite; n--) {
        soma += matriz[m][n];
        divisor++;
    }
    if (m < 5) {
        limite--;
    } else if (m > 5) {
        limite++;
    }
}

if (O === 'S') {
    console.log(soma.toFixed(1));
} else if (O === 'M') {
    let media = (soma/divisor).toFixed(1);
    console.log(media);
} else {

}
