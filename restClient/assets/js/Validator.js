function numericValidator(fieldArray) {
	var msg = "";
	for (var i = 0; i < fieldArray.length; i++) {
	  if(isNaN(fieldArray[i].value)){
		  msg = "Please provide numeric fields.";
		 fieldArray[i].className =fieldArray[i].className + " inputError";
	  } else {
		 fieldArray[i].className = fieldArray[i].className.replace("inputError", "") ;
	  }
	}
	return msg;
}

function phoneNOValidator(fieldArray) {
	var msg = "";
	for (var i = 0; i < fieldArray.length; i++) {
		fieldArray[i].value = fieldArray[i].value.trim();
	  if(fieldArray[i].value.length !=10 || isNaN(fieldArray[i].value)){
		 fieldArray[i].className =fieldArray[i].className + " inputError";
		 msg = "Please provide corrrect phone no.";
	  } else {
		 fieldArray[i].className = fieldArray[i].className.replace("inputError", "") ;
	  }
	}
	return msg;
}	

/*
function mailValidator(emailField) {	
	var isErrorExisting = false;
	for(var i = 0 ; i < emailField.length ; i++){
		if(emailField[i].value != "") {
			var atpos = emailField[i].value.indexOf("@");
			var dotpos = emailField[i].value.lastIndexOf(".");
			if(atpos<1 || dotpos<atpos+2 || dotpos+2 >= email.length) {
				isErrorExisting = true;
				emailField[i].className =emailField[i].className + " inputError";
			} else {
				emailField[i].className = emailField[i].className.replace("inputError", "") ;
			}
		}
	}
	return isErrorExisting;
}
*/
function emailValidator(emailField) {	
	var msg = "";
	for(var i = 0 ; i < emailField.length ; i++){
		emailField[i].value = emailField[i].value.trim();
		if(emailField[i].value != "") {
//			var emailReg = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
			
			var emailReg = /^([a-zA-Z0-9._-]{1,40})+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
			if(!emailField[i].value.match(emailReg)) {
				emailField[i].className =emailField[i].className + " inputError";
				msg = "Please provide email of correct format.";
			} else {
				emailField[i].className = emailField[i].className.replace("inputError", "") ;
			}
		}
	}
	return msg;
}

function compareStringValidator(fiedlArray) {
	var msg = "";
	if(fiedlArray[0].value != "" && fiedlArray[1].value != ""){
		if(fiedlArray[0].value != fiedlArray[1].value) {
			msg = "Values not matching.";
			fiedlArray[1].className =fiedlArray[1].className + " inputError";
		} else {
			fiedlArray[1].className = fiedlArray[1].className.replace("inputError", "") ;
		}
	}
	return msg;
}

function requiredFieldValidator(fieldArray) {
	//var isRequired = false;
	var msg = "";
	for (var i = 0; i < fieldArray.length; i++) {
		fieldArray[i].value = fieldArray[i].value.trim();		
	  if(fieldArray[i].value == "" || fieldArray[i].value =="-1"){
		 isRequired = true;
		 msg = "Please provide mandatory fields";
		 fieldArray[i].className = fieldArray[i].className + " inputError";
		 if(fieldArray[i].id != "password" || fieldArray[i].id != "cnfpassword" || 
				 fieldArray[i].id != "email" || fieldArray[i].id !="address") {
		 }
	  } else {
		  fieldArray[i].className = fieldArray[i].className.replace("inputError", "") ;
	  }
	}
	return msg;
}

/**
 * Checks if at least one field in not empty from the given field array
 * @param fieldArray
 * @returns {String}
 */
function atLeastOneFieldValidator(fieldArray) {
	var msg = "Please enter at least one field";
	for(var i = 0; i < fieldArray.length; i++) {
		fieldArray[i].value = fieldArray[i].value.trim();
		if(fieldArray[i].value != "" && fieldArray[i].value != "-1"){
			msg = "";
			return msg;
		}
	}
	return msg;
}

/**
 * @author Neel Borooah
 * @param messageArray
 */
function alertMSG(messageArray) {
	var message="";
	for(var i = 0; i < messageArray.length; i++) {
		message += messageArray[i] + "\n";
	}
	alert(message);
}

function noSpecialCharacterValidator(fieldArray) {
	//var isErrorExisting = false;
	var msg = ""; 
	var alphaExp = /^[a-zA-Z0-9\s]+$/ ;
	
	for (var i = 0; i < fieldArray.length; i++) {
		fieldArray[i].value = fieldArray[i].value.trim();
	  if(fieldArray[i].value.length > 1 && !fieldArray[i].value.match(alphaExp)){
	//	 isErrorExisting = true;
		 msg = "Special characters are not allowed.Please enter valid data.";
		 fieldArray[i].className =fieldArray[i].className + " inputError";
	  } else {
		 fieldArray[i].className = fieldArray[i].className.replace("inputError", "") ;
	  }
	}
	return msg;
}

function minLengthCharacterValidator(fieldArray) {
//	var isErrorExisting = false;
	var msg = "";
	for (var i = 0; i < fieldArray.length; i++) {
		fieldArray[i].value = fieldArray[i].value.trim();
	  if(fieldArray[i].value.length < 3){
//		 isErrorExisting = true;
		  msg = "Please enter data of minimum 3 characters.";
		 fieldArray[i].className =fieldArray[i].className + " inputError";
	  } else {
		 fieldArray[i].className = fieldArray[i].className.replace("inputError", "") ;
	  }
	}
	return msg;
}

function passwordValidator(field) {
	var isErrorExisting = false;
	var msg = "";
	field.value = field.value.trim();
	// password between 8 to 15 characters which contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character
	
	var decimal=  /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
	  if(field.value.length > 1 && !field.value.match(decimal)){
		 isErrorExisting = true;
		 msg = "Password is not in correct format.";
		 field.className =field.className + " inputError";
	  } else {
		 field.className = field.className.replace("inputError", "") ;
	  }
	return isErrorExisting;
	return msg;
}