// setup the application
var channel = require('./channel.js');

var express = require('express');
var app = express();			// function handler used to supply an HTTP server
const http = require('http').Server(app); // HTTP server
const port = process.env.PORT || 3000;
var io = require('socket.io')(http);
var channel = require('./channel.js');

app.use(express.static(__dirname + '/public'));

// routes
app.get('/', function(req, res){1
	res.stausCode = 200;
	res.sendFile(__dirname + '/public/index.html');
});

io.on('connection', function(socket){	
	
	socket.on('create', function(data){		
		// console.log(data);
		channel.send_data(data);
	});
	/*
	socket.on('report', function(data){		
		console.log(data);
		// channel.send_data(data);
	});*/
});

http.listen(port, () => {
    console.log('Server is up on port ' + port);
});
/*
function send_report(data) {
	console.log(data);
}

module.exports = { send_report };
*/
