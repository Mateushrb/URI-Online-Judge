while (true) {
    let qtd = 0;
    let soma = 0;
    let nota;

    while (qtd != 2) {
        nota = parseFloat(lines.shift());
        if (nota < 0 || nota > 10) {
            console.log('nota invalida');
        } else {
            soma += nota;
            qtd += 1;
        }
    }

    console.log(`media = ${(soma/2).toFixed(2)}`);
    
    let novoCalculo;

    while (true) {
        console.log('novo calculo (1-sim 2-nao)');
        novoCalculo = lines.shift();
        if (novoCalculo === '1' || novoCalculo === '2') {
            break;
        } else {

        }
    }

    if (novoCalculo === '2') {
        break;
    } else {

    }
}
