var http = require('http');
  fs = require('fs');

fs.readFile('./Website.html', function(err, html)
{
  if(err)
  {
    throw err;
  }
  http.createServer(function(req, res)
  {
    res.writeHead(200, {"Content-Type": "text/html"});
    res.write(html);
    res.end()
  }).listen(8080);
});  
