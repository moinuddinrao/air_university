function add() {
  var num1 = parseInt(document.getElementById('num1').value);
  var num2 = parseInt(document.getElementById('num2').value);
  var result = num1 + num2;
  document.getElementById('result').innerHTML = result;
}

function sub() {
  var num1 = parseInt(document.getElementById('num1').value);
  var num2 = parseInt(document.getElementById('num2').value);
  var result = num1 - num2;
  document.getElementById('result').innerHTML = result;
}

function mul() {
  var num1 = parseInt(document.getElementById('num1').value);
  var num2 = parseInt(document.getElementById('num2').value);
  var result = num1 * num2;
  document.getElementById('result').innerHTML = result;
}

function div() {
  var num1 = parseInt(document.getElementById('num1').value);
  var num2 = parseInt(document.getElementById('num2').value);
  var result = num1 / num2;

  document.getElementById('result').innerHTML = result;
}
