var http = require('http');
  fs = require('fs');
var connect =require('connect');
var serveStatic = require('serve-static');

connect().use(serveStatic(__dirname)).listen(8080, function(){
    console.log('server is running...')
});
