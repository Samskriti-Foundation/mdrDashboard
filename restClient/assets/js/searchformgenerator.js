var recordsPerPage = 20;//Default no of records per page as of now.
var isConditionalSearch = false;
var pager = new Pager('displayRow', recordsPerPage);
var pageNo = 1;
var requestId = null;

function sendToPage() {
	alert('inside method');
	var link = document.getElementById("createPageURL").value;
	document.getElementById("mainForm").action = link;
	document.getElementById("mainForm").submit();
}

function setRequestId(requestId) {
	this.requestId = requestId;
}

function Pager(tableName, itemsPerPage) {
	
	this.tableName = tableName;
	this.itemsPerPage = itemsPerPage;
	this.currentPage = 1;
	this.pages = 0;
	this.inited = false;
	
	this.showPage = function(pageNumber) {
		if (! this.inited) {
			alert("not inited");
			return;
		}
	//	var oldPageAnchor = document.getElementById('pg'+this.currentPage);
	//	oldPageAnchor.className = 'pg-normal';
		this.currentPage = pageNumber;
	//	var newPageAnchor = document.getElementById('pg'+this.currentPage);
	//	newPageAnchor.className = 'pg-selected';
	//	
		var element = document.getElementById('pagerCombo');
	    element.value = pageNumber;
		
	}
	
	this.init = function(records) {
		this.tableName = tableName;
		this.itemsPerPage = itemsPerPage;
		this.pages = 0;
		
		if(records != 0) {
			this.currentPage = 1;
			this.pages = Math.ceil(records / itemsPerPage);
		}
		this.inited = true;
	}

	this.showPageNav = function(pagerName, positionId) {
		if (! this.inited) {
			alert("not inited");
			return;
		}
		var element = document.getElementById(positionId);
		element.innerHTML = "";
		
		if(this.pages > 1) {
			//	var pagerHtml = '<span onclick="' + pagerName + '.prev();" class="pg-normal"> � Prev </span> ';
			var pagerHtml = "<select id='pagerCombo' style='float: right; width : 150px;' onchange='changePager(value)'>" ;
			for (var page = 1; page <= this.pages; page++)  {
				pagerHtml += '<option value="'+page+'">Showing Page No  '+ page +'</option>';
				//pagerHtml += '<span id="pg' + page + '" class="pg-normal" onclick="changePager(' + page + ');">' + page + '</span> ';
			}
			//pagerHtml += '<span onclick="'+pagerName+'.next();" class="pg-normal"> Next �</span>';
			
			pagerHtml += "</select>";
			element.innerHTML = pagerHtml;
		}
		
	} 
}
function getXMLHttpRequest() {
	var xmlHttpReq = false;
	// to create XMLHttpRequest object in non-Microsoft browsers
	if (window.XMLHttpRequest) {
		xmlHttpReq = new XMLHttpRequest();
	} else if (window.ActiveXObject) {
		try {
			// to create XMLHttpRequest object in later versions of Internet Explorer
			xmlHttpReq = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (exp1) {
			try {
				// to create XMLHttpRequest object in older versions of Internet Explorer
				xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (exp2) {
				xmlHttpReq = false;
			}
		}
	}
	return xmlHttpReq;
}

function changePager(pageNumber) {
	if(pageNumber != pager.currentPage) {
		if(isConditionalSearch) {
			searchSpecificRecord(pageNumber , recordsPerPage);
		} else {
			findAllRecord(pageNumber , recordsPerPage);
		}
	}
}

function getReadyStateHandle(xmlHttpRequest) {
	return function() {
		if (xmlHttpRequest.readyState == 4) {
			if (xmlHttpRequest.status == 200) {
				
				var tableHtmlbegin = "<table  id='displayRow' class='yui table'>";
				
				//document.getElementById("displayRow").innerHTML = "";
				document.getElementById("outerTableDiv").innerHTML = "";
				
				var dataRead = JSON.parse(xmlHttpRequest.responseText);
				var htmlStr1 = "";
				var htmlStrTableHeader = "";
				document.getElementById("outerTableDiv").innerHTML = "";
				if(dataRead.parentList.length > 0) {
					document.getElementById('gridContainer').className="visibleTable";
					//Creating the headers for the table.
					for( var i = 0; i < dataRead.displayList.length; i++) {
						var label = dataRead.displayList[i];
					    var html1 = '<td style="text-align: left;"><b>'+label+'</b></td>';
					    htmlStr1 = htmlStr1+html1;
					}
					
					//Appending the Update and Delete Headers to the Table as the last two column headers.
					//var html2 = '<td><b>Update</b></td><td><b>Delete</b></td>';
					var html2 = '<td colspan=2><b>Actions</b></td>';
					htmlStrTableHeader = '<tr>'+htmlStr1+html2+'</tr>';
					
					var htmlStrTableContent = "";
					
					//In this for loop iterate number of content rows.
					for(var i = 0; i < dataRead.parentList.length; i++) {
						var strColumn = "";
						var id = "";
						//In the for loop below iterating the column values for particular row.
						for(var j=0; j<dataRead.nameList.length ; j++) {
							
							var valueName = dataRead.nameList[j];
							var newr = dataRead.parentList[i];
							if(j == 0){
								id =  newr[valueName];
							} else {
								var coljs = '<td>'+ newr[valueName]  + '</td>';
								strColumn = strColumn + coljs;
							}
						}
						var updateColStr = '<td><a href="'+dataRead.updateAction+'?id='+id+'&requestId='+requestId+'"><img height="20" src="/mdr-src/assets/images/update.png" alt="Edit" ></a></td>' ;
						var deleteColStr = '<td><a onclick="return deleteConfirmation();" href="'+dataRead.deleteAction+'?id='+id+'&requestId='+requestId+'"><img height="20" src="/mdr-src/assets/images/Delete.jpg" alt="Delete" ></a></td>' ;
						
						var htmlTableRow = '<tr>'+strColumn+updateColStr+deleteColStr+'</tr>';
						
						htmlStrTableContent = htmlStrTableContent+htmlTableRow;
					}
					
					var tableHtmlend = "</table>";
					
					document.getElementById("outerTableDiv").innerHTML = tableHtmlbegin+htmlStrTableHeader + htmlStrTableContent+tableHtmlend;
					//var pager = new Pager('displayRow', 20);
					
					var recordCount = dataRead.recordCount;
					
					pager.init(recordCount);
					pager.showPageNav('pager', 'pageNavPosition');
					pager.showPage(pageNo);
					
					document.getElementById("pageNavPosition").className = "visibleTable";
				} else {
					document.getElementById('pageNavPosition').className = 'inVisibleTable';
					alert('No result found for this search.');
				}
				//appendToLinks();
			}
		}
	};
}

function deleteConfirmation(value) {
	return confirm("Are you sure you want to delete this record?");
}

function sendToPage() {
	var link = document.getElementById("createPageURL").value;
	document.getElementById("mainForm").action = link;
	document.getElementById("mainForm").submit();
}

function findAllRecord(pageNumber , recordsPerPage) {
	var xmlHttpRequest = getXMLHttpRequest();

	var tableName = document.getElementById("fullyQualifiedVOName").value;
	console.log(tableName);
	pagerParamStr = "&pageNumber="+ pageNumber +"&recordsPerPage="+recordsPerPage;
	
	xmlHttpRequest.onreadystatechange = getReadyStateHandle(xmlHttpRequest);
	xmlHttpRequest.open("POST", "searchAction.action?requestId="+ requestId + "&tableName=" + tableName +pagerParamStr,  true);
	xmlHttpRequest.setRequestHeader("Content-Type",
				"application/x-www-form-urlencoded");
	xmlHttpRequest.send();
	isConditionalSearch = false;
	pageNo = pageNumber;
}
