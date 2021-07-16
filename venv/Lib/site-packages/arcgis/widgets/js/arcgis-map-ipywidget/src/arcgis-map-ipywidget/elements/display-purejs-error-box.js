//We want to alert the user using no esri-specific stylings or code, incase
//esri code failed to load
var config = require("config");

var displayPureJSErrorBox = function(msg, elements){
    elements.errorTextBox.textContent = msg;
    elements.errorCloseButton.textContent = "✕";
    elements.errorTextBox.style.padding = "10px";
}

module.exports = displayPureJSErrorBox;
