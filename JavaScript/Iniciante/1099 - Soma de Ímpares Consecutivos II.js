const N = parseInt(lines.shift())

for (let i = 0; i<N; i++) {
    let valores = lines.shift().split(' ')

    let X
    let Y

    let soma = 0

    if (parseInt(valores[0]) > parseInt(valores[1])) {
        X = parseInt(valores[0])
        Y = parseInt(valores[1])
    } else {
        X = parseInt(valores[1])
        Y = parseInt(valores[0])
    }

    Y += 1

    while (Y < X) {
        if (Y%2 != 0) {
            soma += Y
        }
        Y += 1
    }
    console.log(soma)
}
