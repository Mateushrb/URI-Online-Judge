const raio = parseFloat(lines.shift())
const pi = 3.14159

let volume = (4/3) * pi * Math.pow(raio, 3)
volume = volume.toFixed(3)

console.log(`VOLUME = ${volume}`)
