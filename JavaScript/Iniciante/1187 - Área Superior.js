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
let dividendo = 0;

let limite = 10;

for (let m = 0; m<=4; m++) {
    for (let n = m+1; n<=limite; n++) {
        soma += matriz[m][n];
        dividendo += 1;
    }
    limite -= 1;
}

if (O === 'S') {
    console.log(soma.toFixed(1));
} else if (O === 'M') {
    let media = (soma/dividendo).toFixed(1);
    console.log(media);
} else {

}
