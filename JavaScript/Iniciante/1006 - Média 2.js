var A = parseFloat(lines.shift())
var B = parseFloat(lines.shift())
var C = parseFloat(lines.shift())

var MP = ( (A*2) + (B*3) + (C*5) ) / 10
MP = MP.toFixed(1)

console.log(`MEDIA = ${MP}`)
