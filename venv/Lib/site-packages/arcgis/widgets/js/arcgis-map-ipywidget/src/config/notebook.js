var config = require("./common");
var configureCdn = require("./configure-cdn");

// This logic constructs the base URL where the nbextensions widgets are stored.
// This is located at http://<host>:<port>/nbextensions/arcgis/ for any jupyter
// notebook server. When you are accessing notebooks through this server 
// directly, the base URL should be "/nbextensions/arcgis/". When accessing a
// notebook through ArcGIS Hosted Notebooks, the jupyter server is accessed
// indirectly, so extra steps are needed. A notebook is at a URL like this:
// https://<host>:<port>/<webadaptor>/notebooks/<32_char_uuid>/notebooks/file.ipynb
// for an enterprise setup. An AGOL setup has a URL like this:
// https://<host>:<port>/<32_char_uuid>/notebooks/file.ipynb
// For both of the AGOL/enterprise use cases, the nbextensions location is 
// located AFTER the <32_char_uuid> hexadecimal string.
// (ex. https://<host>:<port>/<32_char_uuid>/nbextensions/)

var jupyterBase = "/";
if(/\/[0-9A-Fa-f]{32}\/notebooks\//.test(location.pathname)){
    // We are in a hosted notebooks environment
    try{
        jupyterBase = location.pathname.match(
            /.*\/[0-9A-Fa-f]{32}\/(?=notebooks\/)/)[0];}
    catch (e){}
}
var nbextensionPath = jupyterBase + "nbextensions/arcgis/";
console.log("nbextension path = " + nbextensionPath);

config.JSOutputContext = "default";
config.JupyterTarget = "notebook"; 
config.BaseRequireJSConfig = {
    map : {
        "*" : {
            "arcgis-map-ipywidget": nbextensionPath + "arcgis-map-ipywidget.js",
            "legacy-mapview": nbextensionPath + "legacy-mapview.js"
        },
    },
    config : {
            has: {
              "esri-featurelayer-webgl": 1
            },

            geotext: {

            useXhr: function(url) {
                // Allow cross domain XHR requests:
                // We will route them through a proxy in onXhr below.
                // https://github.com/requirejs/text/blob/master/text.js#L129

                return true;
            },

            // In IE 9, text plugin fails even before onXhr is called:
            // It fails right when calling xhr.open:
            // https://github.com/requirejs/text/blob/master/text.js#L267
            // - This is different from other browsers which appear to fail
            // much later, allowing us a chance to append proxy below.
            // -- Probably because IE 9 does not support CORS as opposed to
            // other modern browsers that have CORS support.

            // ESRI modification: let's take over xhr.open below
            openXhr: false,

            onXhr: function(xhr, url) {
                // Route cross domain XHR through a proxy if required
                var hasCors = (
                typeof XMLHttpRequest !== "undefined"
                && ("withCredentials" in (new XMLHttpRequest()))
                );

                xhr.open(
                "GET",
                hasCors ? url : (proxyUrl + "?" + url),
                true
                );
            }
        }
    }
};
configureCdn(config, config.CdnUrl);

module.exports = config;
