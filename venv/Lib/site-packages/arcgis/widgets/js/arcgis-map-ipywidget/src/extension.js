// This file contains the javascript that is run when the notebook is loaded.
// It contains some requirejs configuration and the `load_ipython_extension`
// which is required for any notebook extension.

// Add Esri Javascript from CDN:

//$('body').append('<link rel="stylesheet" href="https://js.arcgis.com/4.7/esri/css/main.css"><script src="https://js.arcgis.com/4.7/"></script>');

// Configure requirejs

var config = require("config");
var getEsriLoader = require("./arcgis-map-ipywidget/loaders/get-esri-loader")
var esriLoader = getEsriLoader(config);

__webpack_public_path__ = document.querySelector('body').getAttribute('data-base-url') + 'nbextensions/arcgis-map-ipywidget';

var _httpGetAsync = function(theUrl){
    return new Promise((resolve, reject) => {
        fetch(theUrl, {mode: 'cors'}).then((response) => {
            if (response.status >= 200 && response.status < 300){
                response.text().then((data) => {
                    resolve(data);
                }).catch((err) => {
                    reject(err);
                });
            } else {
                reject("HTTP request on " + theUrl + 
                       " returned code " + status);
            }
        }).catch((err) => {
            reject(err);
        });
    })
}

if (window.require) {
    _httpGetAsync(config.CdnUrl).then((data) => {
        //We can reach the CdnUrl: We aren't in a disconected environment
        esriLoader.setRequireJSConfig(config.BaseRequireJSConfig);
        console.log("Initializing esriLoader for quicker load times...");
        //Use the esri-loader here on notebook load: will make subsequent loads quicker
        esriLoader.loadModules(['esri/Map',
                                'esri/views/MapView',
                                'esri/views/SceneView',
                                'esri/layers/Layer'],
                                config.EsriLoaderOptions).then((
                                    [Map,
                                     MapView,
                                     SceneView,
                                     Layer]) => {
            console.log("esriLoader initialization completed successfully!");
        }).catch((err) => {
            console.log("esriLoader initialization ran into an error:");
            console.log(err);
        })
    }).catch((err) => {
        console.log("Cannot reach " + config.CdnUrl + ": Not pre-loading, " +
                    "waiting for user to specify the proper CDN path");
    });
}

// Export the required load_ipython_extension
module.exports = {
    load_ipython_extension: function() {}
};
