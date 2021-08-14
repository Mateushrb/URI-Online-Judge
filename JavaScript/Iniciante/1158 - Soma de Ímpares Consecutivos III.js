const N = parseInt(lines.shift());

for (let i = 0; i < N; i++) {
    let numeros = lines.shift().split(' ');
    let X = parseInt(numeros[0]);
    let Y = parseInt(numeros[1]);

    let soma = 0;
    if (X%2 === 0) {
        X ++;
    }
    for (let l = 0; l < Y; l++) {
        soma += X;
        X += 2;
    }
    console.log(soma);
}
