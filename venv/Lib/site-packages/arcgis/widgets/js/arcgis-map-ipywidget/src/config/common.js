var CdnUrl = "https://js.arcgis.com/4.19/";

var CdnMainCssUrl = CdnUrl + "esri/css/main.css";

var EsriLoaderOptions = {
    url: CdnUrl,
    dojoConfig: {
        has: {
            "esri-featurelayer-webgl": 1
        }
    }
}

var minJSAPIVersion = "4.19";

var config = {
    CdnUrl,
    CdnMainCssUrl,
    EsriLoaderOptions,
    minJSAPIVersion
};

module.exports = config;
