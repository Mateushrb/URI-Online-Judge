let N = parseInt(lines.shift());
let fibo = '0 1';
let numero = 1;

if (N === 1) {
    console.log('0');
} else if (N === 2) {
    console.log(fibo);
} else {
    for (let i = 0; i < N-2; i++) {
        let linha = fibo.split(' ');
        let tamanho = linha.length;
        let calc = parseInt(linha[tamanho-1]) + parseInt(linha[tamanho-2]);
        fibo += ' ';
        fibo += String(calc);
    }
    console.log(fibo);
}
