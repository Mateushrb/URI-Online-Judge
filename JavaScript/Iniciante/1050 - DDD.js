const DDD = parseInt(lines.shift())

let cidade

if (DDD === 61) {
    cidade = 'Brasilia'
} else if (DDD === 71) {
    cidade = 'Salvador'
} else if (DDD === 11) {
    cidade = 'Sao Paulo'
} else if (DDD === 21) {
    cidade = 'Rio de Janeiro'
} else if (DDD === 32) {
    cidade = 'Juiz de Fora'
} else if (DDD === 19) {
    cidade = 'Campinas'
} else if (DDD === 27) {
    cidade = 'Vitoria'
} else if (DDD === 31) {
    cidade = 'Belo Horizonte'
} else {
    cidade = 'DDD nao cadastrado'
}

console.log(cidade)
