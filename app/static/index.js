/*
    API Key:
    AIzaSyAJ60DmWOcVVmwHreizFWSfp2EHrTzJIcg
*/

function initMap(){

    /* Autocomplete for the Current Location Input Field */
    autocomplete = new google.maps.places.Autocomplete(document.getElementById("start_input"),
    {
        componentRestrictions: {'country': ['us']},
        fields: ['geometry', 'name'],
        types: ['establishment']
    });
    
    /* Autocomplete for the Destination Input Field */
    autocomplete = new google.maps.places.Autocomplete(document.getElementById("destination_input"),
    {
        componentRestrictions: {'country': ['us']},
        fields: ['geometry', 'name'],
        types: ['establishment']
    });
}