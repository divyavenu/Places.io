function initMap() {
  
  var map = new google.maps.Map(document.getElementById('map'), {
    // Map centers on the the Carnegie Mellon Silicon Valley Campus
    zoom: 3,
    center: {lat: 37.4090697, lng: -122.06382530000002},

    // Adds option to switch between map and satellite imagery
    mapTypeControl: true,
    mapTypeControlOptions: {
        style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
        position: google.maps.ControlPosition.TOP_CENTER
    },

    // Adds zoom control panel on the left side of the map
    zoomControl: true,
    zoomControlOptions: {
        position: google.maps.ControlPosition.LEFT_CENTER
    },

    // Allows full screen view
    fullscreenControl: true
  });

  function placeMarker(lat, lng, title) {
    var marker = new google.maps.Marker({
      position: {lat: lat, lng: lng},
      map: map,
      title: title
    });
  }

  function placeMarkerWithInfoWindow(lat, lng, title, infotitle, infoimageurl) {
    // Place a marker with title "infotitle" that renders image at url "infoimageurl"
    var contentString = `<h1>${infotitle}</h1><br>` +
                        `<img src="${infoimageurl}" alt="Pretty Pictures!!" style="width:300px;height:220px;">`;

    var infowindow = new google.maps.InfoWindow({
      content: contentString
    });

    var marker = new google.maps.Marker({
      position: {lat: lat, lng: lng},
      map: map,
      title: title
    });

    marker.addListener('click', function() {
      infowindow.open(map, marker);
    });
  }
// Example code - auto generates one marker on the map every 2 seconds 
// until 20 markers have been generated
/*
var count = 0;
var interval = setInterval(function() {
  placeMarker(Math.random() * 100, Math.random()*-100, 'ANOTHER MARKER');
  count++;
  if (count > 20) {
    clearInterval(interval);
  }
}, 2000);
*/

  // TODO XXX hardcoded example for 7/21 presentation, remove this and use api call instead
  var infourl = 'https://lh3.googleusercontent.com/-Lvy0wxH9-AM/V4wCxtbebMI/AAAAAAAAAAs/wHsJ0Qdu6lQQs-rR-2lywFqxl5Flsjo3gCHM/IMG_4445.jpg';
  var latitude = 39.9037777;
  var longitude = 116.3918916;
  var infotitle = 'IMG_4445.jpg';
  var title = "IMAGE 1";
  placeMarkerWithInfoWindow(latitude, longitude, title, infotitle, infourl);
}

// Adds a script making a call to the google maps API with the appropriate API key
var apiScript = document.createElement('script');

apiScript.setAttribute('async', '');
apiScript.setAttribute('defer','');
apiScript.setAttribute('src','https://maps.googleapis.com/maps/api/js?key=' + 
  GOOGLE_MAPS_API_KEY + '&callback=initMap');

document.body.appendChild(apiScript);