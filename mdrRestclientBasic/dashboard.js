function dashboardCounts(jsonKey, prefix) {
  var url = "127.0.0.1";
  var port = "5000";
  return fetch('http://' + url + ':' + port + prefix)
    .then(response => response.json())
    .then(json => {
      const dataArray = json[jsonKey];
      // console.log("dashboard:", prefix, jsonKey, dataArray);
      return dataArray;
    })
    .catch(error => {
      console.error("Error fetching data:", error);
      return null; // Return null in case of error
    });
}
function totalthem(dataArrays) {
  totals = {Manuscripts:0, Books:0, Articles:0, Users:0};
  dataArrays.forEach(function (arrayItem) {
    Object.entries(arrayItem).forEach(([key, value]) => {
      totals[key] += value;
    });
  });
  return totals;
}

function render(dataArray) {
  const divMainTableContainer = document.getElementById("mainTableContainer");
  const divTblContainer = document.createElement("div");
  divTblContainer.id = "tableContainer";
  divTblContainer.className = "metro-nav metro-fix-view";
  total = 0;
    Object.entries(dataArray).forEach(([key, value]) => {
    divInnerTableContainer =  document.createElement("div");
    divInnerTableContainer.className = "metro-nav-block nav-block-purple";
    element_i = document.createElement("i");
    element_i.className = "glyphicon glyphicon-file";
    if (key=="Users") element_i.className = "glyphicon glyphicon-user";
        else {element_i.className = "glyphicon glyphicon-file"; total += value;}
    divInfo =  document.createElement("div");
    divInfo.className = "info";
    divInfo.innerHTML = value;
    divStatus = document.createElement("div");
    divStatus.className = "status";
    divStatus.innerHTML = key;
    divInnerTableContainer.appendChild(divStatus);
    divInnerTableContainer.appendChild(element_i);
    divInnerTableContainer.appendChild(divInfo);
    divTblContainer.appendChild(divInnerTableContainer);
});
divInnerTableContainer =  document.createElement("div");
divInnerTableContainer.className = "metro-nav-block nav-block-purple";
divInfo =  document.createElement("div");
divInfo.className = "info";
divInfo.innerHTML = total;
divStatus = document.createElement("div");
divStatus.className = "status";
divStatus.innerHTML = "Documents";
element_i = document.createElement("i");
element_i.className = "glyphicon glyphicon-file";
divInnerTableContainer.appendChild(divStatus);
divInnerTableContainer.appendChild(element_i);
divInnerTableContainer.appendChild(divInfo);
divTblContainer.appendChild(divInnerTableContainer)
divMainTableContainer.appendChild(divTblContainer);
}