/**
 * @author Neel Borooah 
 * 
 * ################################################################################################
 * 
 * Manual:
 * ============================================================================
 * Creates a tri state tree structure 
 * 
 * ----------------------------------------------------------------------------------
 * Function : Expand/Collapse nodes
 *  -	Required: Two icons for expanding and contracting Nodes whose location is specified 
 * 				in hasChildrenOpen and hasChildrenClosed
 * 	-	Call toggleVisibility on click of tree plus/minus icon
 * 	-	Set children nodes inside inner div whose ID is parent node id + "DIV"
 * 	-	Specify the class of tree plus/minus icon as hasChildrenOpen/hasChildrenClosed/noChildren
 * ---------------------------------------------------------------------------------------
 * Function: Check/Uncheck Box
 * 	-	Required: 3 state images whose location is specified in checked, intermediate, and unchecked variables
 * 	-	Call toggleNodes on click of checkbox image
 * 	-	Specify the class of checkbox image as "checkbox"
 * 
 * ==================================================================================
 * ########################################################################################################
 */

var checked = '../assets/images/menu/checked.gif';
var intermediate = '../assets/images/menu/intermediate.gif';
var unchecked = '../assets/images/menu/unchecked.gif';

var hasChildrenOpen = "../assets/images/menu/tree_minus.png";
var hasChildrenClosed = "../assets/images/menu/tree_plus.png";

function setContextPath(path) {
	checked = "/" + path + '/assets/images/menu/checked.gif';
	
	intermediate = "/" +  path + '/assets/images/menu/intermediate.gif';
	unchecked = "/" +  path + '/assets/images/menu/unchecked.gif';
	
	hasChildrenOpen = "/" + path + "/assets/images/menu/tree_minus.png";
	hasChildrenClosed = "/" + path + "/assets/images/menu/tree_plus.png";

}

function toggleVisibility(id, path) {	
   var e = document.getElementById(id+"DIV");
   $("#" + e.id).slideToggle();
   var list_status = document.getElementById(id + "IMG").getAttribute("class");
   if(list_status == "hasChildrenOpen") {
	   document.getElementById(id + "IMG").setAttribute("class", "hasChildrenClosed");
	   document.getElementById(id + "IMG").setAttribute("src", hasChildrenClosed);
   }
   else if(list_status == "hasChildrenClosed") {
	   document.getElementById(id + "IMG").setAttribute("class", "hasChildrenOpen");
	   document.getElementById(id + "IMG").setAttribute("src", hasChildrenOpen);
   }
}

function toggleNodes(id, path) {
	
	var e = document.getElementById(id);
	//Toggle value of check box
	if((e.alt == "unchecked") || (e.alt == "intermediate"))  {
		e.alt = "checked";
		e.src = checked;
	}
	else {
		e.alt = "unchecked";
		e.src = unchecked;
	}
	parentToggler(e); //Toggles value of children according to parent
	childToggler(); //Toggles value of parent according to children
}

function parentToggler(e) {
	//Set all children to checked or unchecked depending upon parent status
	var id = e.id;
	if(e.alt == "checked") {
		var divs = document.getElementsByTagName("img"), item;
		for (var i = 0, len = divs.length; i < len; i++) {
			if(divs[i].getAttribute("class") != "checkbox")
				continue;
		    item = divs[i];
		    if (item.id && item.id.indexOf(id) == 0) {
		        item.src = checked;
		        item.alt = "checked";
		    }
		}
	}
	else {
		var divs = document.getElementsByTagName("img"), item;
		for (var i = 0, len = divs.length; i < len; i++) {
			if(divs[i].getAttribute("class") != "checkbox")
				continue;
		    item = divs[i];
		    if (item.id && item.id.indexOf(id) == 0) {
		        item.src = unchecked;
		        item.alt = "unchecked";
		    }
		}
	}
}

function childToggler() {
	var allElem = document.getElementsByTagName("img");
	for(var i = 0; i < allElem.length; i++) {
		if(allElem[i].getAttribute("class") != "checkbox")
			continue;
		var flag1 = true;
		var flag2 = false;
		var count = 0;
		for(var j = 0; j < allElem.length; j++) {
			if(allElem[j].getAttribute("class") != "checkbox")
				continue;
			if(allElem[i] == allElem[j]) {
				count++;
				continue;
			}
			if(allElem[i].id && allElem[j].id.indexOf(allElem[i].id) == 0) {
				count++;
				if(allElem[j].alt == "unchecked") {
					flag1 = false;
				}
				else if(allElem[j].alt == "checked") {
					flag2 = true;
				}
    		}
			
		}			
		if((flag1) && (count > 1)) {
			//If all children are checked, parent node is checked
			allElem[i].src = checked;
			allElem[i].alt = "checked";
		}
		if((!flag2) && (count > 1)) {
			//If all children are unchecked, parent node is unchecked
			allElem[i].src = unchecked;
			allElem[i].alt = "unchecked";
		}
		if((!flag1) && (flag2) && (count > 1)) {
			//Puts intermediate image if few children are checked
			allElem[i].src = intermediate;
			allElem[i].alt = "intermediate";
		}
		
	}
}

/**
 *  Returns the tree to it's initial state
 *  Gets the JSON initial state from hidden field (menuFkId)
 * @returns {Boolean}
 */
function getTreeState() {
	var obj = JSON.parse(document.getElementById("menuFkId").value);
	var flag = false;
	var allElem = document.getElementsByTagName("img");
	for ( var i = 0; i < allElem.length; i++) {
		flag = false;
		if (allElem[i].getAttribute("class").indexOf("checkbox") == -1)
			continue;
		
		for(var k in obj) {
			if(obj[k].menuFkId == allElem[i].id) {
				allElem[i].alt = "checked";
				allElem[i].src = checked;
				flag = true;
			}
		}
		
		if(!flag) {
			allElem[i].alt = "unchecked";
			allElem[i].src = unchecked;
		}
	}
	return true;
}

/**
 * Saves the tree state in check box form within hidden field (menuFkId)
 * @returns {Boolean}
 */
function saveTreeState() {
	var menuFkId = [];
	var allElem = document.getElementsByTagName("img");
	for ( var i = 0; i < allElem.length; i++) {
		/*if (allElem[i].getAttribute("class").indexOf("checkbox") == -1)
			continue;*/
		if (allElem[i].alt != "checked")
			continue;
		var map = {};
		map["menuFkId"] = allElem[i].id;
		map["roleFkId"] = 1;
		menuFkId.push(map);
	}
	document.getElementById("menuFkId").value = JSON.stringify(menuFkId);
	return true;
}