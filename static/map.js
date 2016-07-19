function initMap() {
  
  var map = new google.maps.Map(document.getElementById('map'), {
    // Map centers on the the Carnegie Mellon Silicon Valley Campus
    zoom: 2,
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

// Example code - auto generates one marker on the map every 2 seconds 
// until 20 markers have been generated
var count = 0;
var interval = setInterval(function() {
  placeMarker(Math.random() * 100, Math.random()*-100, 'ANOTHER MARKER');
  count++;
  if (count > 20) {
    clearInterval(interval);
  }
}, 2000);

}

// Adds a script making a call to the google maps API with the appropriate API key
var apiScript = document.createElement('script');

apiScript.setAttribute('async', '');
apiScript.setAttribute('defer','');
apiScript.setAttribute('src','https://maps.googleapis.com/maps/api/js?key=' + 
  GOOGLE_MAPS_API_KEY + '&callback=initMap');

document.body.appendChild(apiScript);