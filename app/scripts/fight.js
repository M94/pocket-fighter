// Searches for an image of #name and sets #img.src to it.
function loadImage(name, img)
{
	var size = 400;
	var url = 'http://en.wikipedia.org/w/api.php?action=query&titles=' +
	name + '&pithumbsize=' + size + '&prop=pageimages&continue&format=json';
	$.ajax
	({
		url: url,
		cache: false,
		dataType: 'jsonp',
		xhrFields: {
			withCredentials: true
		},
		success: function(resp)
		{
			for (var key in resp.query.pages);
			img.src = resp.query.pages[key].thumbnail.source;
		}
	});

}

// AJAX object creator
function createXmlHttp() {
	var xmlhttp;
	if (window.XMLHttpRequest) {
		xmlhttp = new XMLHttpRequest();
	} else {
		xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	if (!(xmlhttp)) {
		alert("Your browser does not support AJAX!");
	}
	return xmlhttp;
}

var interval;

function setup_ajax()
{
	
}

function ajax(cmd)
{
	var xmlHttp = createXmlHttp();
	
	xmlHttp.onreadystatechange = function() {
	
		if (xmlHttp.readyState == 4) {
			console.log(xmlHttp.responseText)
			var msg = document.getElementById('message');
			if (xmlHttp.responseText == 0) {
				//no match found, do nothing?
				msg.innerHTML = "Connection error...";
				showMessage();
			}
			else if (xmlHttp.responseText == 1) { 
				showButtons();
			}
			else if (xmlHttp.responseText == 2) { 
				msg.innerHTML = "Waiting for opponent's turn...";
				showMessage();
			}
		}
		
	}
	var uid = document.getElementById('uid').value;
	var mid = document.getElementById('mid').value;
	var param = 'uid=' + escape(uid) + '&mid=' + escape(mid); + '&cmd=' + escape(cmd);
	xmlHttp.open("POST", '/process_fight', true); // Set up link for post request
	xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xmlHttp.send(param); // Send parameters as post request	
}

function showButtons()
{
	document.getElementById("attack1").style.display = "block";
	document.getElementById("attack2").style.display = "block";
	document.getElementById("attack3").style.display = "block";
	document.getElementById("forfeit").style.display = "block";
	document.getElementById("message").style.display = "none";
}

function showMessage()
{
	document.getElementById("attack1").style.display = "none";
	document.getElementById("attack2").style.display = "none";
	document.getElementById("attack3").style.display = "none";
	document.getElementById("forfeit").style.display = "none";
	document.getElementById("message").style.display = "block";
}

// Init functions
showButtons();
loadImage(document.getElementById('fighter1').innerHTML, document.getElementById('photo1'));
loadImage(document.getElementById('fighter2').innerHTML, document.getElementById('photo2'));