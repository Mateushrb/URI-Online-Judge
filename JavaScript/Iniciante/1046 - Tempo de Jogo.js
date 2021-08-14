let horas = lines.shift().split(' ')

let inicio = parseInt(horas[0])
let fim = parseInt(horas[1])

let duracao

if (inicio === fim) {
    console.log('O JOGO DUROU 24 HORA(S)')
} else {
    if (inicio > fim) {
        duracao = 24 - inicio + fim
        console.log(`O JOGO DUROU ${duracao} HORA(S)`)
    } else {
        duracao = fim - inicio
        console.log(`O JOGO DUROU ${duracao} HORA(S)`)
    }
}
