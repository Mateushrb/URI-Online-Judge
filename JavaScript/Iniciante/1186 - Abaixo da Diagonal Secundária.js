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
let qtd = 1;
let dividendo = 0;

for (let m = 11; m>0; m--) {
    for (let n = qtd; n<12; n++) {
        soma += matriz[m][n];
        dividendo++;
    }
    qtd++;
}

if (O === 'S') {
    soma = soma.toFixed(1);
    console.log(soma);
} else if (O === 'M') {
    let media = (soma/dividendo).toFixed(1);
    console.log(media);
} else {
    
}
