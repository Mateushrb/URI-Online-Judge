const valores = lines.shift().split(' ')

const V1 = parseInt(valores[0])
const V2 = parseInt(valores[1])
const V3 = parseInt(valores[2])

if (V1 < V2 && V1 < V3) {
    console.log(V1)
    if (V2 < V3) {
        console.log(V2)
        console.log(V3)
    } else {
        console.log(V3)
        console.log(V2)
    }
} else if (V2 < V1 && V2 < V3) {
    console.log(V2)
    if (V1 < V3) {
        console.log(V1)
        console.log(V3)
    } else {
        console.log(V3)
        console.log(V1)
    }
} else {
    console.log(V3)
    if (V1 < V2) {
        console.log(V1)
        console.log(V2)
    } else {
        console.log(V2)
        console.log(V1)
    }
}

console.log('')
console.log(V1)
console.log(V2)
console.log(V3)
