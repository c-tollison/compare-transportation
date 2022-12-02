/*
    The function of this script is to attempt to get the user's
    current location from the browser if they allow it. If permission
    is granted, their location is taken as lat. and long. coords. and
    then converted into an address using Google API's geocoding.
    Once the address is obtained, the data is posted to the flask app
    for further processing, and the address is autofilled into the 
    text input field for starting location.
*/

//Should be the base url of the flask app
const baseURL = 'http://127.0.0.1:5000/';

const onSuccess = async (result) => {
    //Data object to be sent to flask app
    data = {
        latitude: result.coords.latitude,
        longitude: result.coords.longitude,
        address: ''
    }

    //Geocode coords into address
    geocoder = new google.maps.Geocoder();
    await geocoder.geocode({location: {lat: result.coords.latitude, lng: result.coords.longitude}}).then(response => {
        data.address = response.results[0].formatted_address;
    });

    //Post data to flask app
    await fetch(`${baseURL}/location`, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(data)
    });

    //Set the value of starting location input
    document.getElementById('start_input').setAttribute('value', data.address);
}

//Don't allow for location processing until the whole DOM has loaded to ensure that Google Maps API has been defined.
addEventListener('load', () => {
    //Check if user has allowed access to location data and process their location if they have.
    if(window.navigator.geolocation) {
        window.navigator.geolocation.getCurrentPosition(onSuccess, () => console.log('Failed to get user location.'));
    }
});