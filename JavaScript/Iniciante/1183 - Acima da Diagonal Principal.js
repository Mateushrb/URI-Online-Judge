const O = String(lines.shift());

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
let dividendo = 0;
let s = 1;
for (let m = 0; m<11; m++) {
    for (let n = s; n<12; n++) {
        soma += matriz[m][n];
        dividendo += 1;
    }
    s += 1;
}

if (O === 'S') {
    console.log(soma.toFixed(1));
} else if (O === 'M') {
    console.log((soma/dividendo).toFixed(1));
}
