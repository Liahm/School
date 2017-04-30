var express = require('express');
var mysql = require('mysql');
var app = express();

app.use(express.static('public'))

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '963852aa',
    database: 'mydb',
});

connection.connect(function(error){
    if(error)
    {
        console.log('Error');
    }
    else
    {
        console.log('Connected');
    }
});

app.get('/student', function(req, res){
    connection.query("select * from student;", function(error, rows, field){
        var i = 0;
        if(error)
        {
            console.log('Error in the query');
        }
        else{
            console.log('Running Student Server');
            res.send(rows);
        }
    });
})

app.get('/grades', function(req, res){
    connection.query("select * from grades;", function(error, rows, field){
        var i = 0;
        if(error)
        {
            console.log('Error in the query');
        }
        else{
            console.log('Running Grades Server');
            res.send(rows);

        }
    });
})

app.get('/course', function(req, res){
    connection.query("select * from course;", function(error, rows, field){
        var i = 0;
        if(error)
        {
            console.log('Error in the query');
        }
        else{
            console.log('Running course Server');
            res.send(rows);
        }
    });
})
app.listen(8080);