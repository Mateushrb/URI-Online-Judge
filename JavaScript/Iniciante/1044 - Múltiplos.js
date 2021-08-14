let valores = lines.shift().split(' ')

const A = parseInt(valores[0])
const B = parseInt(valores[1])

if (A > B) {
    if (A%B === 0) {
        console.log('Sao Multiplos')
    } else {
        console.log('Nao sao Multiplos')
    }
} else {
    if (B%A === 0) {
        console.log('Sao Multiplos')
    } else {
        console.log('Nao sao Multiplos')
    }
}
