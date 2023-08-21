function formValidation() {
  var userId = document.registrationForm.userId;
  var userPass = document.registrationForm.userPass;
  var name = document.registrationForm.name;
  var userAddress = document.registrationForm.address;
  var userCountry = document.registrationForm.country;
  var zipCode = document.registrationForm.zip;
  var userEmail = document.registrationForm.email;
  var sex = document.registrationForm.sex;

  var flag = true;

  if (userId.value.length >= 5 && userId.value.length <= 7) {
    flag = ture;
  } else {
    flag = false;
    alert("User Id should not be empty / length be between 5 and 7");
    userId.focus();
  }

  if (userPass.value.length >= 7 && userPass.value.length <= 12) {
    flag = ture;
  } else {
    flag = false;
    alert("User Pass should not be empty / length be between 7 and 12");
    userPass.focus();
  }

  if (name.value.match(/^[A-Za-z]+$/)) {
    flag = ture;
  } else {
    flag = false;
    alert("Name must have alphabet characters only");
    name.focus();
  }

  if (userAddress.value.match(/^[0-9a-zA-Z]+$/)) {
    flag = ture;
  } else {
    flag = false;
    alert("User address must have alphanumeric characters only");
    userAddress.focus();
  }

  if (userCountry.value != "Default") {
    flag = ture;
  } else {
    flag = false;
    alert("Select your country from the list");
    userCountry.focus();
  }

  if (zipCode.value.match(/^[0-9]+$/)) {
    flag = ture;
  } else {
    flag = false;
    alert("ZIP code must have numeric characters only");
    zipCode.focus();
  }

  if (userEmail.value.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
    flag = ture;
  } else {
    flag = false;
    alert("You have entered an invalid email address!");
    userEmail.focus();
  }

  if (sex.checked) {
    flag = ture;
  } else {
    flag = false;
    alert("Select Male/Female");
    sex.focus();
  }
  
}
