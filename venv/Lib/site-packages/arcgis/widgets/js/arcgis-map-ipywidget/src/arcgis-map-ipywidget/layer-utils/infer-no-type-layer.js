var getEsriLoader = require("../loaders/get-esri-loader");
var inferRenderer = require("../renderer-utils/infer-renderer");
var rendererTypesUtil = require("../renderer-utils/renderer-types-util");
var createDefaultPopup = require("../popup-utils/create-default-popup");
var config = require("config");
var esriLoader = getEsriLoader(config);
var options = config.EsriLoaderOptions;

var _uuid4 = function() {
      return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, 
          function(c) {
            var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
          });
}

var inferNoTypeLayer = function(noTypeLayer, widget){
    ///Take a generic object, constructs the correct layer type, returns
    //a promise that let's you use the typedLayer this func constructs.
    //For example: if you have an untyped layer (generic js object) like:
    //var foo = {type: "FeatureLayer", url: "https://arcgis.com/..."}
    //You can use this function like this:
    //inferNoTypeLayer(foo).then((typedLayer) => 
    //    {//typedLayer is an instance of type FeatureLayer })
    //TODO: put logic for major layer types here (i.e., FeatureLayer) in 
    //their own JS file
    return new Promise(function(resolve, reject) {
        esriLoader.loadModules(['esri/layers/ImageryLayer',
                                'esri/layers/KMLLayer',
                                'esri/layers/TileLayer',
                                'esri/layers/MapImageLayer',
                                'esri/layers/VectorTileLayer',
                                'esri/layers/SceneLayer',
                                'esri/layers/FeatureLayer',
                                'esri/tasks/support/FeatureSet',
                                'esri/layers/WMSLayer',
                                'esri/layers/WMTSLayer',
                                'esri/layers/GeoRSSLayer',
                                'esri/layers/GeoJSONLayer',
                                'esri/layers/CSVLayer',
                                'esri/layers/support/RasterFunction',
                                'esri/layers/support/MosaicRule',
                                'esri/layers/PointCloudLayer',
                                'esri/layers/IntegratedMeshLayer',
                                'esri/layers/BuildingSceneLayer',
                                'esri/layers/ImageryTileLayer'],
        options).then(([ImageryLayer,
                        KMLLayer,
                        TileLayer,
                        MapImageLayer,
                        VectorTileLayer,
                        SceneLayer,
                        FeatureLayer,
                        FeatureSet,
                        WMSLayer,
                        WMTSLayer,
                        GeoRSSLayer,
                        GeoJSONLayer,
                        CSVLayer,
                        RasterFunction,
                        MosaicRule,
                        PointCloudLayer,
                        IntegratedMeshLayer,
                        BuildingSceneLayer,
                        ImageryTileLayer]) => {
            if (noTypeLayer.type === "ImageryLayer"){
                if (('capabilities' in noTypeLayer) &&
                    (noTypeLayer.capabilities == "tilesOnly")){
                        var typedLayer = new ImageryTileLayer(noTypeLayer.url);
                        typedLayer.id = noTypeLayer._hashFromPython;
                    }
                else {
                    var typedLayer = new ImageryLayer(noTypeLayer.url);
                    typedLayer.id = noTypeLayer._hashFromPython;
                    if (('options' in noTypeLayer) && 
                        ('imageServiceParameters' in noTypeLayer.options)){
                        if('renderingRule' in noTypeLayer.options.imageServiceParameters){
                            console.log("Applying rendering rule to imagery layer..");
                            var renderingRuleJSON = 
                                noTypeLayer.options.imageServiceParameters.renderingRule;
                            var renderingRule = RasterFunction.fromJSON(renderingRuleJSON);
                            typedLayer.renderingRule = renderingRule;}
                        if('mosaicRule' in noTypeLayer.options.imageServiceParameters){
                            console.log("Applying mosaic rule to imagery layer..");
                            var mosaicRuleJSON = 
                                noTypeLayer.options.imageServiceParameters.mosaicRule;
                            var mosaicRule = MosaicRule.fromJSON(mosaicRuleJSON);
                            typedLayer.mosaicRule = mosaicRule;}
                        if ('raster' in noTypeLayer.options.imageServiceParameters) {
                            var raster =
                                noTypeLayer.options.imageServiceParameters.raster;
                            var encodedRaster;
                            if (typeof raster == "string") {
                                encodedRaster = raster;
                            }
                            else {
                                encodedRaster =
                                    btoa(JSON.stringify(raster));
                            }
                            typedLayer.raster = encodedRaster;
                        }
                    }
                }
                resolve(typedLayer);}
            else if (noTypeLayer.type == "KMLLayer" || noTypeLayer.type == "KML") {
                var typedLayer = new KMLLayer(noTypeLayer.url);
                typedLayer.id = noTypeLayer._hashFromPython;
                resolve(typedLayer);}
            else if ((noTypeLayer.type == "ArcGISTiledMapServiceLayer") ||
                     (noTypeLayer.type == "TileLayer")){
                //Renamed in 4.X
                var typedLayer = new TileLayer(noTypeLayer.url);
                typedLayer.id = noTypeLayer._hashFromPython;
                resolve(typedLayer);}
            else if ((noTypeLayer.type == "ArcGISDynamicMapServiceLayer") ||
                     (noTypeLayer.type == "MapImageLayer" )){
                //renamed in 4.X
                var typedLayer = new MapImageLayer(noTypeLayer.url);
                typedLayer.id = noTypeLayer._hashFromPython;
                resolve(typedLayer)}
            else if (noTypeLayer.type == "VectorTileLayer") {
                var typedLayer = new VectorTileLayer(noTypeLayer.url);
                typedLayer.id = noTypeLayer._hashFromPython;
                resolve(typedLayer);}
            else if (noTypeLayer.type == "WMS"){
                noTypeLayer.subLayers = [noTypeLayer.sublayers[0],];
                delete noTypeLayer.type;
                var typedLayer = new WMSLayer(noTypeLayer);
                typedLayer.id = noTypeLayer._hashFromPython;
                resolve(typedLayer);}
            else if (noTypeLayer.type == "WebTiledLayer"){
                var typedLayer = new WMTSLayer({url : noTypeLayer.url});
                typedLayer.id = noTypeLayer._hashFromPython;
                resolve(typedLayer);}
            else if (noTypeLayer.type == "GeoRSS"){
                var typedLayer = new GeoRSSLayer({url: noTypeLayer.url});
                typedLayer.id = noTypeLayer._hashFromPython;
                resolve(typedLayer);}
            else if (noTypeLayer.type == "GeoJSON"){
                if(Object.keys(noTypeLayer.data).length !== 0){
                    var blob = new Blob([JSON.stringify(noTypeLayer.data)],
                                        {type: "application/json"});
                    url = URL.createObjectURL(blob);}
                else{
                    url = noTypeLayer.url;}
                var typedLayer = new GeoJSONLayer({url: url});
                typedLayer.id = noTypeLayer._hashFromPython;
                if("renderer" in noTypeLayer){
                    console.log("Using custom renderer for GeoJSON layer " + 
                                typedLayer.id);
                    inferRenderer(noTypeLayer.renderer.type,
                                  noTypeLayer.renderer).then((renderer) => {
                        typedLayer.renderer = renderer;
                        resolve(typedLayer);
                    }).catch((err) => {
                        console.warn("Could not infer renderer for " + 
                                     typedLayer.id);
                        console.warn(err);
                        resolve(typedLayer);
                    });
                } else {
                    resolve(typedLayer);}}
            else if (noTypeLayer.type == "CSV"){
                inferRenderer(noTypeLayer.layerDefinition.drawingInfo.renderer.type,
                    noTypeLayer.layerDefinition.drawingInfo.renderer).then((renderer) => {
                    var typedLayer = new CSVLayer({url: noTypeLayer.url,
                                                   renderer: renderer});
                    typedLayer.id = noTypeLayer._hashFromPython;
                    resolve(typedLayer);
                }).catch((err) => {
                    var typedLayer = new CSVLayer({url: noTypeLayer.url});
                    typedLayer.id = noTypeLayer._hashFromPython;
                    resolve(typedLayer);})}
            else if (noTypeLayer.type == "SceneLayer"){
                var typedLayer = new SceneLayer({url: noTypeLayer.url});
                typedLayer.id = noTypeLayer._hashFromPython;
                resolve(typedLayer);}
            else if (noTypeLayer.type == "PointCloudLayer"){
                var typedLayer = new PointCloudLayer({url: noTypeLayer.url});
                typedLayer.id = noTypeLayer._hashFromPython;
                resolve(typedLayer);}
            else if (noTypeLayer.type == "IntegratedMeshLayer"){
                var typedLayer = new IntegratedMeshLayer({url: noTypeLayer.url});
                typedLayer.id = noTypeLayer._hashFromPython;
                resolve(typedLayer);}
            else if (noTypeLayer.type == "BuildingSceneLayer"){
                var typedLayer = new BuildingSceneLayer({url: noTypeLayer.url});
                typedLayer.id = noTypeLayer._hashFromPython;
                resolve(typedLayer);}
            else if ((noTypeLayer.type == "FeatureLayer") ||
                     (noTypeLayer.type == "Feature Layer")) {
                //TODO: clean up this Feature layer stuff, seperate into new file
                
                //Create the base FeatureLayer
                var unloadedLayer = new FeatureLayer(noTypeLayer.url, {
                    "outFields": ["*"]});
                unloadedLayer.id = noTypeLayer._hashFromPython;
                unloadedLayer.load().then((layer) => {

                    layer.popupTemplate = createDefaultPopup(layer);

                    //Find out where any extra options are located, set them to lyr_options
                    var lyr_options = {}
                    if (noTypeLayer.options == null) {
                        lyr_options = noTypeLayer;}
                    else{
                        lyr_options = noTypeLayer.options;}

                    //Figure out if those options specify opacity and definition_expression
                    if (lyr_options.opacity != null) {
                        console.log('FeatureLayerOpacity:' + lyr_options.opacity);
                        layer.opacity = lyr_options.opacity;}
                    if (noTypeLayer.opacity != null) {
                        layer.opacity = noTypeLayer.opacity;}
                    if (lyr_options.definition_expression != null) {
                        console.log("FeatureLayerDefinitionExpression:");
                        console.log(lyr_options.definition_expression);
                        layer.definitionExpression = lyr_options.definition_expression;}
                    if (noTypeLayer.definition_expression != null) {
                        console.log("FeatureLayerDefinitionExpression:");
                        console.log(noTypeLayer.definition_expression);
                        layer.definitionExpression = noTypeLayer.definition_expression;}

                    //Figure out the renderer
                    if (!lyr_options.renderer) {
                        resolve(layer);
                    } else { 
                        console.log("Specifying the FeatureLayer's custom renderer...");
                        var renderer = "";
                        var rendererOptions = {};
                        if(rendererTypesUtil.isSmartMapRenderer(lyr_options.renderer)){
                            //TODO: Clean up this section, seperate out into own file
                            rendererOptions = {layer: layer,
                                               fieldName: lyr_options.field_name,
                                               basemap: widget.model.get("basemap"),
                                               otherLayerOptions: lyr_options };
                        } else {
                            rendererOptions = lyr_options;
                        }

                        //At this point, lyr_options.renderer should be a string
                        //If instead the user passed in the whole object as the 
                        //'renderer', assemble 'renderer' and 'rendererOptions' correctly
                        if((typeof lyr_options.renderer != 'string') && 
                           ("type" in lyr_options.renderer)) {
                            renderer = lyr_options.renderer.type;
                            rendererOptions = lyr_options.renderer;
                        } else {
                            renderer = lyr_options.renderer;
                        }

                        inferRenderer(renderer, rendererOptions,
                        widget).then((renderer) => {
                            layer.renderer = renderer;
                            resolve(layer);
                        }).catch((err) => {
                            console.warn("Error on inferring renderer.");
                            reject(err);})}}
                ).catch((err) => {
                    console.warn("Error when laoding Feature Layer");
                    reject(err);
                })
            } else if('featureSet' in noTypeLayer){
                ///This is a catch for FeatureCollections
                ///TODO: Seperate this out into its own file,
                ///have the result of this stored in it's own widget model
                console.log("Creating from FeatureCollection...");

                //convert all esriJSON to correct 4.X JSON via fromJSON
                var layerDefinition = noTypeLayer.layerDefinition;
                var esriJSONFS = noTypeLayer.featureSet;
                esriJSONFS.spatialReference = layerDefinition.spatialReference;
                esriJSONFS.fields = layerDefinition.fields;
                var featureSet = FeatureSet.fromJSON(esriJSONFS);

                //Assemble everything from the featureLayer BUT the renderer
                var typedLayer = new FeatureLayer({
                    title: _uuid4(), 
                    fields: featureSet.fields,
                    objectIdField: layerDefinition.objectIdField,
                    geometryType: featureSet.geometryType,
                    spatialReference: featureSet.spatialReference,
                    source: featureSet.features})
                typedLayer.popupTemplate = createDefaultPopup(typedLayer);
                typedLayer.id = noTypeLayer._hashFromPython;

                //Get the correct renderer and rendererOptions to
                if("renderer" in noTypeLayer.options){
                    renderer = noTypeLayer.options.renderer;
                } else if(layerDefinition.drawingInfo.renderer.renderer === "autocast"){
                    renderer = "autocast";
                } else {
                    renderer = layerDefinition.drawingInfo.renderer.type;
                }
                if(rendererTypesUtil.isSmartMapRenderer(renderer)){
                    rendererOptions = { layer: typedLayer,
                                        fieldName: noTypeLayer.options.field_name,
                                        basemap: widget.model.get("basemap"),
                                        otherLayerOptions: noTypeLayer.options };
                } else {
                    rendererOptions = layerDefinition.drawingInfo.renderer;
                }

                //Infer the renderer from the above info, add to layer, resolve
                inferRenderer(renderer, rendererOptions, widget).then(
                (renderer) => {
                        typedLayer.renderer = renderer;
                        resolve(typedLayer);
                    }).catch((err) => {
                        console.warn("Error on inferring renderer.");
                        reject(err);});}
            else{
                console.warn('This layer type is not supported:');
                console.warn(noTypeLayer);
                reject("This layer type is not supported.");}
       }).catch((err) => {
            reject(err);
        });
    });
}

module.exports = inferNoTypeLayer;
