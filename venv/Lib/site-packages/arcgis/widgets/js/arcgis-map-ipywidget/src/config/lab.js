var config = require("./common");
var configureCdn = require("./configure-cdn");

config.JSOutputContext = "default";
config.JupyterTarget = "lab"; 
configureCdn(config, config.CdnUrl);

module.exports = config;
