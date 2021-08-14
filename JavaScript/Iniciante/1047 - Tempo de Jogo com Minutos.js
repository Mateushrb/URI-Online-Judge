const horarios = lines.shift().split(' ')

let hInicio = parseInt(horarios[0])
let mInicio = parseInt(horarios[1])
let hFim = parseInt(horarios[2])
let mFim = parseInt(horarios[3])

let minutos
let horas

if (hInicio === hFim && mInicio === mFim) {
    minutos = 0
    horas = 24
} else {
    if (mInicio > mFim) {
        minutos = 60 - mInicio + mFim
    } else {
        minutos = mFim - mInicio
    }
    
    if (hInicio > hFim) {
        horas = 24 - hInicio + hFim
    } else {
        horas = hFim - hInicio
    }
}
if (mInicio > mFim) {
    horas -= 1
} if (hInicio === hFim && mInicio > mFim) {
    horas = 23
} 

console.log(`O JOGO DUROU ${horas} HORA(S) E ${minutos} MINUTO(S)`)
