//Convert a Dog Age to Human Age
let myAge = 24; //초기 나이
let earlyYears = 2;
earlyYears *= 10.5
let laterYears = myAge - 2;  //첫 2년은 10.5살임
laterYears *= 4;

let myAgeInDogYears = earlyYears + laterYears;

let myName = "KimJungWoo".toLowerCase();

console.log(`My name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} old in dog years.`)