// Temp Conversion without UsrInput
// UsrInput은 JS 완독하고 Web과 연동하여 구현

const kelvin = 293;  // 정해진 수치
var celsius = kelvin - 273;  // kelvin - 273 은 celsius
var fahrenheit = celsius * (9/5) + 32; // Temperature Convert
Math.floor(fahrenheit);

console.log(`Converted Temperature is ${fahrenheit}`);
