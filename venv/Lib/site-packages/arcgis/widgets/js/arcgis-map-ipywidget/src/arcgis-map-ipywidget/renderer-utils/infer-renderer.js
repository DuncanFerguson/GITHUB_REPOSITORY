var getEsriLoader = require("../loaders/get-esri-loader");
var config = require("config");
var esriLoader = getEsriLoader(config);
var options = config.EsriLoaderOptions;
var rendererTypesUtil = require("./renderer-types-util");

var getColorOrSizeProp = function(rendererOptions){
    return Object.assign({
        layer: rendererOptions.layer,
        field: rendererOptions.fieldName,
        basemap: rendererOptions.basemap,
        classificationMethod: "quantile"
        },
        rendererOptions.otherLyrOptions)
}

var inferRenderer = function(renderer, rendererOptions, widget){
    return new Promise(function(resolve, reject) {
        esriLoader.loadModules(["esri/renderers/smartMapping/creators/size",
                                "esri/renderers/smartMapping/creators/color",
                                "esri/renderers/smartMapping/creators/location",
                                "esri/renderers/SimpleRenderer",
                                "esri/renderers/UniqueValueRenderer",
                                "esri/renderers/ClassBreaksRenderer",
                                "esri/renderers/HeatmapRenderer",
                                "esri/renderers/DotDensityRenderer"],
        options).then(([sizeRendererCreator,
                        colorRendererCreator,
                        locationRendererCreator,
                        SimpleRenderer,
                        UniqueValueRenderer,
                        ClassBreaksRenderer,
                        HeatmapRenderer,
                        DotDensityRenderer]) => {
            if(rendererTypesUtil.isClassedSizeRenderer(renderer)){
                console.log("Using classedSizeRenderer...");
                var prop = getColorOrSizeProp(rendererOptions);
                console.log(prop);
                sizeRendererCreator.createClassBreaksRenderer(prop).then((response) => {
                    resolve(response.renderer)
                }).catch((err) => {
                    console.warn("Error on creating Class Breaks Renderer");
                    reject(err);
                });
            } else if(rendererTypesUtil.isClassedColorRenderer(renderer)){
                console.log("Using classedColorRenderer...");
                var prop = getColorOrSizeProp(rendererOptions);
                colorRendererCreator.createClassBreaksRenderer(prop).then((response) => {
                    resolve(response.renderer);
                }).catch((err) => {
                    console.warn("Error on creating Color Renderer");
                    reject(err);
                });
            } else if (rendererTypesUtil.isHeatMapRenderer(renderer)){
                console.log("Using heatmap renderer...");
                resolve(HeatmapRenderer.fromJSON(rendererOptions));
           } else if (rendererTypesUtil.isSimpleRenderer(renderer)){
                console.log("Using simpleRenderer...");
                resolve(SimpleRenderer.fromJSON(rendererOptions));
            } else if (rendererTypesUtil.isUniqueRenderer(renderer)){
                console.log("Using uniqueValueRenderer");
                resolve(UniqueValueRenderer.fromJSON(rendererOptions));
            } else if (rendererTypesUtil.isClassBreaksRenderer(renderer)){
                console.log("Using classBreaksRenderer");
                resolve(ClassBreaksRenderer.fromJSON(rendererOptions));
            } else if (rendererTypesUtil.isDotDensityRenderer(renderer)){
                console.log("Using Dot Density Renderer"); 
                resolve(DotDensityRenderer.fromJSON(rendererOptions));
            } else if (rendererTypesUtil.userSpecifiedAutocastRenderer(renderer)){
                console.log("Autocasting the renderer");
                resolve(rendererOptions);
            } else {
                console.warn("Could not infer renderer type");
                reject("Renderer of type '" + renderer + "' is not supported. ");
            }
        }).catch((err) => {
            console.warn("Error on inferring Renderer");
            reject(err);
        });
    });
}

module.exports = inferRenderer;
