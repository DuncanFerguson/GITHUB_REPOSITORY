const path = require('path');
const version = require('./package.json').version;
const merge = require('webpack-merge');
const common = require("./webpack.common.js");
const webpack = require("webpack");

//Use the config/notebook.js file for all "require('config')" statements
nbResolve = {
    alias: {
            config: path.join(__dirname, 'src', 'config', 'notebook')
        }
}

embedResolve = {
    alias: {
            config: path.join(__dirname, 'src', 'config', 'embed')
    }
}

module.exports = [
     merge(common, {
     // Notebook extension
     //
     // This bundle only contains the part of the JavaScript that is run on
     // load of the notebook. This section generally only performs
     // some configuration for requirejs, and provides the legacy
     // "load_ipython_extension" function which is required for any notebook
     // extension.
     //
        entry: './src/extension.js',
        output: {
            filename: 'extension.js',
            path: path.resolve(__dirname, 'dist'),
            libraryTarget: 'amd'
        },
         resolve: nbResolve
    }),
    merge(common, {
    // Bundle for the notebook containing the custom widget views and models
     //
     // This bundle contains the implementation for the custom widget views and
     // custom widget.
     // It must be an amd module
     //
        entry: './src/index.js',
        output: {
            filename: 'arcgis-map-ipywidget.js',
            path: path.resolve(__dirname, 'dist'),
            libraryTarget: 'amd'
        },
        resolve: nbResolve
    }),
    merge(common, {
     // Embeddable widgets bundle
     //
     // This bundle is generally almost identical to the notebook bundle
     // containing the custom widget views and models.
     //
     // The only difference is in the configuration of the webpack public path
     // for the static assets.
     //
     // It will be automatically distributed by unpkg to work with the static
     // widget embedder.
     //
     // The target bundle is always `dist/index.js`, which is the path required
     // by the custom widget embedder.
     //
        entry: './src/embed.js',
        output: {
            filename: 'index.js',
            path: path.resolve(__dirname, 'dist'),
            libraryTarget: 'amd',
            publicPath: 'https://unpkg.com/arcgis-map-ipywidget@' + version + '/dist/'
        },
        resolve: embedResolve,
        externals: [],
    })
];
