function inputValidate() {
  var name = document.from1.fullname;
  var email = document.from1.email;
  var address = document.from1.address;
  var city = document.from1.city;
  var cnic = document.from1.cnic;
  var noc = document.from1.noc;
  var ccn = document.from1.ccn;
  var expiry = document.from1.expiry;

  if (!name.value.match(/^[A-Za-z]+$/)) {
    alert("Name must have alphabet characters only");
    return;
  }

  if (!email.value.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
    alert("You have entered an invalid email address!");
    return;
  }

  if (!address.value.match(/^[0-9a-zA-Z]+$/)) {
    alert("User address must have alphanumeric characters only");
    return;
  }

  if (!city.value.match(/^[A-Za-z]+$/)) {
    alert("City must have alphabet characters only");
    return;
  }

  if (!cnic.value.match(/^\d{5}-\d{7}-\d{1}$/)) {
    alert("CNIC is incorrect");
    return;
  }
  
  if (!noc.value.match(/^[a-zA-Z]{3,}/)) {
    alert("Name on card is incorrect");
    return;
  }

  if (!ccn.value.match(/^\d{4}-\d{4}-\d{4}-\d{4}/)) {
    alert("Credit Card Number is incorrect");
    return;
  }

  if (!expiry.value.match(/^\d{4}$/)) {
    alert("Expiry month is incorrect");
    return;
  }

  else {
    alert("Form submitted succesfully");
    return;
  }
}
