let valores = Array();

const T = parseInt(lines.shift());

for (let i = 0; i < T; i++) {
    let N = parseInt(lines.shift());

    let sequencia = Array();
    sequencia.push(0, 1);

    if (N > 1) {
        for (let l = 1; l <= N; l++) {
            let soma = sequencia[l] + sequencia[l-1];
            sequencia.push(soma);
        }
    }
    valores.push(`Fib(${N}) = ${sequencia[N]}`);
}

for (let saida = 0; saida < valores.length; saida++) {
    console.log(valores[saida]);
}
