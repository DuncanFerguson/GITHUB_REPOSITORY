var config = require("./common");

config.CdnUrl = "https:" + config.CdnUrl;

config.JSOutputContext = "embed";

config.BaseRequireJSConfig = {
   packages: [{ name: "esri", location: config.CdnUrl + "esri" },
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
    ],
    
    /*[{
        name: 'esri',
        location: config.CdnUrl + 'esri',
        },{
        name: 'dojo',
        location: config.CdnUrl + 'dojo'
        },{
        name:'dojox',
        location: config.CdnUrl + "dojox"
        },{
        name: "dijit",
        location: config.CdnUrl + "dijit"
        },{
        name: "dgrid",
        location: config.CdnUrl + "dgrid",
        },{
        name: "xstyle",
        location: config.CdnUrl + "xstyle",
        },{
        name: "put-selector",
        location: config.CdnUrl + "put-selector",
        },{
        name: "moment",
        location: config.CdnUrl + "moment",
        },{
        name: "maquette",
        location: config.CdnUrl + "esri/widgets/libs/maquette"
        }
    ],*/
    config: {
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

config.JupyterTarget = "notebook"; 

module.exports = config;
