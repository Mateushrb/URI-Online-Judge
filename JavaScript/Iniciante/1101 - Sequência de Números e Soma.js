let valores = lines.shift().split(' ')

let M
let N

if (parseInt(valores[0]) > parseInt(valores[1])) {
    M = parseInt(valores[0])
    N = parseInt(valores[1])
} else {
    M = parseInt(valores[1])
    N = parseInt(valores[0])
}

while (N > 0) {
    let sequencia = ''
    let soma = 0
    for (let i = N; i < M+1; i++) {
        sequencia += String(i)
        sequencia += ' '
        soma += i
    }
    console.log(`${sequencia}Sum=${soma}`)

    valores = lines.shift().split(' ')

    if (parseInt(valores[0]) > parseInt(valores[1])) {
        M = parseInt(valores[0])
        N = parseInt(valores[1])
    } else {
        M = parseInt(valores[1])
        N = parseInt(valores[0])
    }
}
