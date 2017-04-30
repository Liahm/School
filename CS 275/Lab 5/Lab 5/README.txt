To run you might have to update Lab5.js file
In line 7, where this code starts
var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '963852aa',
    database: 'mydb',
});

Change the user/password/database to yours.

To run this program make sure that the index.html file is inside the public folder.
Then in node.js do
$ npm install express

After that just run the Lab5.js by node Lab5.js
links:
./student - for student JSON information
./grades - for grades JSON information
./course - for course JSON information
./ or ./index.html - for the main website