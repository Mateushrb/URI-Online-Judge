let notas = lines.shift().split(' ')

const N1 = parseFloat(notas[0])
const N2 = parseFloat(notas[1])
const N3 = parseFloat(notas[2])
const N4 = parseFloat(notas[3])

let media = (N1*2 + N2*3 + N3*4 + N4*1) / 10
media = media.toFixed(1)

console.log(`Media: ${media}`)

if (media >= 7) {
    console.log('Aluno aprovado.')
} else if (media < 5) {
    console.log('Aluno reprovado.')
} else if (media >= 5 && media < 7) {
    console.log('Aluno em exame.')
    let NE = parseFloat(lines.shift())
    NE = NE.toFixed(1)
    console.log(`Nota do exame: ${NE}`)
    let novaMedia = (parseFloat(media) + parseFloat(NE)) / 2
    novaMedia = novaMedia.toFixed(1)
    if (novaMedia >= 5) {
        console.log('Aluno aprovado.')
        console.log(`Media final: ${novaMedia}`)
    } else {
        console.log('Aluno reprovado.')
        console.log(`Media final: ${novaMedia}`)
    }
}
