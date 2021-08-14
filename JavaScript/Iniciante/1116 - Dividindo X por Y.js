const N = parseInt(lines.shift());

let valores;
let X;
let Y;

let divisao;

for (let i = 0; i < N; i++) {
    valores = lines.shift().split(' ');
    X = parseInt(valores[0]);
    Y = parseInt(valores[1]);

    if (Y === 0) {
        console.log('divisao impossivel');
    } else {
        divisao = (X/Y).toFixed(1);
        console.log(divisao);
    }
}
