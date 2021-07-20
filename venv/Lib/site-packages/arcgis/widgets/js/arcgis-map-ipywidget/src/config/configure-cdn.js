var configureCDN = function(config, cdn){
    ///Takes in an existing config, updates the mainCDN and fallbackCDN for
    ///Jupyter notebook configuration (Jupyterlab configuration just uses
    ///the main CDNUrl defined in the 'esriLoaderOptions' var of the config
    config.CdnUrl = cdn;
    config.EsriLoaderOptions.url = config.CdnUrl
    if (config.JupyterTarget === "notebook"){
        config.BaseRequireJSConfig.packages = 
           [{ name: "esri", location: config.CdnUrl + "esri" },
            { name: "dojo", location: config.CdnUrl + "dojo" },
            { name: "dojox", location: config.CdnUrl + "dojox" },
            { name: "dijit", location: config.CdnUrl + "dijit" },
            { name: "dstore", location: config.CdnUrl + "dstore" },
            { name: "moment", location: config.CdnUrl + "moment" },
            { name: "@dojo", location: config.CdnUrl + "@dojo" },
            {
              name: "cldrjs",
              location: config.CdnUrl + "cldrjs",
              main: "dist/cldr"
            },
            {
              name: "globalize",
              location: config.CdnUrl + "globalize",
              main: "dist/globalize"
            },
            {
              name: "maquette",
              location: config.CdnUrl + "maquette",
              main: "dist/maquette.umd"
            },
            {
              name: "maquette-css-transitions",
              location: config.CdnUrl + "maquette-css-transitions",
              main: "dist/maquette-css-transitions.umd"
            },
            {
              name: "maquette-jsx",
              location: config.CdnUrl + "maquette-jsx",
              main: "dist/maquette-jsx.umd"
            },
            { name: "tslib", location: config.CdnUrl + "tslib", main: "tslib" }
            ]
        if (window.require) {
            window.customRequire = window.require.config(config.BaseRequireJSConfig);
        }
    } else if (config.JupyterTarget === "lab"){
        //delete any existing script tags in a jupyterlab setting
        //TODO: Find a more elegant solution to removing the original script element
        var scriptEl = document.querySelector('script[data-esri-loader]');
        if(scriptEl != null){
            scriptEl.parentNode.removeChild(scriptEl);
        }
    }
}

module.exports = configureCDN;
