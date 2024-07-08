

function getAuthorField() {
	var authorCount = $('#authorBox').children().size();
	var isBlankAuthor= false;
//alert('inside the method');
	
	/*var tr = "<div class='author-search alert alert-success' style='height:90;background-color: #EEE; border-color: #404040;'>"+
	"<div class'form-group row'>"+
		"<div class='col-md-4'>"+
			"<label class='control-label'>Search By Name</label>"+
			"<span class='glyphicon glyphicon-info-sign labelInfo' style='color: red;'"+
  				"data-toggle='popover' data-content='Type the first letters of the Author's name in the auto complete field and the  related records will be fetched if present and then select the author's name you want to refer.Otherwise click on"+ 
  				"ADD NEW RECORD and add a new author.'></span></div>"+
		"<div class='col-md-6'>"+
		    "<input type='text' name='' autocomplete='off' cssClass='form-control ui-autocomplete-input' id='authorSearch' maxlength='50' placeholder='Autocomplete Field..'/>"+
		"</div>"+
		"<div class='col-md-2'>"+
			  "<input type='button' class='btn btn-lg btn-success btn-block' value='new' id='add-author'>"+
			  "</div></div></div>";*/
	for(var i=0;i<authorCount;i++){
		if($('#authorId'+i).val().trim()=="" && $('#authorName'+i).val().trim()== ""){
			isBlankAuthor = true;
		}
	}
	
	if(isBlankAuthor){
		alert("A set of blank Author fields is already available");
	}else{
	var authorTr = 
		"<div id='authordiv"+authorCount+"'>" +
		"<div class='authorheaderspan headerAuth"+authorCount+"'><span>Author[+]</span></div>"+
		"<div class='containerAuth author-data' style='border: thin solid #404040;'  id='authorDivId"+authorCount+"'><br>"+
	  "<div class='form-group row'>"+
        "<label class='col-md-4 control-label'>Name</label>"+
        "<div class='col-md-8'>"+
            "<input type='text' class='form-control' id='authorName"+authorCount+"' name='digitalManuscriptVO.authors["+authorCount+"].name' maxlength='255'/>"+
            "<input type='hidden' id='authorId"+authorCount+"' name='digitalManuscriptVO.authors["+authorCount+"].id'/>"+
        "</div>"+
    "</div>"+
    
    "<div class='form-group row'>"+
        "<label class='col-md-4 control-label'>Name (in Diacritical)</label>"+
        "<div class='col-md-8'>"+
            "<input type='text' class='form-control' id='authorDiacriticName"+authorCount+"' name='digitalManuscriptVO.authors["+authorCount+"].diacriticName' maxlength='250' placeholder='Multilingual field..'/>"+
        "</div>"+
    "</div>"+
    
    "<div class='form-group row'>"+
        "<label class='col-md-4 control-label'>Name (in Vernacular)</label>"+
        "<div class='col-md-8'>"+
            "<input type='text' class='form-control' id='authorRegionalName"+authorCount+"' name='digitalManuscriptVO.authors["+authorCount+"].regionalName' maxlength='250' placeholder='Multilingual field..'/>"+
        "</div>"+
    "</div>"+
    "<div class='form-group row'>"+
    	  "<div class='col-md-12'>"+
	      	  "<div class='alert alert-warning validation-warning' style='border-color: #d88a25;'>"+
	      	  	  "<h6>Tip : You must enter at least one of the three form fields (ie. name, regional name, diacritical name)</h6>"+
			  "</div>"+
    	  "</div>"+
    "</div>"+
    "<div class='form-group row'>"+
        "<label class='col-md-4 control-label'>Period of the author</label>"+
        "<div class='col-md-6'>"+
            "<input type='text' class='form-control' id='authorPeriod"+authorCount+"' name='digitalManuscriptVO.authors["+authorCount+"].period' maxlength='100'/>"+
        "</div>"+
        "<div class='col-md-2'>"+
            "<s:select list='#{'AD':'AD', 'BC':'BC'}' name='digitalManuscriptVO.authors["+authorCount+"].periodEra' "+ 
            	"value='digitalManuscriptVO.authors["+authorCount+"].periodEra' cssClass='form-control' id='periodEra"+authorCount+"'/>"+
        "</div>"+
    "</div>"+
    "<div class='form-group row'>"+
        "<label class='col-md-4 control-label'>Author's Biography</label>"+
        "<div class='col-md-8'>"+
            "<input type='text' class='form-control' name='digitalManuscriptVO.authors["+authorCount+"].lifeHistory' id='authorLifeHistory"+authorCount+"' maxlength='3000'/>"+
        "</div>"+
    "</div>"+
"</div></div>";

	//$('#authorBox').empty();
	$('#authorBox').prepend(authorTr);
//	$('#authorBox').append(odlContent);
	
	var authorDivClass = '.headerAuth'+authorCount;
	$(authorDivClass).click(function () {
		$('#authorDiacriticName'+authorCount).ime();
		$('#authorRegionalName'+authorCount).ime();
	    $header = $(this);
	    //getting the next element
	    $content = $header.next();
	    //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
	    $content.slideToggle(500, function () {
	        //execute this after slideToggle is done
	        //change text of header based on visibility of content div
	        $header.text(function () {
	            //change text based on condition
	            return $content.is(":visible") ? "Author[-]" : "Author[+]";
	        });
	    });

	});
	$(authorDivClass).click();
	}
	
}