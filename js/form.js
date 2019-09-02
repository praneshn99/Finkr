var socket = io().connect();

var ele = $("form").serializeArray();

$(document).ready(function(){
  $("button").click(function(){
  	var data = [];
    var x = $("form").serializeArray();
    $.each(x, function(i, field){
      data.push({
      	key: field.name,
      	value: field.value
      });
      //data.push(field.name + ' ' + field.value);
      //[field.name] = field.value;//$("#results").append(field.name + ":" + field.value + " ");
    });
    // alert(data[0].value);
    socket.emit('create', data);
  });
});
