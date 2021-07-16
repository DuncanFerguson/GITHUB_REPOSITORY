var defaultEsriLoader = require("esri-loader");
var requireJSEsriLoader = require("./requirejs-esri-loader");

function getEsriLoader(config){
    if(!config.JupyterTarget){
        throw "config does not specify 'JupyterTarget'! Failing";
    } else if(config.JupyterTarget === "lab"){
        return defaultEsriLoader;
    } else if(config.JupyterTarget === "notebook") {
        //Jupyter Notebooks use RequireJS for AMD module loading
        //We must use the custom requireJSesri-loader for it to work
        //See ./requirejs-esri-loader.js for more details
        return requireJSEsriLoader;
    } else{
        throw "Misconfigured config file! Failing";
    }
}

module.exports = getEsriLoader;
