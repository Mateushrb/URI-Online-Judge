const tempo = parseInt(lines.shift())

let horas = parseInt(tempo/3600)
let minutos = parseInt((tempo%3600)/60)
let segundos = tempo%60

console.log(`${horas}:${minutos}:${segundos}`)
