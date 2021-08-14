let X
let Y
let valores
while (true) {
    valores = lines.shift().split(' ')

    X = parseInt(valores[0])
    Y = parseInt(valores[1])

    if (X === Y) {
        break
    } else {
        if (X > Y) {
            console.log('Decrescente')
        } else {
            console.log('Crescente')
        }
    }
}
