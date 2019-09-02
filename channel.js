/*
use another js file in public and export it here
that js file will append report content in a webpage
report content will be passed by the channel.js script
*/

// function to transfer data form node.js to python
//using spawn process
function send_data(data) {

	// create data variable to store arguments to be passed
	// data = [subject, body, seqno, url_list];
	
	// require spawn
	var spawn = require('child_process').spawn;
	var	py = spawn('python',["./python-scripts/analyze.py", data]);
	
	// output string
	var dataString = '';	
	
	// write output of analyze.py to dataString
	py.stdout.on('data', function(data){
  		dataString += data.toString();
	});

	// when analysis over print output
	py.stdout.on('end', function(){
		console.log(dataString);
		// server.send_report(dataString);
		// socket.emit('report', dataString);
		// pass_values(dataString);
	});

	// transfer data to analyze.py
	py.stdin.write(JSON.stringify(data));	
	py.stdin.end();
}

// export send_data()
module.exports = { send_data };
