var A = parseFloat(lines.shift())
var B = parseFloat(lines.shift())

var MP = ((A*3.5) + (B*7.5)) / 11
MP = MP.toFixed(5)

console.log(`MEDIA = ${MP}`)
