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
let limite = 11;

for (let m = 0; m<11; m++) {
    for (let n = 0; n<limite; n++) {
        soma += matriz[m][n];
        dividendo += 1;
    }
    limite -= 1;
}

switch (O) {
    case 'S':
        soma = soma.toFixed(1);
        console.log(soma);
        break;
    case 'M':
        let media = (soma/dividendo).toFixed(1);
        console.log(media);
        break;
    default:

}
