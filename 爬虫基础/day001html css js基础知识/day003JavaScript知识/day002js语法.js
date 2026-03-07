//数据类型
var aa

console.log(typeof(aa))

var nullData= null

console.log(typeof(nullData))

//一种复杂类型
var obj ={
    name:"张山",
    age:18,
    sex:"男"
}
console.log(obj)
console.log(typeof(obj))

//json 字符串
dd=JSON.stringify(obj)
console.log(typeof(dd),dd)
ee=JSON.parse(dd)
console.log(ee)