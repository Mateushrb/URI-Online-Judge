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
let inicio = 1;
let divisor = 0;

for (let m = 11; m>=7; m--) {
    for (let n = inicio; n<m; n++) {
        soma += matriz[m][n];
        divisor += 1;
    }
    inicio += 1;
}

if (O === 'S') {
    console.log(soma.toFixed(1));
} else if (O === 'M') {
    let media = (soma/divisor).toFixed(1);
    console.log(media);
} else {

}
