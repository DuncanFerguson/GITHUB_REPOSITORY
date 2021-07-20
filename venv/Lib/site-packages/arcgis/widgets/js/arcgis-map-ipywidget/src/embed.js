// Entry point for the unpkg bundle containing custom model definitions.
//
// It differs from the notebook bundle in that it does not need to define a
// dynamic baseURL for the static assets and may load some css that would
// already be loaded by the notebook otherwise.

// Export widget models and views, and the npm package version number.
require('./extension');

var config = require("config");
var getEsriLoader = require('./arcgis-map-ipywidget/loaders/get-esri-loader');
var esriLoader = getEsriLoader(config);
esriLoader.setRequireJSConfig(config.BaseRequireJSConfig);

module.exports = require('./arcgis-map-ipywidget/arcgis-map-ipywidget.js');
module.exports['version'] = require('../package.json').version;
