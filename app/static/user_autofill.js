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
    fetch("http://127.0.0.1:5000/location", {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => console.log(response));
}

//Check if user has allowed access to location data
if(window.navigator.geolocation) {
    window.navigator.geolocation.getCurrentPosition(onSuccess, () => console.log('Failed to get user location.'));
}
