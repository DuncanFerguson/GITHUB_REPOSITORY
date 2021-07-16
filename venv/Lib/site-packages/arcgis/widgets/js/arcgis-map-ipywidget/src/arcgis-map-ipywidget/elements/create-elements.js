/*All elements that either contain the widget or add onto it*/
var loadingProgress = require("./loading-progress-display");
var config = require("config");
var images = require("../images/images");

var createElements = function(uuid){
    //The parent 'viewElement' that contains the map, info, etc.
    var viewdivElement = document.createElement("div");
    viewdivElement.className = "viewDiv";
    viewdivElement.id = viewdivElement.className + uuid;
    viewdivElement.style.padding = "0";
    viewdivElement.style.margin = "0";
    viewdivElement.style.height = "100%";
    viewdivElement.style.width = "100%";
    viewdivElement.style.position = "relative";

    //The information element (note: I don't see this on the widget)
    var infodivElement = document.createElement("div");
    infodivElement.className = "infoDiv";
    infodivElement.id = infodivElement.className + uuid;
    infodivElement.style.position = "absolute";
    infodivElement.style.top = "15px";
    infodivElement.style.left = "60px";

    //The button that allows you to switch from 2D to 3D
    var switchButton   = document.createElement("input");
    switchButton.classList.add('switchButtonId');
    switchButton.id = 'switchButton' + uuid;
    switchButton.type = "image";
    switchButton.classList.add("esri-component");
    switchButton.classList.add("esri-widget--button");
    switchButton.classList.add("esri-widget"); 
    switchButton.classList.add("esri-interactive");
    switchButton.style.boxShadow = "rgba(0, 0, 0, 0.3) 0px 1px 2px";
    switchButton.style.border = "none";
    switchButton.style.float = "left";
    switchButton.style.marginRight = "13px";

    if(config.JupyterTarget === "lab"){
        var newWindowButton   = document.createElement("input");
        newWindowButton.classList.add('newWindowButton');
        newWindowButton.id = 'newWindowButtonId' + uuid;
        newWindowButton.type = "image";
        newWindowButton.src = images.toNewWindowEncoded;
        newWindowButton.classList.add("esri-component");
        newWindowButton.classList.add("esri-widget--button");
        newWindowButton.classList.add("esri-widget"); 
        newWindowButton.classList.add("esri-interactive");
        newWindowButton.style.boxShadow = "rgba(0, 0, 0, 0.3) 0px 1px 2px";
        newWindowButton.style.fontFamily ='CalciteWebCoreIcons';
        newWindowButton.style.border = "none";
        newWindowButton.style.float = "right";
        newWindowButton.style.marginRight = "13px"; 

        newWindowButton.style.width = "32px";
        newWindowButton.style.height = "32px";
        newWindowButton.style.textAlign = "center";
        newWindowButton.style.margin = "0 10px 10px 0";
        newWindowButton.style.fontSize = "125%";

    }
    //The loading text element
    var loadingText = loadingProgress.element;
    loadingText.className = "loadingText";
    loadingText.id = loadingText.className + uuid;

    //A generic information text box that shows error info (manually styled to match map widget)
    var errorTextBox = document.createElement("div");
    errorTextBox.className = 'errorTextDiv';
    errorTextBox.id = errorTextBox.className + uuid;
    errorTextBox.style.position = "absolute";
    errorTextBox.style.right = "5px";
    errorTextBox.style.top = "5px";
    errorTextBox.style.width = "25%";
    errorTextBox.style.color = "#6f6f6f"
    errorTextBox.style.backgroundColor = "#ffffff";
    errorTextBox.style.boxShadow = "rgba(0, 0, 0, 0.3) 0px 1px 2px";
    errorTextBox.style.fontFamily = "sans-serif";
    errorTextBox.style.fontWeight = "400";
    errorTextBox.style.wordWrap = "break-word";
    var errorCloseButton = document.createElement("div");
    errorCloseButton.className = "errorCloseButton";
    errorCloseButton.id = errorCloseButton.className + uuid;
    errorCloseButton.style.position = "absolute";
    errorCloseButton.style.top = "3px";
    errorCloseButton.style.right = "9px";
    errorCloseButton.style.color = "#ababab";
    errorCloseButton.style.fontFamily = "sans-serif";
    errorCloseButton.style.fontWeight = "400";
    errorTextBox.appendChild(errorCloseButton);
    var clearAllText = function() {
        errorTextBox.textContent = "";
        errorCloseButton.textContent = "";
        errorTextBox.style.padding = "0px";
    };
    errorTextBox.onclick = clearAllText;
    errorCloseButton.onclick = clearAllText;

    //The actual map element
    var mapElement     = document.createElement("div");
    mapElement.className = "mapElement";
    mapElement.id = mapElement.className + uuid;
    mapElement.style.height = "100%";
    mapElement.style.width = "100%";

    //Establish parent/child relationships
    viewdivElement.appendChild(loadingText);
    viewdivElement.appendChild(mapElement);
    viewdivElement.appendChild(infodivElement);
    viewdivElement.appendChild(errorTextBox);
    viewdivElement.appendChild(errorCloseButton);

    return {
        viewdivElement,
        infodivElement,
        mapElement,
        switchButton,
        errorTextBox,
        errorCloseButton,
        loadingText,
        newWindowButton
    }
}

module.exports = createElements;
