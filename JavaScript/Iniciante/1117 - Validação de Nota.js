let soma = 0;
let nota;
let qtd = 0;
while (qtd != 2) {
    nota = parseFloat(lines.shift());
    if (nota < 0 || nota > 10) {
        console.log('nota invalida');
    } else {
        soma += nota;
        qtd += 1;
    }
}
console.log(`media = ${(soma/2).toFixed(2)}`)
