let inicioDia = lines.shift().split(' ')
let inicioHora = lines.shift().split(' ')
let fimDia = lines.shift().split(' ')
let fimHora = lines.shift().split(' ')

let diaInicio = parseInt(inicioDia[1])
let horaInicio = parseInt(inicioHora[0])
let minutoInicio = parseInt(inicioHora[2])
let segundoInicio = parseInt(inicioHora[4])

let diaFim = parseInt(fimDia[1])
let horaFim = parseInt(fimHora[0])
let minutoFim = parseInt(fimHora[2])
let segundoFim = parseInt(fimHora[4])

let diaTotal = 0
let horaTotal = 0
let minutoTotal = 0
let segundoTotal = 0

/* O segredo é somar os valores nas variáveis ao invés de redefinilas com novos valores */

if (segundoInicio > segundoFim) {
    segundoTotal = 60 - segundoInicio + segundoFim
    minutoTotal -= 1
} else {
    segundoTotal = segundoFim - segundoInicio
}

if (minutoInicio > minutoFim) {
    minutoTotal += 60 - minutoInicio + minutoFim
    horaTotal -= 1
} else if (minutoInicio < minutoFim) {
    minutoTotal += minutoFim - minutoInicio
} else {
    if (segundoInicio > segundoFim) {
        minutoTotal = 59
        horaTotal -= 1
    }
}

if (horaInicio > horaFim) {
    horaTotal += 24 - horaInicio + horaFim
    diaTotal -= 1
}else if (horaInicio < horaFim) {
    horaTotal += horaFim - horaInicio
} else {
    if (minutoInicio > minutoFim) {
        horaTotal = 23
        diaTotal -= 1
    }
}

diaTotal += diaFim - diaInicio

console.log(`${diaTotal} dia(s)`)
console.log(`${horaTotal} hora(s)`)
console.log(`${minutoTotal} minuto(s)`)
console.log(`${segundoTotal} segundo(s)`)