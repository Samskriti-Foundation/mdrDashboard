
function renderDashboard(url, port, prefix, jsonKey) {
    const divMainTableContainer = document.getElementById("mainTableContainer");
    fetch('http://' + url + ':' + port + prefix)
        .then(response => response.json())
        .then(json => {
      dataArray = json[jsonKey];
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
  });
}