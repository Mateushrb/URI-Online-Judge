let coordenadas = lines.shift().split(' ')

const X = parseFloat(coordenadas[0])
const Y = parseFloat(coordenadas[1])

if (X === 0 && Y ===0) {
    console.log('Origem')
} else if (X > 0 && Y > 0) {
    console.log('Q1')
} else if (X < 0 && Y > 0) {
    console.log('Q2')
} else if (X < 0 && Y < 0) {
    console.log('Q3')
} else if (X > 0 && Y < 0) {
    console.log('Q4')
} else if (X === 0 && Y !== 0) {
    console.log('Eixo Y')
} else if (X !== 0 && Y === 0) {
    console.log('Eixo X')
}
