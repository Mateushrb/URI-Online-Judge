let X = parseInt(lines.shift());
while (X !== 0) {
    if (X % 2 !== 0) {
        X++;
    }
    let soma = X;
    for (let i = 0; i < 4; i++) {
        X += 2;
        soma += X;
    }
    console.log(soma);

    X = parseInt(lines.shift());
}
