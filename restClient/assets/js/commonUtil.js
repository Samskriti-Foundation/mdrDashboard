/* creates a new XMLHttpRequest object which is the backbone of AJAX, or returns false if the browser doesn't support it
 */
function getXMLHttpRequest() {
	var xmlHttpReq = false;
	// to create XMLHttpRequest object in non-Microsoft browsers
	if (window.XMLHttpRequest) {
		xmlHttpReq = new XMLHttpRequest();
	} else if (window.ActiveXObject) {
		try {
			// to create XMLHttpRequest object in later versions of Internet
			// Explorer
			xmlHttpReq = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (exp1) {
			try {
				// to create XMLHttpRequest object in older versions of Internet
				// Explorer
				xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (exp2) {
				xmlHttpReq = false;
			}
		}
	}
	return xmlHttpReq;
}

//Method to focus on the first text field of the form 
function setFocus(formName)
{
	var i=0;
	for(i=0;;i++)
		{
		var elem = formName.getElementsByTagName("input")[i];
			if(elem.type == "text" || elem.type=="password")
				{
				var val=elem.value;
				elem.focus();
				elem.value="";
				elem.value=val;
			break;
				}
		}
	}

//method to clear all the text field except the first text field.
function Formclear(frm){
	var inputs = frm.getElementsByTagName('input');
	var i=1;
	for(i;i<inputs.length;i++)
		{
		frm.getElementsByTagName("input")[i].value="";
		}
}
function clearfield(frm){
	var elements = document.getElementsByTagName("input");
	for (var i=0; i < elements.length; i++) {
	  if (elements[i].type == "text" || elements[i].type=="password") {
	    elements[i].value = "";
	    setFocus(frm);
	  }
	}
	}
