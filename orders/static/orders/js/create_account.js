document.addEventListener("DOMContentLoaded", function(event) { 

	var password1 = document.getElementById("password1");
	var password2 = document.getElementById("password2");
	var letter = document.getElementById("letter");
	var capital = document.getElementById("capital");
	var number = document.getElementById("number");
	var length = document.getElementById("length");
	var btnCreate = document.getElementById("submit");

// When the user clicks on the password field, show the message box
	password1.onfocus = function() {
		document.getElementById("pwd_message").style.display = "block";			
	}

// When the user clicks outside of the password field, hide the message box
//	password1.onblur = function() {
//		document.getElementById("pwd_message").style.display = "none";
//	}

// When the user starts to type something inside the password field
	password1.onkeyup = function() {
	
// Validate lowercase letters
		var lowerCaseLetters = /[a-z]/g;
		if(password1.value.match(lowerCaseLetters)) { 
			letter.classList.remove("invalid");
			letter.classList.add("valid");
		} 
		else {
			letter.classList.remove("valid");
			letter.classList.add("invalid");
		}

// Validate capital letters
		var upperCaseLetters = /[A-Z]/g;
		if(password1.value.match(upperCaseLetters)) { 
			capital.classList.remove("invalid");
			capital.classList.add("valid");
		} 
		else {
			capital.classList.remove("valid");
			capital.classList.add("invalid");
		}

// Validate numbers
		var numbers = /[0-9]/g;
		if(password1.value.match(numbers)) { 
			number.classList.remove("invalid");
			number.classList.add("valid");
		} 
		else {
			number.classList.remove("valid");
			number.classList.add("invalid");
		}

// Validate length
		if(password1.value.length >= 8) {
			length.classList.remove("invalid");
			length.classList.add("valid");
		} 
		else {
			length.classList.remove("valid");
			length.classList.add("invalid");
		}
		
		if(password1.value == password2.value) {
			match.classList.remove("invalid");
			match.classList.add("valid");
		} 
		else {
			match.classList.remove("valid");
			match.classList.add("invalid");
		}
	}
	
	password2.onkeyup = function(){
		if(password1.value == password2.value) {
			match.classList.remove("invalid");
			match.classList.add("valid");
		} 
		else {
			match.classList.remove("valid");
			match.classList.add("invalid");
		}
	}
});