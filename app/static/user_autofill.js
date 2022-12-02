const onSuccess = async (result) => {
    geocoder = new google.maps.Geocoder();
    data = {
        latitude: result.coords.latitude,
        longitude: result.coords.longitude,
        address: ''
    }
    await geocoder.geocode({location: {lat: result.coords.latitude, lng: result.coords.longitude}}).then(response => {
        data.address = response.results[0].formatted_address;
    });
    await fetch("http://127.0.0.1:5000/location", {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => console.log(response));
    //window.location = 'http://127.0.0.1:5000/';
    document.getElementById('current_location_input').setAttribute('value', data.address);
}

//Don't allow for location processing until the whole DOM has loaded to ensure that Google Maps API has been defined
addEventListener('load', () => {
    //Check if user has allowed access to location data
    if(window.navigator.geolocation) {
        window.navigator.geolocation.getCurrentPosition(onSuccess, () => console.log('Failed to get user location.'));
    }
});